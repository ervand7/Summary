package job

import (
	"context"
	"fmt"
	"net/http"

	"github.com/tmvrus/pqueue/model"
)

type CallbackRequest struct {
	req    *http.Request
	client *http.Client
}

func NewCallbackRequest(r *http.Request, c *http.Client) CallbackRequest {
	return CallbackRequest{r, c}
}

func (r CallbackRequest) Execute(ctx context.Context) error {
	req := r.req.WithContext(ctx)
	res, err := r.client.Do(req)
	if err != nil {
		return fmt.Errorf("failed to perform request: %w", err)
	}
	if res.StatusCode == http.StatusGatewayTimeout || res.StatusCode == http.StatusTooManyRequests {
		return fmt.Errorf("%w: got repeateble status code: %s", model.ErrRepeatable, res.Status)
	}
	return nil
}
