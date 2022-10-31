# Inheritance

Inheritance is a mechanism in object-oriented programming where classes have a defined hierarchy: 
one class called base class can have more detailed subclasses (derived classes).

In this module you will learn to use inheritance when writing object-based Python programs.

## Base class and subclass

Let's look at the following situation where a program processes Employee objects:

```python
class Employee:

    total_employees = 0

    def __init__(self, first_name, last_name):
        Employee.total_employees = Employee.total_employees + 1
        self.employee_number = Employee.total_employees
        self.first_name = first_name
        self.last_name = last_name

    def print_information(self):
        print(f"{self.employee_number}: {self.first_name} {self.last_name}")

employees = []
employees.append(Employee("Viivi", "Virta"))
employees.append(Employee("Ahmed", "Habib"))

for e in employees:
    e.print_information()
```

The program creates two employees: Viivi and Ahmed, adds them to the employee list and prints out the contents
of the list:

``` monospace
1: Viivi Virta
2: Ahmed Habib
```

Each employee has three properties: employee number, first name and last name. Each employee gets an employee number 
automatically and it is based on the total amount of employees. The total amount of employees here is a
class variable: its value is not defined separately for each instance of the Employee class but instead only once
for the entire Employee class. Notice that a class variable is defined outside the initializer and when referenced
the `self` expression is replaced by the name of the class.

Let's assume that we face a need for improvement: some employees are hourly employees while others have a monthly salary. 
How should the salary information be added to the properties list in the Employee class?

One solution would be to add two separate properties: hourly pay and monthly pay. The solution would, however, be imprecise 
and when using the software, we would always have to check the field values to see which employee type is in question. 
Moreover, nothing would technically prevent us from defining both and hourly as well as a monthly pay for the same employee. 

Let's solve this by using the inheritance mechanism of Python.
Let's write two subclasses for the Employee class to clarify things: HourlyPaid and MonthlyPaid. When we create a new object,
we could make it for example an instance of the HourlyPaid subclass. Then it would have all the properties and methods inherited 
from the Employee base class (such as first name and the method work) but also the hourly pay property only defined for hourly
paid staff inside the subclass.

The extended program looks as follows:

```python
class Employee:

    total_employees = 0

    def __init__(self, first_name, last_name):
        Employee.total_employees = Employee.total_employees + 1
        self.employee_number = Employee.total_employees
        self.first_name = first_name
        self.last_name = last_name

    def print_information(self):
        print(f"{self.employee_number}: {self.first_name} {self.last_name}")

class HourlyPaid(Employee):

    def __init__(self, first_name, last_name, hourly_pay):
        self.hourly_pay = hourly_pay
        super().__init__(first_name, last_name)

    def print_information(self):
        super().print_information()
        print(f"Hourly pay: {self.hourly_pay}")

class MonthlyPaid(Employee):

    def __init__(self, first_name, last_name, monthly_pay):
        self.monthly_pay = monthly_pay
        super().__init__(first_name, last_name)

    def print_information(self):
        super().print_information()
        print(f"Monthly pay: {self.monthly_pay}")


employees = []
employees.append(HourlyPaid("Viivi", "Virta", 12.35))
employees.append(MonthlyPaid("Ahmed", "Habib", 2750))
employees.append(Employee("Pekka", "Puro"))
employees.append(HourlyPaid("Olga", "Glebova", 14.92))

for e in employees:
    e.print_information()

```

The example has four employees: two with hourly pay, one with monthly pay and one employee (Pekka) without a defined
contract type.

The program provides the following output:
```monospace
1: Viivi Virta
 Hourly pay: 12.35
2: Ahmed Habib
 Montly pay: 2750
3: Pekka Puro
4: Olga Glebova
 Hourly pay: 14.92
```

A base class - subclass relationship in Python is expressed by adding the name of the base class enclosed in brackets
to the `class` statement that defines the subclass. Thus, the beginning of statement the `class HourlyPaid(Employee)` 
determines that the HourlyPaid class becomes a subclass of the Employee class.

If needed, a subclass can have its own initializer. When an instance of the subclass is created, only the initializer
of the subclass is executed. In practice, usually this is done the same way as in out example: The program calls the
initializer of the subclass which then calls the initializer of the base class. In this case the initializer of the
subclass assigns the value for hourly pay whereas the first and last name are defined in the base class. Their values
are passed to the base class by calling the base class initializer, or `__init__` method. The base class of an object
can be accessed with the super() function: statement `super().__init__(first_name, last_name)` calls the initializer
of the base class that receives the first and last name as parameters.

Properties defined in the base class are automatically visible in the subclass. Thus, we can create an instance of the 
`HourlyPaid` class and fetch their name anytime with the expression `e.first_name`.

## Overriding methods

When we look at the example above, we notice that the `Employee` base class has a `print_information` method that
prints out the first and last name of the employee. The method works well when a person has been created as an 
instance of the `Employee` class regardless of their contract type. On the other hand, for printing the information
of hourly paid employees for example the method is too concise: it prints out the name information but cannot access
the hourly pay defined in the subclass.

The problem can be solved by overriding the `print_information` method. Overriding means that another implementation
of a method that exists in the base class is written into the subclass. The overridden method in the subclass overrides
the method defined in the base class. Therefore, when we write `e.print_information()` for an object of the `HourlyPaid`
class, it automatically calls the version of the method defined in the `HourlyPaid` class. If the same method call
is written for an object from the `Employee` class, the version of the same method in the base class is called.

Overriding a method makes our program more flexible: we can have diverse types of employees with different
data structures. Nevertheless, the information of all employees can be printed out in the main program with a simple
loop structure:

```
for e in employees:
    e.print_information()
```

Variants of the called method and technical details of the implementation are hidden where they belong: the implementing classes.
They are not visible to the main program.

## Multiple inheritance

Sometimes there are situations where a single class needs to be defined as a subclass of two or even more base classes.
This feature is called multiple inheritance. In contrary to some other programming languages, Python allows multiple inheritance.

The following example illustrates multiple inheritance. We define two classes: `Vehicle` and `SportsItem`. A third class `Bicycle`
can be made a subclass of both of the classes:

```python
class Vehicle:
    def __init__(self, speed):
        self.speed = speed

class SportsItem:
    def __init__(self, weight):
        self.weight = weight

class Bicycle(Vehicle, SportsItem):
    def __init__(self, speed, weight, gears):
        Vehicle.__init__(self, speed)
        SportsItem.__init__(self, weight)
        
        self.gears = gears

b = Bicycle(45, 18.7, 3)
print (b.gears)
print (b.speed)
print (b.weight)
```

We create a Bicycle object and print out the number of gears, speed and weight. The number of gears is defined in the `Bicycle` class.
The class inherits speed ifrom the `Vehicle` class and weight from the `SportsItem` class. The program produces the following output:

```monospace
3
45
18.7
```

In this case we cannot reference the initializers of both base classes from the initializer of the `Bicycle` class using `super`:

```python
# Incorrect initializer calls
super.__init__(speed)
super.__init__(weight)
```

The base class that the `super` function refers to is determined by the Python Method Resolution Order (MRO). In this case both
statements would call the initializer in the `Vehicle` class and the program would not work correctly.

We can call the initializers of both base classes using an alternative notation where the base class is specified by its name:

```python
Vehicle.__init__(self, speed)
SportsItem.__init__(self, weight)
```
