#include <stdio.h>

int main(void)
{
    int count = 0, size = 5;
    int current = count++;

    int width = ++size;
    printf("count = %d, size = %d, current = %d, width = %d\n",
                                    count, size, current, width);
    // count = 1, size = 6, current = 0, width = 6
    return 0;
}