#include <stdio.h>

int main(void)
{
    int age;
    scanf("%d", &age);
    if (age >= 18 && age < 45)
        printf("Входи");
    else if (age >= 45 && age < 65)
        printf("Вам точно понравится эта музыка?");
    else if (age >= 65)
        printf("Это уже слишком для вас");
    else
        printf("Тебе нет 18");
    return 0;
}
