#include <iostream>

using namespace std;

int main()
{
    double a, b, c;
    cout << "Введите b и c: ";
    cin >> b >> c;

    double x = 0;
    for (;;)
    {
        if (x > 1)
            break;
        a = b * x + c;
        cout << a << endl;
        x += 0.1;
    }

    return 0;
}
