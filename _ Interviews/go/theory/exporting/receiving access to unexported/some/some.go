package some

type ivan int

// NewIvan Лучше вместо этого возвращать экспортируемый интерфейс
func NewIvan(value int) ivan {
	return ivan(value)
}

var VarOfNonExportType ivan
