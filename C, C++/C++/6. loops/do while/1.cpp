#include <iostream>

using namespace std;
int main()
{
    const int secret_code = 13;
    int code_ent;

    do
    {
        cout << "Input secret code: ";
        cin >> code_ent;
    } while (code_ent != secret_code);

    cout << "You entred correct code!";

    return 0;
}