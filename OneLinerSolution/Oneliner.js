<script>
    let num1 = 80, num2 = 50;

    document.write("Before Swapping: <br>");
    document.write("num1: " + num1 + ", num2: " + num2 + "<br>");

    // One line solution to swap two numbers
    (num1 ^= num2), (num2 ^= num1), (num1 ^= num2);

    document.write("After Swapping: <br>");
    document.write("num1: " + num1 + ", num2: " + num2 + "<br>");
</script>
