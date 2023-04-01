#define WIN

#ifdef WIN
#include <iostream>
using namespace std;
#else
#include <stdio.h>
#endif

int main()
{
    int x = 5;
#ifdef WIN
    cout << x << endl;
#else
    printf("%d\n", x);
#endif
    return 0;
}