#include <stdio.h>

/*
symbols - is the same rune in Go:
func main() {
	a := 'd'
	fmt.Printf("%d", a)  // 100
}
*/

int main(void)
{
    char ch;
    ch = 'd';
    printf("ch = %c, code = %d\n", ch, ch);  // ch = d, code = 100

    return 0;
}