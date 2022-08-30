package main

import "go.uber.org/zap"

// New create a new logger
func New(level string) (*zap.Logger, error) {
	// создаем когфиг
	cfg := zap.NewProductionConfig()

	// задаем минимальный уровень логирования
	cfg.Level = zap.NewAtomicLevelAt(zap.DebugLevel)

	// задаем уровень логирования приложения
	atom := zap.NewAtomicLevel()
	err := atom.UnmarshalText([]byte(level))
	if err != nil {
		return nil, err
	}
	cfg.Level = atom

	// куда выводим
	cfg.OutputPaths = []string{"stdout"}

	// Конфигурируем формат выводимого времени (если нужно поменять)
	//cfg.EncoderConfig.EncodeTime = CustomMillisTimeEncoder

	return cfg.Build()
}
