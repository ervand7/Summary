#include <stdio.h>

int main(void)
{
    double heigh, a;
    int count_input_values = scanf("%lf %lf", &heigh, &a);
    if(count_input_values != 2) {
        printf("Error");
        return 0;
    }

    double sq = heigh * a / (float)2;
    printf("%.2f\n", sq);

    return 0;
}