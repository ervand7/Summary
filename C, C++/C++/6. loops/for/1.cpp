#include <iostream>

using namespace std;

int main()
{
    double s = 0;

    for (int n = 1; n <= 1000; ++n)
        s += 1.0 / n;

    cout << s << endl;
    return 0;
}
