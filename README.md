# Recursion and Conditionals

## Objective:
By the end of this lab, you will:
- Understand and implement Python conditionals for validating input.
- Use recursion to solve problems related to number conversion.
- Gain hands-on practice with Python conditionals and recursion.

## Part 1: Conditional Validation of IP Addresses

**Task 1: Validating IP Address Parts**

Write a function `is_valid_part(part)` that takes a string as input and checks if the string represents a valid part of an IP address. Each part should:
- Be a number between 0 and 255 (inclusive).
- Not contain leading zeroes (e.g., "01" is invalid, but "1" is valid).

*Incremental Development:*
1. Write code to check if the input can be converted to an integer.
2. Ensure the integer is between 0 and 255.
3. Verify that it doesn’t start with a leading zero unless the number is exactly "0".
    * HINT: This is NEW, but you can access the *characters* in a *string* with an index. Example: 'Hello'[0] evaluates to 'H', 'Hello'[1] evaluates to 'e', and 'Hello'[-1] evaluates to 'o' as its reverse!
    * You should only need to check index of 0 (i.e. [0]) if you also use the `len()` function, however.
4. Example test cases
```python
print(is_valid_part("255"))  # True
print(is_valid_part("256"))  # False
print(is_valid_part("01"))   # False
print(is_valid_part("0"))    # True
```

**Task 2: Validating the Full IP Address**

Using `is_valid_part`, write a function `is_valid_ip(ip)` that validates an entire IP address. The IP address will be passed as a string, and each part will be separated by dots (e.g., "192.168.1.1"). Return `True` if the IP is valid, otherwise `False`.

*Incremental Development:*
1. Split the input string by periods.
    * HINT: use the `split('.')` function!
    * split will return a *list* which we haven't covered yet, but you don't need to know that to complete this problem, just treat it like any other `str` type variable (i.e. len() of a list will return its length).
2. Ensure there are exactly four parts.
    * HINT: `len()` again!
3. Use `is_valid_part` to check each part.
    * HINT: Just like we use *loops* to loop over a `range()` you can loop over a list (i.e. for p in list:)
4. Example test cases
```python
print(is_valid_ip("192.168.1.1"))  # True
print(is_valid_ip("192.168.256.1"))  # False
print(is_valid_ip("192.168.1"))  # False
print(is_valid_ip("192.168.01.1"))  # False
```
## Part 2: Recursion and Number Conversion

**Task 1: Convert Decimal to Binary (Recursion)**

Write a recursive function `decimal_to_binary(n)` that takes a positive integer `n` and returns its binary representation as a string. 

*Incremental Development:*
1. Base case: If `n` is 0, return "0".
2. Recursive case: Use integer division and modulus to find the binary representation.
    * HINT: To convert 10 to binary you divide by 2, store the remainder as part of your answer, and use the quotient in the next division:
```shell
10 / 2 -> 0
5  / 2 -> 1
2  / 2 -> 0
1  / 2 -> 1
RESULT: 1010
```
3. Example test cases
```python
# Test cases
print(decimal_to_binary(10))   # "1010"
print(decimal_to_binary(255))  # "11111111"
print(decimal_to_binary(1))    # "1"
```

**Task 2: Convert Binary to Decimal (Recursion)**

Write a recursive function `binary_to_decimal(b)` that takes a binary string `b` and returns its decimal equivalent. 

*Incremental Development:*
1. Base case: If the string is empty, return 0.
2. Recursive case: Convert the leftmost bit and add its value to the result of the remaining bits.
    * HINT: Remember you can access the *characters* of a string with [i], where i is a number from 0 to the len('str') - 1!
    * 'Hello'[0] is 'H', etc.
3. To convert from a binary number to a decimal note the following:
```shell
1010 base 2 is 10 base 10, but how do we get there?
````
* NOTE binary has place values for numbers just like base 10
```shell
1    0    1    0
2^3  2^2  2^1  2^0
```
* SO if we multiply and add the *place value* by the *place* we get our decimal equivalent
```shell
1    0    1    0
2^3  2^2  2^1  2^0
------------------
8 +  0 +  2 +  0  = 10
```
4. Example test cases for a working function.
```python
print(binary_to_decimal("1010"))      # 10
print(binary_to_decimal("11111111"))  # 255
print(binary_to_decimal("1"))         # 1
```

## Part 3: (BONUS+10pts) Combining Recursion and Conditionals (Optional)

**Task 1: IP Address and Binary Conversion**

Using your knowledge of recursion and conditionals, write a function `ip_to_binary(ip)` that converts each part of a valid IP address to its binary representation.

*Incremental Development:*
1. Ensure the IP address is valid using `is_valid_ip`.
2. Convert each part to binary using `decimal_to_binary`.
    * HINT: use the `split('.')` again!
3. Return the full binary representation of the IP address.
4. Example test cases:
```python
print(ip_to_binary("192.168.1.1"))  # "11000000.10101000.00000001.00000001"
print(ip_to_binary("255.255.255.0"))  # "11111111.11111111.11111111.00000000"
print(ip_to_binary("256.1.1.1"))  # "Invalid IP address"
```

**Task 2: Bonus-Bonus (BONUS+5pt) Exercise (Extra Optional):**  
Extend the `ip_to_binary` function so that it accepts both valid IP addresses and binary representations of IP addresses without ANY guidance! In other words, you should have an `ip_to_binary`, but also a `binary_to_ip`, and a generalized `ip_convert` function that can:
1. Determine the type of IP passed in
2. Convert the IP type appropriately.
3. You have to come up with the HINTS!!!

## Part 4: Turn In!
[Review video of this process](https://redwoods.us-west-2.instructuremedia.com/embed/72299bfd-8420-4ad0-8af5-18fb8e32e50a)
1. **Create a GitHub Repository:**
   * Log in to your GitHub account.
   * Create a new repository with a suitable name (e.g., "python_lab5").
2. **Configure Git in PyCharm:**
   * Open the "Git" menu in PyCharm and initialize a Git repository for your project.
   * Add your GitHub remote repository by going to "Git" -> "Manage Remotes".
3. **Commit Changes:**
   * Stage all changes in your PyCharm project.
   * Commit the changes with a descriptive message (e.g., "Initial commit").
4. **Push to GitHub:**
   * Push the committed changes to your GitHub repository using the "Push" button in PyCharm.

### Submission
Submit the link from your GitHub repository containing your lab 5 repo to Canvas.