# Python ZeroDivisionError Bug

This repository demonstrates a common Python error: `ZeroDivisionError`. The `calculate_average` function is designed to compute the average of a list of numbers.  However, it fails when provided an empty list. This bug is addressed by adding a check for an empty list before calculating the average, ensuring that the function handles such cases gracefully.

**Bug:**
The original code lacks error handling for an empty input list, resulting in a `ZeroDivisionError`.

**Solution:**
The solution implements a check for an empty list before calculating the average, using a conditional statement to return 0 if the list is empty.