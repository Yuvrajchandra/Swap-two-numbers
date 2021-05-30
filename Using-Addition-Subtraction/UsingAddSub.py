# Python implementation to swap two
# numbers using arithmetic operators (+, -)

# Function to swap two numbers
# using arithmetic operators (+, -)
def swapNums(num1, num2):

    # Printing numbers before swapping
    print("Before Swapping:")
    print("num1: " , num1 , ", num2: " , num2)

    # Swapping with the help of
    # arithmetic operators (+, -)
    num1 = num1 + num2
    num2 = num1 - num2
    num1 = num1 - num2

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
