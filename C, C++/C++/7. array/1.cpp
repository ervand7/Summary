#include <iostream>
using namespace std;

int main()
{
    float y[100], k = 0.5, b = 2;

    for (int x = 0; x < 100; ++x)
    {
        y[x] = k * x + b;
        cout << y[x] << " ";
    }

    return 0;
}