// C++ implementation to swap two
// numbers using a temporary variable
#include <iostream>

using namespace std;

// Function to swap two numbers
// using a temporary variable
void swapNums(int num1, int num2)
{
    // Printing numbers before swapping
    cout << "Before Swapping: " << endl;
    cout << "num1 = " << num1 << ", num2 = " << num2 << endl;

    // Swapping with the help of a
    // temporary variable "temp"
    int temp = num1;
    num1 = num2;
    num2 = temp;

    // Printing numbers after swapping
    cout << "After Swapping: " << endl;
    cout << "num1 = " << num1 << ", num2 = " << num2 << endl;
}

// Driver Code
int main()
{
    // Test Case: 1
    swapNums(80, 50);

    // Test Case: 2
    swapNums(2, 7);

    // Test Case: 3
    swapNums(3, 9);

    return 0;
}
