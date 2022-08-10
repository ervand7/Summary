module main

go 1.18

replace (
	company => ../company
	person => ../person
	robot => ../robot
)

require (
	company v0.0.0-00010101000000-000000000000 // indirect
	person v0.0.0-00010101000000-000000000000 // indirect
	robot v0.0.0-00010101000000-000000000000 // indirect
)
