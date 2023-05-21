package job

import (
	"context"
	"fmt"
)

type Report struct {
	from, to string
	store    interface {
		StoreReport(ctx context.Context, result []byte) error
	}
	reporter interface {
		GenerateReport(ctx context.Context, from, to string) ([]byte, error)
	}
}

func (r Report) Execute(ctx context.Context) error {
	data, err := r.reporter.GenerateReport(ctx, r.from, r.to)
	if err != nil {
		return fmt.Errorf("failed to generate report: %w", err)
	}
	err = r.store.StoreReport(ctx, data)
	if err != nil {
		return fmt.Errorf("failed to store report: %w", err)
	}
	return nil
}
