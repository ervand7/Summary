package main

import (
	"fmt"
	"strings"
)

// Приведём пример простейшего прокси-сервера.

// Server — интерфейс веб-сервера.
type Server interface {
	handleRequest(string, string) (int, string)
}

// WebServer — сервер по умолчанию.
type WebServer struct {
}

// Proxy — прокси-сервер.
type Proxy struct {
	WebServer *WebServer
}

func NewProxyServer(webServer *WebServer) *Proxy {
	return &Proxy{
		WebServer: webServer,
	}
}

func (p *Proxy) handleRequest(url, method string) (int, string) {
	// запрещает доступ к /api/admin
	if strings.HasPrefix(url, "/api/admin") {
		return 403, "Forbidden"
	}
	return p.WebServer.handleRequest(url, method)
}

func (webServer *WebServer) handleRequest(url, method string) (int, string) {
	if !strings.HasPrefix(url, "/api/") {
		return 400, "Bad Request"
	}
	return 200, fmt.Sprintf("%s Request: %s", method, url)
}

func main() {
	proxyServer := NewProxyServer(&WebServer{})
	for _, v := range []string{"/api/info", "/api/admin", "/api/version", "/admin"} {
		httpCode, body := proxyServer.handleRequest(v, "GET")
		fmt.Println(v, httpCode, body)
	}
}

/*
/api/info 200 GET Request: /api/info
/api/admin 403 Forbidden
/api/version 200 GET Request: /api/version
/admin 400 Bad Request
*/

// Ошибку 403 Forbidden вернул прокси-сервер.
