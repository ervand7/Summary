package main

import (
	"golang.org/x/tools/go/analysis"
	"golang.org/x/tools/go/analysis/multichecker"
	"honnef.co/go/tools/staticcheck"
)

/*
Если скомпилировать программу, получится статический анализатор с проверкой
трёх правил из staticcheck. В примере список правил указан в исходном коде.
На практике лучше получать этот список из внешних источников, например из
файла конфигурации.
*/

func main() {
	// определяем map подключаемых правил
	checks := map[string]bool{
		"SA5000": true,
		"SA6000": true,
		"SA9004": true,
	}
	var mychecks []*analysis.Analyzer
	for _, v := range staticcheck.Analyzers {
		// добавляем в массив нужные проверки
		if checks[v.Analyzer.Name] {
			mychecks = append(mychecks, v.Analyzer)
		}
	}
	multichecker.Main(
		mychecks...,
	)
}
