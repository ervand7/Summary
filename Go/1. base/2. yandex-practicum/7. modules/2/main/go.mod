module main

go 1.18

replace workspace/user/repo => ../somemodule

// go get workspace/user/repo
require workspace/user/repo v0.0.0-00010101000000-000000000000 // indirect
