package main

import (
	"context"
	"errors"

	"golang.org/x/sync/errgroup"
	"golang.org/x/sync/semaphore"
	"golang.org/x/sync/singleflight"
)

type PostID string

type Post struct {
	ID      PostID
	Content string
}

type PostProvider interface {
	GetPost(ctx context.Context, postID PostID) (*Post, error)
}

type BatchPostProvider interface {
	GetPosts(ctx context.Context, postIDs []PostID) (map[PostID]*Post, error)
}

type batchPostProvider struct {
	provider PostProvider
	sflgrp   *singleflight.Group // для переиспользования результатов
	sem      *semaphore.Weighted // для поддержки очереди запросов к PostProvider
}

// NewbatchPostProvider конструктор
func NewbatchPostProvider(p PostProvider, n int64) *batchPostProvider {
	b := new(batchPostProvider)
	b.provider = p
	b.sflgrp = new(singleflight.Group)
	b.sem = semaphore.NewWeighted(n) // лимит очереди запросов n
	return b
}

func (p *batchPostProvider) GetPosts(
	ctx context.Context, postIDs []PostID,
) (map[PostID]*Post, error) {
	grp, ctx := errgroup.WithContext(ctx)
	posts := make([]*Post, len(postIDs))
	for i, id := range postIDs {
		index, idx := i, id
		grp.Go(func() error {
			// используем новый метод запроса с кешированием результатов
			post, err := p.SingleGetPost(ctx, idx)
			if err != nil {
				return err
			}
			posts[index] = post
			return nil
		})
	}
	if err := grp.Wait(); err != nil {
		return nil, err
	}
	return p.collectPostsByIDs(postIDs, posts), nil
}

func (p *batchPostProvider) collectPostsByIDs(
	ids []PostID, posts []*Post,
) map[PostID]*Post {
	result := make(map[PostID]*Post, len(ids))
	for i, id := range ids {
		result[id] = posts[i]
	}
	return result
}

// SingleGetPost метод с той же сигнатурой, что и GetPost, но переиспользующий
// результаты запросов и поддерживающий очередь семафора
func (p *batchPostProvider) SingleGetPost(
	ctx context.Context, postID PostID,
) (*Post, error) {
	// лямбда-функция в аргументе будет вызвана только один раз для каждого ключа postID
	// для передачи параметров используем замыкание — closure
	post, err, _ := p.sflgrp.Do(string(postID), func() (interface{}, error) {
		// если возможно, занимаем место в очереди семафора
		if !p.sem.TryAcquire(1) {
			// если очередь переполнена, возвращаем ошибку
			return nil, errors.New("too many requests")
		}
		pst, er := p.provider.GetPost(ctx, postID)
		// освобождаем место в очереди семафора
		p.sem.Release(1)
		return pst, er
	})
	if err != nil {
		return nil, err
	}
	// неудобство функций, возвращающих интерфейсы,
	// в том, что необходим type assertion
	return post.(*Post), nil
}
