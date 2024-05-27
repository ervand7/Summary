package main

import (
	"fmt"

	"github.com/aws/aws-lambda-go/lambda"
)

// Request represents the requested object
type Request struct {
	ID    int    `json:"ID"`
	Value string `json:"Value"`
}

// Response represents the Response object
type Response struct {
	Message string `json:"Message"`
	Ok      bool   `json:"Ok"`
}

// Handler represents the Handler of lambda
func Handler(request Request) (Response, error) {
	return Response{
		Message: fmt.Sprintf("Process Request Id %d", request.ID),
		Ok:      true,
	}, nil
}

func main() {
	lambda.Start(Handler)
}
