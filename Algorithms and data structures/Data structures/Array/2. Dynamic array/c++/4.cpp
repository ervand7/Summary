#include <iostream>
#include <vector>

int main()
{
    std::vector<double> digits(10, -1.0);
    digits.reserve(20);
    digits.pop_back();

    std::cout << digits.size() << std::endl;
    std::cout << digits.capacity() << std::endl;

    for(int i = 0; i < digits.size(); ++i)
        std::cout << digits[i] << " ";

    return 0;
}