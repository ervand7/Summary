#include <iostream>

using namespace std;

int main()
{
    float x, s = 0;
    int n = 0;

    do
    {
        cout << "Input a number: ";
        cin >> x;

        if (x < 0)
            continue;

        n++;
        s += x;
        cout << "Current sum: " << s << endl;
    } while (n < 5);

    return 0;
}
