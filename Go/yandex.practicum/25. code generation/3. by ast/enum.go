package main

//go:generate go run genenum.go HTTPCode

type HTTPCode int

const (
    BadRequest      HTTPCode = 400
    Unauthorized    HTTPCode = 401
    Forbidden       HTTPCode = 403
    NotFound        HTTPCode = 404
    TooManyRequests HTTPCode = 429 // alert: DDOS alert, call admins!
    Internal        HTTPCode = 500
)