#include <iostream>

int main()
{
    const int N = 20;
    char marks[N] = {2, 2, 3};
    int count_marks = 3;

    int index_insert = 1;
    int end = (count_marks < N) ? count_marks : N - 1;
    for (int i = end; i > index_insert; --i)
        marks[i] = marks[i - 1];
    marks[index_insert] = 4;
    if (count_marks < N) count_marks++;

    for (int i = 0; i < count_marks; ++i)
        printf("%d ", marks[i]);
        
    return 0;
}