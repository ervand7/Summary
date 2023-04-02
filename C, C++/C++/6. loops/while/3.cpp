#include <iostream>

using namespace std;
int main()
{
    int summa = 0;
    int n = 1;

    while ((summa += ++n) < 50)

    {
        cout << summa << endl;
    }
    return 0;
}