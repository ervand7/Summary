package main

import (
	"context"
	"sync"
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
}

// строка ниже не несёт функциональной нагрузки
// её можно убрать без последствий для работы программы
// это отладочная строка
// в этой строке приведением типов проверяем,
// реализует ли *batchPostProvider интерфейс BatchPostProvider —
// если нет, если методы прописаны неверно,
// то компилятор выдаст на этой строке ошибку типизации
var _ BatchPostProvider = (*batchPostProvider)(nil)

func (p *batchPostProvider) GetPosts(
	ctx context.Context, postIDs []PostID,
) (map[PostID]*Post, error) {
	var wg sync.WaitGroup
	wg.Add(len(postIDs))

	ctxWithCancel, cancel := context.WithCancel(ctx)
	defer cancel()

	errs := make([]error, len(postIDs))
	posts := make([]*Post, len(postIDs))
	for i := range postIDs {
		go func(id int) {
			defer wg.Done()
			post, err := p.provider.GetPost(ctxWithCancel, postIDs[id])
			if err != nil {
				errs[id] = err
				if err != context.Canceled {
					// если один из вызовов завершился ошибкой,
					// можем сразу завершать все остальные горутины
					cancel()
				}
			} else {
				posts[id] = post
			}
		}(i)
	}

	wg.Wait()

	for _, err := range errs {
		if err != nil {
			return nil, err
		}
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
