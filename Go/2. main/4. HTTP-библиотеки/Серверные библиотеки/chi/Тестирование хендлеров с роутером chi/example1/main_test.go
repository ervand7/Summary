package main

import (
	"github.com/stretchr/testify/assert"
	"github.com/stretchr/testify/require"
	"io/ioutil"
	"net/http"
	"net/http/httptest"
	"testing"
)

func testRequest(t *testing.T, ts *httptest.Server, method, path string) (*http.Response, string) {
	req, err := http.NewRequest(method, ts.URL+path, nil)
	require.NoError(t, err)

	resp, err := http.DefaultClient.Do(req)
	require.NoError(t, err)

	respBody, err := ioutil.ReadAll(resp.Body)
	defer resp.Body.Close()
	require.NoError(t, err)

	return resp, string(respBody)
}

func TestNewRouter(t *testing.T) {
	r := NewRouter()
	ts := httptest.NewServer(r)
	defer ts.Close()

	resp, body := testRequest(t, ts, "GET", "/cars/renault")
	assert.Equal(t, http.StatusOK, resp.StatusCode)
	assert.Equal(t, "brand:renault", body)

	resp, body = testRequest(t, ts, "GET", "/cars/bmw")
	assert.Equal(t, http.StatusOK, resp.StatusCode)
	assert.Equal(t, "brand:bmw", body)

	resp, body = testRequest(t, ts, "GET", "/cars/hello")
	assert.Equal(t, http.StatusOK, resp.StatusCode)
	assert.Equal(t, "brand:hello", body)

	resp, body = testRequest(t, ts, "GET", "/cars/bmw/x5")
	assert.Equal(t, http.StatusOK, resp.StatusCode)
	assert.Equal(t, "brand and model:bmw-x5", body)
}
