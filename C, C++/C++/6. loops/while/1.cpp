#include <iostream>

using namespace std;
int main() 
{
    double s = 0;
    int n = 1;

    while (n < 1000) {
        s += 1.0 / n;
        n++;
    }

    cout << s << endl;
    return 0;
}