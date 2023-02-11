package job

import (
	"context"
	"fmt"
	"net/smtp"
	"strings"

	"github.com/tmvrus/pqueue/model"
)

const repeatableErrorToken = "timeout"

type Email struct {
	addr, from string
	message    []byte
	to         []string
	auth       smtp.Auth
}

func (e Email) Execute(_ context.Context) error {
	if err := smtp.SendMail(e.addr, e.auth, e.from, e.to, e.message); err != nil {
		if strings.Contains(err.Error(), repeatableErrorToken) {
			return fmt.Errorf("%w, try again later: %s", model.ErrRepeatable, err.Error())
		}
		return fmt.Errorf("failed to send email: %w", err)
	}
	return nil
}
