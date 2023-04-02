#include <iostream>
using namespace std;

int main()
{
    float x;
    cout << "Input a number: ";
    cin >> x;

    if (x < 0)
    {
        cout << "Input numner " << x << " is negative\n";
    }
    else if (x > 0)
    {
        cout << "Input numner " << x << " is positive\n";
    }
    else
    {
        cout << x << " is zero";
    }

    return 0;
}