# Conditional statement (if)

In this module you will learn to write programs that can divide into several alternative execution branches.
This way you can make your program react differently to different inputs. Branching may also be based on the
result of a mathematical operation or something else inside the state of your program.

Branching is done using a selection statement. Selection statements are essential control structures of a
programming language. Learning to use them greatly improves a developer's power of expression.

## Conditional statements

Let's assume that you enter a café to order a latte. The latte costs 5 euros and you want to pay in cash.
Now you must determine if you have enough money to buy the latte. This selection event can be expressed
using pseudo code:

```monospace
if money_in_pocket >=5
	buy latte
```

The pseudo code shows that the decision is made based on whether a condition is true. The condition in this
case is that there is at least 5 euros of money. The condition can be true or false: For example, if there were
7 euros the statement would be 7 >= 5 which is true. On the other hand, if there were only 4.85 euros in the pocket,
the condition would be 4.85 <= 5 which is false.

A conditional part of the program (buying the latte) if executed precisely when the condition is true.

In Python, a conditional part of a program is written with an `if` statement. The structure of the statement is
as follows:

```monospace
if(condition):
	conditionally executed block of code
```

In the example above, the condition is a logical expression that can be true or false. Based on the condition, 
the execution proceeds as follows:
1. If the condition is true, the conditional block of code is executed.
2. If the condition is false, the execution will jump to the next statement after the conditional structure.

The expressions inside the conditional block must be indented by one step. In Python, a one-step indentation 
is written by adding four spaces at the beginning of a line. In practice, it is more efficient to press the
Tab key once instead of writing four spaces. Indentation is important in Python: it expresses the internal
hierarchy of the program. In this example, the one-step indentation shows which lines of code are part of
the body of conditional block. In Python it is not only necessary to indent lines correctly but it also
makes the code clearer and more readable. In this sense Python is different from many other programming
languages where indenting is optional in terms of the syntax of the language.

## Conditionally executed program parts

Let's write the first example of a program that uses a conditional statement. The program asks the user
how much money they have in their pocket and lets them know if it is enough to buy the latte that costs 5
euros. If there is not enough money, there is no output: 

```python
money = float(input("Enter amount of money: "))
if money>=5:
    print("You can buy a latte.")
```
Let's try the program out with different inputs. The conditional block is executed when there is enough money:

```monospace
Enter amount of money: 5.45
You can buy a latte.
```

Now let's try a situation when there is just enough money:
```monospace
Enter amount of money: 5
You can buy a latte.
```

This was an important test as handling boundary cases easily leads to programming errors. If we had written the condition
as `money>5` by mistake, the latte would not have been bought due to incorrectly working program.

Finally, let's check that the conditional block is not executed when there is not enough money:
```monospace
Enter amount of money: 4.95
```

## Comparison operators

In the latte example above, the condition was expressed using the greater than or equal to comparison operator (`>=`).
You can use the following comparison operators to express conditions in Python:

| Notation | Comparison operator        | 
|----------|----------------------------|
| \>       | greater than               |
| \<       | less than                  |
| >=       | greater than or equal to   | 
| >=       | greater than or equal to   | 
| <=       | less than or equal to      | 
| ==       | equal to                   | 
| !=       | not equal to               | 

Logical operators can be chained. The following statement is true when a person's height is at least
170 but less than 180 cm: `170 <= height < 180`.

Operators can also be used with string type expressions. For example, for strings `m1` and `m2` statement
`m1 < m2` is true if `m1` comes earlier in the alphabetical order than `m2`.

The following example checks if two strings are equal:

```python
cat = input("Enter the name of the cat: ")
dog = input("Enter the name of the dog: ")

if cat==dog:
    print("Oh my! The cat and dog have the same name!")
```

Notice that the equality comparison uses two equal signs (`==`) as one is is used for assignment operations.

The program notifies if the cat and dog have the same name:

``` monospace
Enter the name of the cat: Bob
Enter the name of the dog: Bob
Oh my! The cat and dog have the same name!
```

## Logical operators

In earlier examples, the condition of a selection statement was presented in a simple way using comparison operators.
Sometimes the condition is more complex: it might for example consist of several individual conditions that all have
to be true for the condition to be true as a whole. These types of structural conditions can be built using logical
operators.

Python has the following logical operators:

| Notation | Logical operator                | 
|----------|---------------------------------|
| and      | "both"                          |
| or       | "either" or "both"              |
| not      | negation, "no"                  | 

Let's assume that `a` and `b` are logical statements and their values are either true or false.
In that case:
- statement `a and b` is true precisely if both statement `a` and statement `b` are true.
- statement `a or b` is true when at least one of statements `a` and `b` are true.
- statement `not a` is true precisely when statement `a` is false.

The order of precedence of the logical operators is as follows: the `not` operator is applied first, then the `and`
operator and lastly the `or` operator. The order can be altered using parentheses.

Examples:
- statement `a or b and c` is true when either `a` is true or both `b` and `c` are true.
- statement `(a or b) and c` is true when at least one of statements `a` and `b` are true and also statement `c` is true.
- statement `a and not b` is true when `a` is true and `b` is false.

Let's look at an example program that notifies if medicine can be given to a patient. The medicine can be administered
if the patient is an adult. Using the medicine is permitted also if the patient is at least 15 years old and their weight is
at least 55 kilograms. The following program first asks the age of the patient. If the age is at least 15 but less than 18 years,
the program also asks the weight. Finally, the program notifies the user if the medicine can be used.

```python
age = int(input("Enter age: "))
if 15 <= age < 18:
    weight = float(input("Enter weight (kg): "))
if (age >=18 or age>=15 and weight >=55):
    print("The medicine can be used.")
```
Let's try the program for a 17-year-old persons weighing 55 kilograms:
```monospace
Enter age: 17
Enter weight (kg): 55
The medicine can be used.
```

If you look at the second `if` statement, you might notice that weight is only specified for people
whose age is 15, 16 or 17. Others have not been asked for their weight and the variable is not defined.
However, Python has a feature that can be used here: calculating the value of a logical statement is stopped
immediately once its value has been determined. If the age is at least 18 years, the left side of the `or`
statement is true making the whole statement true. In that case the weight information is not needed to
calculate the value of the logical statement. If the age was less than 18 years, the right-side value will be
calculated. If the age is less than 15 years, both sides of the statement are false and the whole statement
is false. The weight information is only read if it is known that the age is at least 15 and less than 18
years, and in this specific case the weight variable is defined. This Python language feature is called
short-circuiting.

## Two mutually exclusive options

In the medicine administration example program has a weakness: if use of the medicine is not allowed, the program
does not print any output. The program would be more beneficial to the user if it always provided a result.

Let's modify the program by adding a conditional block that runs if the original condition was false. This can be
done by adding an `else` branch to the `if` statement.

This is how the `else` branch works:
```monospace
if (condition):
    block that is executed if the condition is true
else:
    block that is executed if the condition is false
```

Let's add an `else` branch to the medicine example:

```python
age = int(input("Enter age: "))
if 15 <= age < 18:
    weight = float(input("Enter weight (kg): "))
if (age >=18 or age>=15 and weight >=55):
    print("The medicine can be used.")
else:
    print("The medicine cannot be used.")
```

The `else` branch in the example is tied to the second `if` statement. In general, an `else` branch is interpreted
to relate to the last `if` statement that has been indented to the same level as the `else` branch in the program.

Let's look at the outputs produced by the program with different inputs:

```monospace
Enter age: 18
The medicine can be used.
```

```monospace
Enter age: 16
Enter weight (kg): 61
The medicine can be used.
```

```monospace
Enter age: 13
The medicine cannot be used.
```

```monospace
Enter age: 17
Enter weight (kg): 52
The medicine cannot be used.
```

## Multiple options

Lastly, let's look at a situation where there are multiple options that each have their own condition. This can
be done with `elif` branches. The word is short for "else if".

The following program asks the user's age and notifies them whether they are retired, working-age, in school or
a small child. (The age limits here are simplified and expect that a certain period in people's lives start at a
specific age, although that is not true in real life.)

```python
age = int(input("Enter your age: "))
if age>=65:
    print("You are retired.")
elif age>=18:
    print("You are working-age.")
elif age>=7:
    print("You are in school.")
else:
    print("You are a small child.")
```

Let's try the program by entering 23 years as the age:
```monospace
Enter your age: 23
You are working-age.
```

How does a structure with `elif` branches work? The execution proceeds as follows: 
1. First is is tested if the age is at least 65 years. If that is ture, the first conditional block will be executed
and the program will end.
2. If the first condition was false (age not 65 or more), it is checked if the age is at least 18 years. At this state
it is already known that the age is less than 65 years, so we do not need an upper limit for the age. If the condition
is true, the conditional block will be executed and the program ends.
3. If neither of the two first conditions were true, the age must be less than 18 years. The third branch checks whether
the age is at least 7 years, so practically 7-17 years. If the condition is true, the third conditional block is executed
and execution stops.
4. If the age was less than 7 years, the last conditional block in the `else` branch is executed.

If we look at the program, we can see that it was written so that the strict condition of the first branch is gradually
loosened by each branch, so we do not need upper limits for the age in the conditions. They can be written but it would
be unnecessary and create a new possibility for a programming error.
