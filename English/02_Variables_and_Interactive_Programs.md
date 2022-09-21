# Variables and interactive programs

In this module you will learn to write interactive Python programs.

An interactive program communicates with the use: it reads and processes input and generates output accordingly.

An example of an interactive program would be a program that asks the user to enter two numbers, calculates their sum
and shows the sum to the user. In this case the input is read from the user (for example numbers 2 and 3), the input
is processed by calculating the sum and the output is shown to the user (sum of the numbers is 5).

## Printing

Let's start with Python's printing function called print. The following program prints out the text "Hello, world!":

```python
print('Hello, world!')
```

The printing is handled with a Python built-in function called print. The argument to the function is called inside
brackets. In this case the message to print is a string literal "Hello, world!". A string literal is a string that
is written directly into the program code. A string literal is written inside apostrophes ' ' or quotation marks " ".
The same program could also be written as shown here:

```python
print("Hello, world!")
```

What if you need to print out a message that includes apostrophes or quotation marks? The solution is to write the
symbol inside a string literal using the other alternative symbol to enclose the string literal:

```python
print('"Hello", said Joe')
```

When a program has multiple print statements, a line break is printed after each of them automatically:

```python
print("Good")
print("morning")
```

Output:
```monospace
Good
morning
```

The above program shows one of the basic structures of programming: sequences. By default, statements are executed
in the order they have been written in the program code. Other basic structures are selections and loops. They will
be introduced later.

You can also print a message with line breaks with a single line of code: It is possible to write a line break symbol
\n inside a string literal. You can get the same output as before by writing:

```python
print("Good\nmorning")
```

## Inputs, variables, and assignment statements

You have now learned how to create simple programs that generate the same output on each run. However, usually
it is required that a program reads inputs from the users and uses the input to execute tasks.

Let's write a program the asks the user for their name and then greets the user with their name.
This can be done as follows:

```python
user = input('Enter your name: ')
print("Nice to meet you, " + user + "!")
```

The user input is read using the built-in input function. The function receives the text to be printed on the screen
as an argument. The text should tell the user what information they are expected to enter.

The built-in input function waits for input from the user's keyboard. The user ends the input with the Enter key.
When the input has been give, the value of the input function is the string entered by the user.

The string must be saved into a *variable* so that it can be used later in the program. Here we are using a variable called
*user*. User input is saved into the memory of the computer and can be fetched from memory using the name of the variable.
The name of a variable is a sort of a handle or name tag that can be used to retrieve the value from memory.

A variable can be given a value using an assignment statement. The assignment statement uses an equals symbol (=).
The name of the variable is on the left side and the expression that determines the value to be assigned to the variable
is written on the right side.

Let's look at the printing statement more closely:

If we only wanted to print out the name the user entered as input, we could replace the bottom row with the following:

```python
print(user)
```

Notice that *user* is the name of the variable. As it is not a string literal, the name is not surrounded by quotes.

However, we want the program to output a whole greeting message, not just the name.
The string to output can be composed of several substrings by joining them together with a plus sign (+).
the lower row of the original program creates the output with three parts:

1. String literal "Nice to meet, "
2. The value of the *user* variable
3. String literal "!"

The program works as follows:
```monospace
Enter your name: Joanne
Nice to meet you, Joanne!
```

## Variable type

Above we assigned the string entered by the user to a variable.

In Python, variables and their type do not have to be declared in advance. The type of a variable
is determined automatically in the assignment statement. Variable type is the type of data a variable
refers to: is the value for example a string or a number?

Python has six basic types of variables:
- string
- number, that can either be integer, long, float or complex
- boolean, that is either True or False
- list
- tuple
- dictionary

Moreover, the type of a variable can be a reference to an object. A string type variable was discussed above.
Lists, tuples, dictionaries and object referencing will be introduced later on the course. Next we will look
at number data types.

The number data type in Python has four sub-types: integer (e.g. 4), long (e.g. 12756413000), float (e.g. 7.28 or 4.0) and
complex (e.g. 3-2i). Next we will create four variables. The first one will be assigned with an integer, the second with a
long integer, the third with a floating point number and the fourth with a complex number. Then we will print out the values
of all four variables and the values of both the real and imaginary parts of the complex number:

```python
first = -9
second = 12_456_123_180
third = 4.973
fourth = -4 + 2j

print(first)
print(second)
print(third)
print(fourth)
print(fourth.real)
print(fourth.imag)
```

When entering an integer or long, the digits can be grouped with an underscore as was done with the *second* variable
above. However, this is not mandatory.

The difference between an integer and long is that the value range of long is wider. It can be used to store integers
that are very large or small. A regular integer can store values between -2147483648 and 2147483647 including the end
points. A long requires more space in memory than a regular integer.

Notice that the imaginary part of a complex number in Python is marked with symbol j and not i as usually in mathematics.

The example program produces the following output:
```monospace
-9
12456123180
4.973
(-4+2j)
-4.0
2.0
```

## Mathematical operations and type conversion

Variables and constants can be used in mathematical operations. The order of the operations can be defined
with brackets if needed.

The arithmetic operations are addition (`+`), subtraction (`-`), multiplication (`*`) and division (`+`). In addition, there is the modulo operator (`%`) for the remainder, as well as the floor division operator (`//`) and the exponential operator (`**`).

The program below asks for a temperature in Fahrenheit and converts it to Celsius. The conversion is done by
subtracting 32 from the Fahrenheit degrees and multiplying the difference with a constant 5/9.


```python
fahrenheit_str = input("Enter a temperature in Fahrenheit: ")
fahrenheit = float(fahrenheit_str)
celsius = (fahrenheit-32)*5/9
print("The temperature in Celsius: " + str(celsius))
```

The program works as follows:
```monospace
Enter a temperature in Fahrenheit: 102
The temperature in Celsius: 38.888888888888886
```

Notice that the value returned by the input function is always interpreted as a string even if
it contains numbers only. A string can be converted into a float with the *float* funcion or into an integer
with the *int* function.

Furthermore, a number can be converted into a string with the *str* function. In the example program the conversion
must be done to add the calculated Celsius degrees to the output string. Both parts of the print must be strings.

## Output formatting

Sometimes it is required to modify the format of the output: how many decimals of a float are shown or for example
how many character spaces are reserved for a string. 

This can be done by using a formatted string literal, where the string to be printed includes format codes.

Let's look at this through an example. We will modify the output of the last example program so that the Celsius 
degrees are always shown with two decimals.

```python
print(f"The temperature in Celsius: {celsius:6.2f}")
```

Notice that the argument of the print function call now starts with letter `f` that shows that the string to print
includes formatting. Without the letter f the string literal would be printed out as it is in the program code,
including the curly brackets.

The string and the format code are enclosed in curly brackets. The expression to be formatted in the example is the
float value stored in the `celsius` variable.

In this case the format code is `6.2f`. The letter `f` determines that the expression is printed out as a floating
point number. The `6.2` notation defines the output to be printed out in a field that is 6 characters long and with
the accuracy of two decimals.

The following list shows examples of format codes:
- .5f : a float with the accuracy of 5 decimals
- 10.2f : a float with two decimals into a field of 10 characters wide
- <20s : a string printed into a field of 20 characters wide, justified to the left
- 8d : an integer into a field of 8 characters wide

Writing format codes is optional. However, using formatted string literals make combining numeric and string type
prints as `str` functions and other types of conversion functions are not necessarily needed. Above we could simply
print out the Celsius degrees without format code:

```python
print(f"The temperature in Celsius: {celsius}")
```

The same formatted string literal can include multiple expressions to format and their possible format codes. The
following program ouputs the value of two natural constants: pi and Euler's number (e) so that the name of each
constant is printed in a field of 12 characters and their corresponding values are printed in a field of 10
characters using 5 decimals:

```python
print(f"{'Pi':12s}:{math.pi:10.5f}")
print(f"{'e':12s}:{math.e:10.5f}")
```

Above, the natural constants pi and e where printed out using Python's math library. They were referred to with
expressions `math.pi` and `math.e`.

Lastly, Python offers multiple ways of formatting outputs. Formatted string literals introduces here are quite a
new way of formatting that has been available since Python version 3.6. It is enough to learn one good way of
formatting output, but you might see alternative methods in online learning materials and when looking at 
program code made by others. These alternative methods are:
1. using the `str.format()` function
2. using format specifiers and a list of expressions (% operator notation)
3. using template strings

The alternative methods listed above are not introduced here. You can find more information in the Python 3 documentation:
[https://docs.python.org/3/tutorial/inputoutput.html]
