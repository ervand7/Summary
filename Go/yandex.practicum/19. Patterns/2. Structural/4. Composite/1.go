package main

import "fmt"

/*
Компоновщик — это структурный паттерн, который группирует множество объектов в
древовидную структуру и позволяет работать как с отдельными объектами,
так и с группой объектов.
Паттерн Компоновщик используется, когда:
 - нужно реализовать объекты в виде древовидной структуры;
 - отдельные объекты и их группы должны реализовывать один и тот же интерфейс.
Для примера возьмём файлы и директории и реализуем
возможность напечатать их имя и размер.
*/

// Component — общий интерфейс для файлов и директорий.
type Component interface {
	Print(string)
	GetSize() int
}

type File struct {
	Name string
	Size int
}

func (f *File) Print(prefix string) {
	fmt.Println(prefix+f.Name, f.Size)
}

func (f *File) GetSize() int {
	return f.Size
}

type Dir struct {
	Name     string
	Children []Component
}

// Print печатает имя директории, её размер и содержимое.
func (d *Dir) Print(prefix string) {
	fmt.Println(prefix+d.Name, d.GetSize())
	for _, v := range d.Children {
		v.Print(prefix + "  ")
	}
}

// GetSize возвращает общий размер всех файлов в директории.
func (d *Dir) GetSize() int {
	var sum int
	for _, v := range d.Children {
		sum += v.GetSize()
	}
	return sum
}

func main() {
	root := &Dir{
		Children: []Component{
			&File{Name: "file1", Size: 778},
			&File{Name: "file2", Size: 222},
			&Dir{
				Children: []Component{
					&File{Name: "file3", Size: 64},
					&File{Name: "file4", Size: 36},
				},
				Name: "subfolder",
			},
		},
		Name: "root",
	}
	root.Print("")
}

/*
root 1100
  file1 778
  file2 222
  subfolder 100
    file3 64
    file4 36
*/
