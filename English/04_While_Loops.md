# Loop structure (while)

Next you will learn to create programs where the same part of code is executed multiple times.
This is possible with loop structures. With a loop structure you can for example program something
to be done 20 times or alternatively to be repeated until the user enters an input to stop the
repetition.

Repetition is one the three basic principles of programming languages with sequence and selection.
Once you have mastered these three basic principles, you can write an algorithmic solution to
any computational problem.

Python language has two types of loops:
1. initial condition loop (while)
2. iterative loop (for)

In this module you will learn to use an initial condition loop.

## Repetition with initial condition

Let's assume that a latte in a café costs five euros and we want to pay with coins.
The following pseudo code shows the idea of a loop repetition with initial condition:
if we have not taken enough money from our pocket yet, we will continue to give more 
coins to the cashier, one coin at a time:

```monospace
as long as amount_paid < 5
	give coin
```

At some point the amount paid is enough and we can stop giving more coins.

With a repetitive structure we can repeat a block of code multiple times in our program.
The pseudo code example has an initial condition that is evaluated every time when entering
the loop. If the condition is true, the indented block is executed. Every time the indented
block has run, the initial condition is evaluated again. As long as the condition is still 
true, the block will be executed again. The repetition ends only when the initial condition
is false.

You can write a conditional loop in Python using a `while` statement:

```monospace
while (condition):
	block to be repeated
```

Similarly to `if` statements, a condition is a statement that has a truth value (Boolean) that can be
calculated. The condition is either true or false.

1. If the condition is true, the indented block (indented statements) will be executed.
2. If the condition is false, the indented block is not executed.

The only difference to an `if` statement is that the condition is evaluated again every time the
indented block has run. If the condition is still true, the indented block is run again. After
that the condition is checked again before each new round.

## Example 1: Fixed amount of repetitions

Let's write a program that asks the user how many times to greet. After that the program will 
print out the greetings:

```python
rounds = int(input("How many greetings: "))
finished_rounds = 0
while finished_rounds<rounds:
    print("Good morning")
    finished_rounds = finished_rounds + 1
```

User input defines how many times the greeting is repeated:

```monospace
How many greetings: 5
Good morning
Good morning
Good morning
Good morning
Good morning
```

This example has two variables:
1. `rounds`- the total amount of greetings. Once it has been read from the user, its value will remain constant throughout
the execution of the program.
2. `finished_rounds` - a loop variable that is initialized with value 0. At the end of each round the loop variable value
is increased by one.

Let's assume the user wants five greetings. The value 5 is saved to the `rounds` variable. When the `while` loop
is entered the first time, the `finished_rounds` variable has been initialized to 0. The condition in the while loop
is now 0<5 which is true. The execution proceeds inside the while loop. In the while loop the first greeting is printed
out and the value of `finished_rounds` increases from zero to one.

As we are using a while loop, the condition is now evaluated again. The condition is now 1<5 which is still true. Inside
the while loop the second greeting is printed out and the value of `finished_rounds` is increased once more. The new
value is 2.

The structure is looped through until after the greeting is printed out for the fifth time and the value of `finished_rounds`
increases to 5. After that the condition is tested again, but this time the condition is 5<5 which is false. The loop is
not repeated again and the execution of the program would continue from the next statement after the while loop. In our example
there are not statements after the while loop so the execution of the program ends.

## Example 2: User ends the repetition

In the next program the number of repetitions is not known when entering the loop structure.
The program asks the user to give text commands until the user enters a stop command:

```python
command = input("Enter command: ")
while command!="stop":
    print("Executing command: " + command)
    command = input("Enter command: ")
print("Execution stopped.")
```

The amount of repetitions depends on user input:

```monospace
Enter command: sing
Executing command: sing
Enter command: dance
Executing command: dance
Enter command: stop
Execution stopped.
```

## Example 3: Varying amount of repetitions

Next, we will look at a simulation example where the amount of repetitions is based on a random number generator.
The program rolls two dice until they result to a pair of sixes.

The number of required rolls varies between runs:

```python
import random
dice1 = dice2 = rolls = 0
while (dice1!=6 or dice2!=6):
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    rolls = rolls + 1
print(f"Rolled {rolls:d} times.")
```

```monospace
Rolled 17 times.
```

```monospace
Rolled 37 times.
```

The example uses the Python built-in `random` library. The library
must be imported with an import statement at the beginning of the program
before it can be used. You do not have to memorize how to use ready-made libraries
as you can always check the documentation for the correct use: [https://docs.python.org/]

## Nested loops

Loops can be placed one inside another so that the inner loop is executed on each round of the outer loop.

Let's print out the multiplication table from one to five. The table includes all twenty-five possible 
multiplications with numbers 1, 2, 3, 4 and 5:

```python
first = 1
while first <= 5:
    second = 1
    while second <= 5:
        print(f"{first} times {second} is {first*second:d}")
        second = second + 1
    first = first + 1
```

```monospace
1 times 1 is 1
1 times 2 is 2
1 times 3 is 3
1 times 4 is 4
1 times 5 is 5
2 times 1 is 2
2 times 2 is 4
...
5 times 3 is 15
5 times 4 is 20
5 times 5 is 25
```

Let's extend the dice rolling example so that the program prints out how many rounds on *average* is needed before
getting a pair of sixes.

To calculate the average, let's set the number of simulated rounds to a very large number, a hundred thousand:

```python
import random
rounds = 0
total_rolls = 0

while rounds < 100000:
    dice1 = dice2 = rolls = 0
    while (dice1!=6 or dice2!=6):
        dice1 = random.randint(1,6)
        dice2 = random.randint(1,6)
	rolls = rolls + 1
    #print(f"Rolled {rolls:d} times.")
    rounds = rounds + 1
    total_rolls = total_rolls + rolls

average_rolls = total_rolls/rounds
print(f"Average rolls required: {average_rolls:6.2f}")
```

A comment symbol (#) has been added to the front of the print statement for individual rolls so that the console
is not filled with 100,000 prints.

The output shows the average amount of rolls required per round. Although there are a large number of rounds, random
variation affects the outcome:

```monospace
Average rolls required:  35.86
```

We can see that the average of 36 rolls are required. This matches the result we would get by calculation.
We just created an empirical simulation where an approximation of a theoretical value is achieved by
imitating the phenomenon on a computer.

## Break

It is possible to exit a loop structure in Python using the `break` statement. If `break` is used, the
value of the condition is no longer calculated.

In the following example the command MAYDAY is used to break out of the loop entirely and immediately:

```python
command = input("Enter command: ")
while command!="stop":
    if command=="MAYDAY":
        break
    print("Executing command: " + command)
    command = input("Enter command: ")
print("Execution stopped.")
```

When the user has given the MAYDAY command, the condition of the while loop permits the start of a new round.
The `if` statement inside the while loop however causes the program to exit the loop instantly:

```monospace
Enter command: sing
Executing command: sing
Enter command: dance
Executing command: dance
Enter command: MAYDAY
Execution stopped.
```

You should be careful when using the break statement. Using break statements can lead to writing code that
is difficult to follow, so called spaghetti code. As a principle, loop conditions should always be built so
that break statements are not needed.

Writing programs that are easy to follow and clear in their logic is part of the expertise of a programmer. Thus,
using the break statement should be limited to situations where using it advances these objectives.

## While/else

In Python, an `else` branch can be added to a while structure so that if the condition of the loop is false, the else
branch will be executed. Therefore, the else branch is executed after a successful run of the loop. It is not executed
if a `break` statement is used to exit the loop.

Let's look at the following example:

```python
command = input("Enter command: ")
while command!="stop":
    if command=="MAYDAY":
        break
    print("Executing command: " + command)
    command = input("Enter command: ")
else:
    print("Goodbye.")
print("Execution stopped.")
```

The program outputs the Goodbye text once when the loop is exited normally after the condition is tested false:

```monospace
Enter command: dance
Executing command: dance
Enter command: stop
Goodbye.
Execution stopped.
```

If a break statement is used to exit the loop, the text is not printed out:

```monospace
Enter command: dance
Executing command: dance
Enter command: MAYDAY
Execution stopped.
```

However, this is a feature of the language that is quite rarely used.

## Infinite loop

Finally, we will look at the infinite loop, a programming error that all programmers cause every once in a while.
A program gets to an infinite loop when the condition of a loop never changes to false. This can occur
for example, if you forget to increase the value of a loop variable inside the loop.

The next faulty program causes an infinite loop to occur:

```python
# Faulty program, infinite loop

number = 1
while number<5:
    print(number)

# This part is never reached:
print("All ready.")
```

The execution never stops:
```monospace
1
1
1
...
```

A program that has entered an infinite loop must be stopped by force. In PyCharm IDE it is done by clicking
the stop button on the side of the console window:

![Stop button to stop executing the program](img/stop_button.png)

If the stop button does not stop the execution, check that the terminal emulation operations are enabled in
the console window: select **Run/Edit Configurations** and check the **Emulate Terminal in Output Console** checkbox.
