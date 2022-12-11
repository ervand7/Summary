package main

// Factory — абстрактная фабрика
type Factory interface {
	MakeChair(string) ChairMaker
	MakeTable(string) TableMaker
}

// ArtDeco — фабрика ар-деко
type ArtDeco struct {
}

func (a *ArtDeco) MakeChair(wood string) ChairMaker {
	var chair Chair
	chair.SetStyle("ар-деко")
	chair.SetWood(wood)
	return &chair
}

func (a *ArtDeco) MakeTable(wood string) TableMaker {
	var table Table
	table.SetStyle("ар-деко")
	table.SetWood(wood)
	return &table
}

// Modern — фабрика модерна
type Modern struct {
}

func (m *Modern) MakeChair(wood string) ChairMaker {
	var chair Chair
	chair.SetStyle("модерн")
	chair.SetWood(wood)
	return &chair
}

func (m *Modern) MakeTable(wood string) TableMaker {
	var table Table
	table.SetStyle("модерн")
	table.SetWood(wood)
	return &table
}

// GetFactory — абстрактная фабрика
func GetFactory(style string) Factory {
	if style == "art-deco" {
		return &ArtDeco{}
	}
	if style == "modern" {
		return &Modern{}
	}
	return nil
}
