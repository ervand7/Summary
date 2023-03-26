#include <stdio.h>

// format specifiers in C: https://www.freecodecamp.org/news/format-specifiers-in-c/

int main(void)
{
    int a = 1208;
    printf("value = %d\n", a);
    printf("value = %x\n", a);
    printf("value = %u\n", a);

    long long b = -12312312313123123;
    printf("value = %lld\n", b);

    return 0;
}