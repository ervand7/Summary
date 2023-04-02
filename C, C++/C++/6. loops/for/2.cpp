#include <iostream>

using namespace std;

int main()
{
    double a, b, c;
    cout << "Введите b и c: ";
    cin >> b >> c;

    for (double x = 0; x <= 1; x += 0.1)
    {
        a = b * x + c;
        cout << a << endl;
    }

    return 0;
}
