#include <iostream>

int main()
{
    const int N = 20;
    char marks[N] = {2, 4, 2, 3};
    int count_marks = 4;

    int index_del = 0;
    for (int i = index_del; i < count_marks; ++i)
        marks[i] = marks[i + 1];

    if (count_marks > 0) count_marks--;

    for (int i = 0; i < count_marks; ++i)
        printf("%d ", marks[i]);
        
    return 0;
}