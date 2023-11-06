#include <iostream>

int main()
{
    float k =0.5f, b = -1.4f;
    int n = 100;
    float* y = new float[n];

    for(int x = 0; x < 100; ++x)
        y[x] = k * x + b;

    for(int i = 0; i < 10; ++i)
        printf("%.2f ", y[i]);

    delete[] y;
    return 0;
}