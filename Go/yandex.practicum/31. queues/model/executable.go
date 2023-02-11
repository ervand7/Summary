package model

import "context"

type Executable interface {
	Execute(ctx context.Context) error
}
