<script>
// JavaScript implementation to swap two
// numbers using arithmetic operators (+, -)

// Function to swap two numbers
// using arithmetic operators (+, -)
function swapNums(num1, num2) {

    // Printing numbers before swapping
    document.write("Before Swapping: <br>")
    document.write("num1: " + num1 + ", num2: " + num2 + "<br>")

    // Swapping with the help of
    // using arithmetic operators (+, -)
    num1 = num1 + num2
    num2 = num1 - num2
    num1 = num1 - num2

    // Printing numbers after swapping
    document.write("After Swapping: <br>")
    document.write("num1: " + num1 + ", num2: " + num2 + "<br>")
}

// Driver Code

// Test Case: 1
swapNums(80, 50);

// Test Case: 2
swapNums(2, 7);

// Test Case: 3
swapNums(3, 9);

</script>
