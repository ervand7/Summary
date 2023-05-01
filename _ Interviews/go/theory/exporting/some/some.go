package some

type ervand int

func NewErvand(value int) ervand {
	return ervand(value)
}

var VarOfNonExportType ervand
