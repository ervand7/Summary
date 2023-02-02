package main

import (
	"context"

	"golang.org/x/sync/errgroup"
)

func (p *batchPostProvider) _GetPosts(
	ctx context.Context, postIDs []PostID,
) (map[PostID]*Post, error) {
	group, ctx := errgroup.WithContext(ctx)

	posts := make([]*Post, len(postIDs))
	for i, id := range postIDs {
		// нельзя использовать переменные цикла i и id в горутине,
		// так как, вероятнее всего, горутина получит только их конечные значения,
		// поэтому определяем переменные внутри цикла
		index, idx := i, id

		group.Go(func() error {
			post, err := p.provider.GetPost(ctx, idx)
			if err != nil {
				return err
			}

			posts[index] = post
			return nil
		})
	}

	if err := group.Wait(); err != nil {
		return nil, err
	}

	return p.collectPostsByIDs(postIDs, posts), nil
}
