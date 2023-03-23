#include <stdio.h>

int main(void)
{
    int value = getchar();
    printf("%c\n", value);

    int result = putchar(value);
    printf("\n%d\n", result);
    return 0;
}