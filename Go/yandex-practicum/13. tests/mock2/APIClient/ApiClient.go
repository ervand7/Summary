package ApiClient

type APIClient interface {
	GetData(query string) (Response, error)
}

type Response struct {
	Text       string
	StatusCode int
}

type MockAPIClient interface {
	APIClient
	SetResponse(resp Response, err error)
}

type Mock struct {
	Resp Response
	Err  error
}

func (m *Mock) GetData(query string) (Response, error) {
	return m.Resp, m.Err
}

func (m *Mock) SetResponse(resp Response, err error) {
	m.Resp = resp
	m.Err = err
}
