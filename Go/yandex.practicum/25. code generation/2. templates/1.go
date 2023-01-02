package main

import (
	"os"
	"text/template"
)

type Data struct {
	Name  string
	Group int
	Score []int
}

const Template = `
{{range .}}
Студент: {{.Name}} {{if .Group}}/ Группа: {{.Group}}{{end}}
Оценки: {{range .Score}}{{.}} {{end}}
{{end}}
`

func main() {
	data := []Data{
		{
			Name:  `Василий Пупкин`,
			Score: []int{3, 4, 2, 5, 4},
		},
		{
			Name:  `Лилия Иванова`,
			Group: 708,
			Score: []int{4, 5, 4, 5, 5},
		},
	}
	t := template.Must(template.New("list").Parse(Template))

	err := t.Execute(os.Stdout, data)
	if err != nil {
		panic(err)
	}
}

/*
Студент: Василий Пупкин
Оценки: 3 4 2 5 4

Студент: Лилия Иванова / Группа: 708
Оценки: 4 5 4 5 5
*/
