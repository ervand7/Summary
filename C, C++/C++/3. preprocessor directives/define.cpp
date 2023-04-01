#include <iostream>

// define нужен для объявления констант
#define TWO 2
#define FOUR TWO *TWO
#define PX cout << "X равно " << x << endl
#define SQUARE(X) X *X

using namespace std;
int main()
{
    setlocale(LC_ALL, "rus");
    int x = TWO;
    PX;
    x = FOUR;
    PX;
    x = SQUARE(3);
    PX;

    return 0;
}