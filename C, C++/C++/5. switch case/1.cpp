#include <iostream>
using namespace std;

int main()
{
    int item;
    scanf("%d", &item);
    switch (item)
    {
    case 1946 ... 1964:
        cout << "Привет, бумер!";
        break;
    case 1965 ... 1980:
        cout << "Привет, представитель X!";
        break;
    case 1981 ... 1996:
        cout << "Привет, миллениал!";
        break;
    case 1997 ... 2012:
        cout << "Привет, зумер!";
        break;
    case 2013 ... 2100:
        cout << "Привет, альфа!";
        break;
    default:
        cout << "Unknown";
        break;
    }

    return 0;
}
