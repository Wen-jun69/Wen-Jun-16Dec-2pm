# Create a file called day3.py and do all the following exercises in it.

# Task 1: input() Introduction

Write a program to 
1. Ask for your name
2. Ask for your title
3. Ask for your command

Example Output: [King] [Kenneth] commands the peasants to [work harder]!

-------------------------------------------------------------------------

# Task 2: Variable Types (string and integer)

Describe what is a **string**, and what is the syntax for a string?
Describe what is a **number**, and what is the syntax for a number?
convert a string to integer using **int()**
convert an integer to string using **str()**

1. Create a string variable called name, and assign a name
2. Create a integer variable num_pens and assign a number (for the number of pens you are buying)
3. Use String Concatenation and print() to print out the following output
4. Use the correct conversion function to convert everything to string

Sample Output: [Lionel] bought [20] pens

------------------------------------------------------------------------

# Task 3: Addition Calculator

Code a simple Calculator program that does addition. (If you finish addition, look at the bonus challenge)

1. Ask for a number input for 1, assign to a variable
2. Ask for a number input for 2, assign to a variable
3. Add the two numbers together.

Assume number1 is 10 and number2 is 20
Sample output: 10 + 20 = 30

## Bonus Challenge: Expand your calculator to do subtraction, multiplication and division
------------------------------------------------------------------------

# Task 4: NTUC Cashier - Variable Types (string and integer)

Imagine you are a NTUC Cashier and you are calculating how much must your customer pay

To make things easier, 
a. the customer will only buy 1 item (e.g. apples)
b. the customer will tell you how much of each item they are buying
c. you can decide how much is the price of each item

Your program will ask the customer:
1. How many units of the items they are buying
2. Calculate the total cost of the item

To Think: How many variables do you need? Where do you do your conversion? Where do you concatenate the sentences?

--------------------------------------------------------------------------

# Task 5: Booleans and if-else conditions

Write a program to check if the first number is bigger than the second number
1. Using **input()**, ask for a number and assign it to **number1**
2. Using **input()**, ask for a number and assign it to **number2**
3. Use the if-else condition to check if **number1** is bigger or not bigger than **number2**

---------------------------------------------------------------------------

# Task 6: Booleans and Password Program

Write a program to ask the user to enter a password.

If the password is correct, say "Access Granted"

Else, say "Access Denied"

-----------------------------------------------------------------------------

# Task 7: Generate Random()

use import random, and random.randint([from], [to]) to generate a random number.
Example:

import random
random_number = random.randint(1,10) # to generate a number between 1 to 10

Using a for loop, generate 10 random numbers and print them out

------------------------------------------------------------------------------

# Task 8: Math Quiz Program

Your math teacher has discovered you are a coding guru, 
and has asked you to code a addition quiz for the class

Using if-else, random, input(), type conversion

1. Use random to generate a random number and assign to num1
2. Use random to generate a random number and assign to num2
3. Use input() to ask the user "What is [num1] + [num2] ? "
   Example: **What is 6 + 9?**
4. Use if-else condition to check if the user enter the correct value