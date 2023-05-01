package main

import (
	"errors"
	"fmt"
	"io"
	"math/rand"
	"time"
)

type Data struct {
	Line string
}

// Xenia type represents a system that I need to pull data from.
// The implementation is not important. What is important is that the
// method Pull can succeed, fail, or not have any data to pull.
type Xenia struct {
	Host    string
	Timeout time.Duration
}

func (*Xenia) Pull(d *Data) error {
	switch rand.Intn(10) {
	case 1, 9:
		return io.EOF
	case 5:
		return errors.New("error reading data from Xenia")
	default:
		d.Line = "Data"
		fmt.Println("In:", d.Line)
		return nil
	}
}

// Pillar type represents a system that I need to store data into. What is
// important again is that the method Store can succeed or fail.
type Pillar struct {
	Host    string
	Timeout time.Duration
}

func (*Pillar) Store(d *Data) error {
	fmt.Println("Out:", d.Line)
	return nil
}

/*
These two types represent a primitive layer of code that provides the
base behavior required to solve the business problem of pulling data
out of Xenia and storing that data into Pillar.
*/

/*
The next layer of code is represented by these two functions, Pull and Store.
They build on the primitive layer of code by accepting a collection
of data values to pull or store in the respective systems.
These functions focus on the concrete types of Xenia and Pillar
since those are the systems the program needs to work with at this time.
*/

func Pull(x *Xenia, data []Data) (int, error) {
	for i := range data {
		if err := x.Pull(&data[i]); err != nil {
			return i, err
		}
	}
	return len(data), nil
}

func Store(p *Pillar, data []Data) (int, error) {
	for i := range data {
		if err := p.Store(&data[i]); err != nil {
			return i, err
		}
	}
	return len(data), nil
}

// System idea is to compose a system that knows how to Pull and Store.
// In this case, composing the ability to Pull and Store
// from Xenia and Pillar.
type System struct {
	Xenia
	Pillar
}

// Copy function builds on top of the Pull and Store functions to move all
// the data that is pending for each run. If I notice the first parameter
// to Copy, it’s a type called System.
func Copy(sys *System, batch int) error {
	data := make([]Data, batch)
	for {
		i, err := Pull(&sys.Xenia, data)
		if i > 0 {
			if _, err := Store(&sys.Pillar, data[:i]); err != nil {
				return err
			}
		}
		if err != nil {
			return err
		}
	}
}

// Finally, the main function can be written to construct a Xenia and Pillar
// within the composition of a System. Then the System can be passed to
// the Copy function and data can begin to flow between the two systems.
//
// With all this code, I now have my first draft of a concrete solution to
// a concrete problem.
func main() {
	sys := System{
		Xenia: Xenia{
			Host:    "localhost:8000",
			Timeout: time.Second,
		},
		Pillar: Pillar{
			Host:    "localhost:9000",
			Timeout: time.Second,
		},
	}
	if err := Copy(&sys, 3); err != io.EOF {
		fmt.Println(err)
	}
}
