#include <iostream>

using namespace std;
int main()
{
    int n = 5, m = 7, s = 0;

    for (int i = 0; i < n; ++i)
        for (int j = 0; j < m; ++j)
            s += i * j;

    cout << s << endl;

    return 0;
}
