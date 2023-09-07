# Functions

In this module you will learn to write functions in Python language. Functions are general-purpose parts of a program
that you can use multiple times.

Using functions helps you avoid situations where you would have to write and copy the same or a similar
block of code to various parts of your program. Reusing the same code should always be avoided in programming as
it makes programs more complex and more difficult to modify. If the reused code changes, the same change must be
applied to more than one place in your program. Writing these repetitive tasks into functions instead solves this problem.

Functions are subroutines that are called from other parts of the program when needed. Python offers two types of subroutines:
functions and methods. We will get back to methods when discussing object-oriented programming with Python later on this course.

## Structure of a function

A program that uses functions is divided into two parts:
- the main program or the part that resides outside the functions
- the functions

Functions can be called from the main program. Functions can also call other functions. Calling a function means that
the execution of the program moves to the function that has been called. Once the function has finished, the execution
will continue from the original location, the next statement after the function call.

Let's write our first function:
```python
def greet():
    print("Hello!")
    return
```

A function is defined using the reversed word `def` followed by the name of the function. In Python, functions
are named with descriptive names written in lowercase letters. If the name of the function has multiple words, the
words are separated with underscores. Following these rules, the same greeting function here could also be
called `greet_user` for example.

The curly brackets after the function name can be used to define parameters for the function. We will get back to these
later. If no parameters are used, empty pair of brackets is written after the function name as in the example above.

The brackets are followed by a colon. The statements that belong to the function body are written after the colon. The
statements inside the function body are run when the function is called.

The statements in the body of the function are written with one-step indentation.

Functions end with a `return` statement. The return statement can be used to return a return value if there is one.
The example function here does not have a return value, but we will learn about them later.

The same program can have multiple functions. The example above only shows one defined function.

## Calling a function

Once a function has been written, the program does not do anything with it yet. For the code inside the function body
to be executed, the function must first be called.

Let's extend our example program so that it has both the function as well as a main program part where the function is
called:

```python
def greet():
    print("Hello!")
    return

print("A new day starts with a greeting.")
greet()
print("Now we can move to other business.")
```

The program above now consists of the `greet` function and the main program after that.
Here the main program consists of two statements: a printing statement, a function call, and another printing statement.

The definition of a function must reside earlier (or higher) in the code than the line where it is called. Therefore,
the main program should be written last in the code file.

The execution of a program always starts at the beginning of the main program.

When the `greet` function is called, the execution moves to the body of the function and the main program waits for the
function call to finish. When the function is finished, the return statement returns the execution back to where the
function was called. 

The program produces the following output:

```monospace
A new day starts with a greeting.
Hello!
Now we can move to other business.
```

## Function parameters

The example function `greet` above always works the same way. It does not require
any initial information from the main program. Sometimes a function needs information 
with the function call for it to be able to execute itself properly.
These parts of information that are sent to a function are called parameters.
The values of the parameters are given with the function call. The values
are copied into parameter variables that are defined in the function definition.

Let's look at an example program:

```python
def greet(times):
    for i in range(times):
        print("Round " + str(i+1) + " of saying hello.")
    return

print("A new day starts with greetings.")
greet(5)
print("Let's greet some more.")
greet(2)
```

Ohjelma tuottaa seuraavan tulosteen:
```monospace
A new day starts with greetings.
Round 1 of saying hello.
Round 2 of saying hello.
Round 3 of saying hello.
Round 4 of saying hello.
Round 5 of saying hello.
Let's greet some more.
Round 1 of saying hello.
Round 2 of saying hello.
```

Above the `times` parameter is given a value from the main program. There are two calls: in the first
call value 5 is given and in the second one the value is 2.

The value sent has here been "hard coded", but it could also be stored in a variable an be defined only
at execution time. It could for example be asked from the user.

Parameter values that are passed on to the function are called arguments. Here each function call has one argument.

## Variable scope

In the earlier example the greeting was handled by using loop variable `i` that was defined inside the function.
These types of variables that are defined inside a function are called local variables. They cannot be seen outside
the function.

Variables defined outside functions are called global variables. The values of global variables are visible everywhere
inside the program, including functions.

If the value of a variable is changed inside a function, the variable is automatically interpreted as local.

To demonstrate this effect, let's look at the following example program:

```python
def change():
    city = "Vantaa"
    print("At the end of the function: " + city)
    return

city = "Helsinki"
print("At the beginning in the main program: " + city)
change()
print("At the end of the main program: " + city)
```

The program provides the following output:

```monospace
At the beginning in the main program: Helsinki
At the end of the function: Vantaa
At the end of the main program: Helsinki
```

So, what happened here? First two instances of the city variable were created:
1. A global variable, which was created in the main program
2. A local variable inside a function that shares the same name as the global variable. Changing the value of the local variable does not affect the value of the global variable.

It is important to understand the rules of variable scope, so that as a programmer you can use both global and local
variables effectively and pass values to functions the correct way.

## Multiple parameters

It is possible to pass multiple arguments to a function. When passing multiple arguments, they are separated by commas.
The argument values in the function call are assigned to the parameter variables in the order they are listed in the
function call.

Let's look at the following example program:

```python
def greet(greeting, times):
    for i in range(times):
        print(greeting + " round: " + str(i+1))
    return
```

The program provides the following output with different arguments:

```monospace
Hello round 1
Hello round 2
Hello round 3
Good day round 1
Good day round 2
```

Notice that we have made the greeting function more general-purpose: it can be used for greeting in many different
ways. This function parameterization (or replacing fixed defaults by parameters) make functions more powerful and
useful for even larger programs.

## Return value

Sometimes functions produce a value that needs to be returned to the part of the program that called the function.
This is possible through the return value mechanism.

The value generated by the function is returned using a return statement. The prior examples of functions have not
had return values. Let's look at how to add a return value to a function.

The following program calculates the sum of squares of two numbers. This can be calculated by multiplying both values
by themselves and then calculating the sum of the squares. It is important that the result calculated in the function 
is passed to the main program.

```python
def sum_of_squares(first, second):
    result = first**2 + second**2
    return result

number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))
result = sum_of_squares(number1, number2)
print(f"The sum of squares for numbers {number1:.3f} and {number2:.3f} is {result:.3f}.")
```

The output is as follows:

```monospace
Enter the first number: 2
Enter the second number: 3.2
The sum of squares for numbers 2.000 and 3.200 is 14.240.
```

Naturally, the return value has to be saved before it can be used.
Usually, the value is assigned to a variable right away in a function call
or used some other way.

## List as a parameter

A function can be given a list as a parameter. In the following example, the inventory function gets a list
as a parameter and then lists all the list elements:

```python
def inventory(items):
    print("You have the following items:")
    for item in items:
        print("- " + item)
    return

backpack = ["Water bottle", "Map", "Compass"]
inventory(backpack)
backpack.append("Swiss Army knife")
inventory(backpack)
```

The function is called twice. Each time the list of items in the backpack is printed out:
```monospace
You have the following items:
- Water bottle
- Map
- Compass
You have the following items:
- Water bottle
- Map
- Compass
- Swiss Army knife
```

Let's modify the program a bit. We will modify the subroutine so that it empties the list once it has been
printed out:

```python
def inventory(items):
    print("You have the following items:")
    for item in items:
        print("- " + item)
	# Items disappear during the invetory
    items.clear()
    return

backpack = ["Water bottle", "Map", "Compass"]
inventory(backpack)
backpack.append("Swiss Army knife")
inventory(backpack)
```

The output shows that the call to the invetory function empties the backpack:
```monospace
You have the following items:
- Water bottle
- Map
- Compass
You have the following items:
- Swiss Army knife
```

What happened here? When a list is given as a parameter, it is passed to the function differently
compared to basic type variables.

The value of a basic-type variable is copied from the argument in the function call to a parameter value.
In case of a list, the list contents are not copied. Only the memory address of the list is passed on
to the function. The memory address is where the list is stored in main memory.

In this case the memory address of the global backpack variable is stored as the value of the items variable.
Now both the backpack and items variables point to the same list in computer memory. The function changes
the contents of the list stored in the items variable with the list method clear that clears the list.
As there is only one shared list, the change also applies to the global backpack variable. Therefore,
changes to a list that has been received as a parameter also apply to the list that was used in the
function call.

## More characteristics of functions

Moreover, Python also have the following characteristics:
1. Argument lists of variable sizes.
2. Using keywords to pass parameters.

A programmer can pass the parameter values as key-value pairs. Parameters can also be given default values in the
function definition.

Furthermore, Python also support anonymous, or so-called lambda functions. In lambda functions only the formula
or rule to produce a return value is provided without writing an actual function. Lambda functions are introduced later.
