#include <iostream>
#define N 10

using namespace std;

int main()
{
    short E[N][N];
    for (int i = 0; i < N; ++i)
    {
        for (int j = 0; j < N; ++j)
        {
            i == j ? E[i][j] = 1 : E[i][j] = 0;
            cout << E[i][j] << " ";
        }
        cout << endl;
    }

    return 0;
}