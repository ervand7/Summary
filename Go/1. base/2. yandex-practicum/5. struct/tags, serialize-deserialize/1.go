package main

type GetUserRequest struct {
	UserId    string `json:"user_id" yaml:"user_id" format:"uuid" example:"2e263a90-b74b-11eb-8529-0242ac130003"`
	IsDeleted *bool  `json:"is_deleted,omitempty" yaml:"is_deleted"`
}

func main() {
}
