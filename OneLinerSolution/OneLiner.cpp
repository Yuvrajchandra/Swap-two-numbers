#include <iostream>

using namespace std;

int main()
{
    int num1 = 80, num2 = 50;
    cout << "Before Swapping: " << endl;
    cout << "num1 = " << num1 << ", num2 = " << num2 << endl;

    // One line solution to swap two numbers
    num1 = num1 ^ num2, num2 = num1 ^ num2, num1 = num1 ^ num2;

    cout << "After Swapping: " << endl;
    cout << "num1 = " << num1 << ", num2 = " << num2 << endl;

    return 0;
}
