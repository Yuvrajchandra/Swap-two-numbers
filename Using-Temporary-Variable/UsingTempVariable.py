# Python implementation to swap two
# numbers using a temporary variable

# Function to swap two numbers
# using a temporary variable
def swapNums(num1, num2):

    # Printing numbers before swapping
    print("Before Swapping:")
    print("num1: " , num1 , ", num2: " , num2)

    # Swapping with the help of a
    # temporary variable "temp"
    temp = num1
    num1 = num2
    num2 = temp

    # Printing numbers after swapping
    print("After Swapping:")
    print("num1: " , num1 , ", num2: " , num2)


# Driver Code

# Test Case: 1
swapNums(80, 50)

# Test Case: 2
swapNums(2, 7)

# Test Case: 3
swapNums(3, 9)
