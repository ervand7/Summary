package main

import "fmt"

/*
В языке Go есть метки (labels), которые позволяют перемещаться к разным частям кода.
Метку можно указать для операторов:
break;
continue;
goto (безусловный оператор перехода, позволяет перейти в любое место кода).
*/
func main() {
	// for break
outerLoopLabel:
	for i := 0; i < 5; i++ {
		for j := 0; j < 5; j++ {
			fmt.Printf("[%d, %d]\n", i, j)
			break outerLoopLabel
		}
	}
	fmt.Println("End")
	/*
		[0, 0]
		End
	*/

	//for continue
outerLoopLabel_:
	for i := 0; i < 5; i++ {
		for j := 0; j < 5; j++ {
			fmt.Printf("[%d, %d]\n", i, j)
			continue outerLoopLabel_
		}
	}
	fmt.Println("End")
	/*
		[0, 0]
		[1, 0]
		[2, 0]
		[3, 0]
		[4, 0]
		End
	*/
}
