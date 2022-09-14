# Class, object, initializer

In this module you will learn the fundamentals of object-oriented programming. You will learn how to write classes
that determine common properties and operations to instances, or objects, of the class. You will learn the
principles of creating, initializing and using objects.

## Classes and objects

In object-oriented programming, a class is a general concept that determines common and shared properties
for the members of the class.

For example, **dog** can be such a general concept. Each dog has a group of properties such as name and
birth year. Dogs also have activities (or in Python, methods) such as barking.

Now we can write the simplest possible Dog class as follows:

```python
class Dog:
    pass
```

The `pass` statement above is an empty statement that does not do anything. It is needed as a placeholder as the body of
a class definition must contain at least one statement. 

This class definition only tells that there is a class called Dog. So far it does not specify any properties or methods
of dogs.

We can use the Dog class to create a Dog object. Objects are runtime instances or realizations of a class. Here is how
we create a Dog object called Bubbles that was born in 2022:

```python
class Dog:
    pass
   
dog = Dog()
dog.name = "Bubbles"
dog.birth_year = 2022

print (f"{dog.name:s} was born in {dog.birth_year:d}." )
```

The first statement in the main program creates a Dog object that is referenced by the variable `dog`. The dog is given
the name Bubbles and birth year of 2022. These are properties of the object we created and specific to that exact object.
We could create multiple dogs each with their own name and year of birth. We could also specify a breed for some of the dogs
and a nickname for others. Therefore, the properties of objects can vary from each other.

As we see in the example, the properties of an object can be referenced by first writing the name of the object, then
a period and lastly the name of the property. An example of such reference would be `dog.name`.

The last statement of the example program outputs the name and birth year of the dog object created in the main program:
```monospace
Bubbles was born in 2022.
```

Notice that class names in Python are written write uppercase initials. If the name of a class consists of multiple words,
the words are written together without underscores so that each word starts with an uppercase letter. This naming style
is called *CamelCase*. An example of this type of a name would be `ScreenRectangle`.

## Initializer

In the example above the Dog object was created so that first an object was created with no properties and then the
properties were assigned one by one. This way of creating objects is quite tiresome for the programmer.

To make creating object easier, an initializer, or constructor, is written inside the class. The constructor automatically
sets the required values to the properties of the new object. The following example shows a class constructor that sets
the values of name and birth year automatically. The constructor is used in the main program to create an object.

```python
class Dog:
    def __init__(self, name, birth_year):
        self.name = name
        self.birth_year = birth_year

dog = Dog("Bubbles", 2022)

print (f"{dog.name:s} was born in {dog.birth_year:d}." )
```

A Python initializer is defined inside a class by writing a function with the name `__init__`. The first parameter of the
function is always `self`. After this other parameters to the initializer are given. In this case they are name and birth year.
A function defined this way is interpreted automatically as the initializer when the program is run and it is executed every
time a new object is created. There is no return statement at the end of an initializer.

Inside the initializer in the example there are two assignment statements were values are given to the properties of the new
object. The properties of the new object are referenced by the reserved word `self` which is followed by a period and the name
of the property. Typically, the parameters of the initializer are used to assign values to the properties of the new object.
For example, the statement `self.name = name` assigs the value of the name parameter to the value of the name property.

Notice that when a new object is created, the first parameter of the initializer, `self`, is not written. So, not this way:  
```python
# Incorrect instantiation statement
dog = Dog(self, "Nuggets", 2022)
```
but this way instead:
```python
dog = Dog("Nuggets", 2022)
```

## Methods

You have already learnt how object properties are defined. Usually you would want to also specify actions, or methods, to
your objects. Let's write a bark method to our Dog class. The method can be called to instances, or objects, of the class.
The program in the following example creates two Dog objects and makes the two dogs bark in their specific barking sound:

```python
class Dog:
    def __init__(self, name, birth_year, sound="Woof woof"):
        self.name = name
        self.birth_year = birth_year
        self.sound = sound

    def bark(self, times):
        for i in range(times):
            print(self.sound)
        return


dog1 = Dog("Rascal", 2018)
dog2 = Dog("Boi", 2022, "Yip yip yip")

dog1.bark(2)
dog2.bark(5)
```

Now the initializer has three parameters. The last parameter (`sound`) has been given a default value that is assigned
if the parameter is not given when a dog object is created. In this example, Rascal gets the default barking sound.

The `bark` method the was written inside the class can be called to any existing instance of the Dog class. The first parameter
of a method is always `self`. This is followed by other parameters that are given values when the method is called.

A method is called by writing the name of an object followed by a period and the name of the method followed by curly brackets
and possible parameters. For example the statement `dog1.bark(2)` calls the bark method for the dog1 object. The times to bark
is passed as a parameter in the method call (2). Inside a method the properties of and object can be referred to by writing `self`
followed by a period and then the name of the property. For example, the expression `self.sound` refers to the value of the
`sound` property specific to each object.

## Class methods or static methods

In the previous example the properties of a dog were name, birth year and barking sound. The properties are of course specific to each object,
meaning that different dogs can have different names.

Sometimes there is a need to store some information that applies to the entire class instead of a single object. In the `Dog` class in the example
this type of a property could for example be the total amount of dogs instantiated from the class. This type of information can be stored in a
class variable, or static variable. 

In the following example a class variable called `created` has been defined to store the amount of dogs. Notice that the variable is defined outside the
initializer. The definition statement of a class variable does not include the `self.` prefix. (The prior barking feature has been left out of this example).

```python
class Dog:
    created = 0
	
    def __init__(self, name, birth_year, sound="Woof woof"):
        self.name = name
        self.birth_year = birth_year
        self.sound = sound
	Dog.created = Dog.created + 1

dog1 = Dog("Rascal", 2018)
dog2 = Dog("Boi", 2022, "Yip yip yip")
print (f"{Dog.created} dogs have been created so far.")
```

The value of a class variable is referenced by writing both the name of the class and the class variable, in this example `Dog.created`.

The program produces the following output:

Ohjelma tuottaa seuraavan tulosteen:
```monospace
2 dogs have been created so far.
```
