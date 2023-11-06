#include <iostream>
#include <vector>

int main()
{
    std::vector<double> digits;
    digits.push_back(5.0);
    digits.push_back(4.0);
    digits.push_back(3.0);
    digits.push_back(2.0);

    digits[0] = 5.43;
    std::cout << digits[0] << std::endl;
    std::cout << digits.size() << std::endl;

    for(int i = 0; i < digits.size(); ++i)
        std::cout << digits[i] << " ";

    return 0;
}