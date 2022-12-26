package example

import (
	"net/http"
	"time"
)

// @Title BucketStorage API
// @Description Сервис хранения данных bucket-ов.
// @Version 1.0

// @Contact.email support@ultimatestore.io

// @BasePath /api/v1
// @Host ultimatestore.io:8080

// @SecurityDefinitions.apikey ApiKeyAuth
// @In header
// @Name authorization

// @Tag.name Info
// @Tag.description "Группа запросов состояния сервиса"

// @Tag.name Storage
// @Tag.description "Группа для работы с данными внутри bucket-ов"

type (
	// HealthResponse содержит информацию о состоянии сервиса.
	HealthResponse struct {
		// Статус сервиса
		State string `json:"state" enums:"Bootstrap,Online,Failed" example:"Online"`
		// Время работы сервиса с последнего старта [с]
		UpTime int64 `json:"uptime" format:"seconds" example:"500"`
		// Доступное место [байт]
		FreeSpace int64 `json:"free_space" format:"bytes" example:"1048576"`
	}

	// BucketResponse содержит данные bucket-а с дополнительной метаинформацией.
	BucketResponse struct {
		Id        int64     `json:"id"`
		Data      string    `json:"data" format:"HEX / Base64" example:"48656c6c6f20776f726c6421"`
		UpdatedAt time.Time `json:"updated_at" format:"RFC3339" example:"2006-01-02T15:04:05.999999999Z07:00"`
	}

	// BucketRequest содержит запрос на обновление данных bucket-а.
	BucketRequest struct {
		Data string `json:"data" format:"HEX" example:"48656c6c6f20776f726c6421"`
	}
)

// Health godoc
// @Tags Info
// @Summary Запрос состояния сервиса
// @ID infoHealth
// @Accept  json
// @Produce json
// @Success 200 {object} HealthResponse
// @Failure 500 {string} string "Внутренняя ошибка"
// @Router /info/health [get]
func Health(w http.ResponseWriter, r *http.Request) {
	// опустим реализацию
}

// GetBucket godoc
// @Tags Storage
// @Summary Запрос содержимого bucket-а
// @Description Запрос содержимого bucket-а по ID
// @ID storageGetBucket
// @Accept  json
// @Produce json
// @Param bucket_id path int64 true "Bucket ID"
// @Param data_format query string false "Формат поля data" Enums(HEX, Base64) default(HEX)
// @Success 200 {object} BucketResponse
// @Failure 400 {string} string "Неверный запрос"
// @Failure 403 {string} string "Ошибка авторизации"
// @Failure 404 {string} string "Bucket не найден"
// @Failure 500 {string} string "Внутренняя ошибка"
// @Security ApiKeyAuth
// @Router /storage/bucket/{bucket_id} [get]
func GetBucket(w http.ResponseWriter, r *http.Response) {
	// опустим реализацию
}

// SetBucket godoc
// @Tags Storage
// @Summary Сохранение содержимого bucket-а
// @Description Создание нового / обновление существующего bucket-а по ID
// @ID storageSetBucket
// @Accept  json
// @Produce json
// @Param bucket_id path int64 true "Bucket ID"
// @Param bucket_data body BucketRequest true "Содержимое bucket-а"
// @Success 200 {string} string "OK"
// @Failure 400 {string} string "Неверный запрос"
// @Failure 403 {string} string "Ошибка авторизации"
// @Failure 500 {string} string "Внутренняя ошибка"
// @Security ApiKeyAuth
// @Router /storage/bucket/{bucket_id} [post]
func SetBucket(w http.ResponseWriter, r *http.Response) {
	// опустим реализацию
}
