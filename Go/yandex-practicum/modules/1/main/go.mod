module main

go 1.18

// директивой replace указываем положение корня
// модуля ypmodule относительно main/go.mod
// go get ypmodule
replace ypmodule => ../ypmodule

require ypmodule v0.0.0-00010101000000-000000000000 // indirect
