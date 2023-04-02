#include <iostream>

using namespace std;
int main()
{
    int summa = 0;
    int n = 1;

    while (summa < 100 && n != 0)
    {
        cout << "Введите целое число: ";
        cin >> n;

        summa += n;
    }

    cout << summa << endl;
    return 0;
}