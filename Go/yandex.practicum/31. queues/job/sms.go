package job

import (
	"context"
	"fmt"
)

type SMS struct {
	phone   uint8
	message []byte
	gateway interface {
		Send(ctx context.Context, phone uint8, message []byte) error
	}
}

func (s SMS) Execute(ctx context.Context) error {
	if err := s.gateway.Send(ctx, s.phone, s.message); err != nil {
		return fmt.Errorf("failed to send sms to +%d: %w", s.phone, err)
	}
	return nil
}
