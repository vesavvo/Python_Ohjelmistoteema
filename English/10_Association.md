# Association

In this module you will learn to write programs where objects can interact with each other.

In object-oriented programming a program is composed of classes. The classes are used to create
instances, or objects, during runtime. The objects can interact with each other: an object can
process other objects and call their methods.

This relationship between objects is called association. The power of object-oriented programming is achieved
by programming these associative relationships: the program breaks up into small, easily understandable pieces
and the programmer can write code in small portions, focusing in one feature at a time. When the associations
between objects are designed well, even a large program is easy to build with these small parts.

## Designing the structure

In the last module we wrote a `Dog` class that defines the properties of a dog (name, birth year and distinctive barking
sound). Furthermore, the class has a single method: `bark`. The `Dog` class looks like this:

```python
class Dog:
    def __init__(self, name, birth_year, sound="Woof woof"):
        self.name = name
        self.birth_year = birth_year
        self.sound = sound

    def bark(self, times):
        for i in range(times):
            print(self.name + " barks: " + self.sound)
        return
```

Let's extend the example by adding a dog hotel. A dog hotel is defined as follows: a dog can be taken to a dog hotel and 
later be picked up from the hotel. Occasionally, a member of the dog hotel staff takes a round around the hotel: they greet 
all the dogs and each dog barks back.

First, we will need to think about what we need to implement the dog hotel.

First of all, the dog hotel should be implemented as a separate class. The functionality of the dog hotel has nothing to
do with a single dog, so it should not be written inside the Dog class. Therefore, we will add a second class called Hotel 
to our program.

Next, we need to think about what properties relate to a dog hotel. We notice that a dog hotel must know which dogs are in
its care at any given time. This can be done by using a list: let's add a list of dogs as a property of the Hotel class.

What about activities of a dog hotel that should be written into methods? From the definition earlier we
can identify three methods we should write for a dog hotel:
1. Checking a dog in to the dog hotel.
2. Checking a dog out from the dog hotel.
3. Doing a round in the dog hotel.

Now we have defined and designed the program and we can go ahead to implement it.

## A program with two classes

There are two classes in our example program: `Dog` and `Hotel`. In Python, it is common to write multiple classes into 
a single source file. The classes could also be in separate files. If the classes are in placed in
separate files, referencing another class is only possible if an `import` statement for the other file (or module) is added
at the beginning of the program. 

It is handy to write classes of a small program into one file, and this is what we will do now. We will create a file called
doghotel.py where we will program all the required functionality:

```python
class Dog:
    def __init__(self, name, birth_year, sound="Woof woof"):
        self.name = name
        self.birth_year = birth_year
        self.sound = sound

    def bark(self, times):
        for i in range(times):
            print(self.name + " barks: " + self.sound)
        return

class Hotel:
    def __init__(self):
        self.dogs = []

    def dog_checkin(self, dog):
        self.dogs.append(dog)
        print(dog.nimi + " checked in")
        return

    def dog_checkout(self, dog):
        self.dogs.remove(dog)
        print(koira.name + " checked out")
        return

    def greet_dogs(self):
        for dog in self.dogs:
            dog.bark(1)

# Main program

dog1 = Dog("Rascal", 2018)
dog2 = Dog("Boi", 2022, "Yip yip yip")

hotel = Hotel()

hotel.dog_checkin(dog1)
hotel.dog_checkin(dog2)
hotel.greet_dogs()

hotel.dog_checkout(dog1)
hotel.greet_dogs()
```

The example program consists of three parts:
1. the `Dog` class
2. the `Hotel` class
3. the main program.

The execution of the program starts at the beginning of the main program. First two dogs, Rascal and Boi, are created.
Then a new hotel is created:

```python
hotel = Hotel()
```

Now the execution moves to the initializer of the Hotel class where an empty dogs list is added as a property of
the hotel. The newly created hotel does not have any guests yet, but it has an empty list for storing dogs later.

Next, the first dog (Rascal) is checked in to the hotel:

```python
hotel.dog_checkin(dog1)
```

This is a method provided by the hotel: the check-in is clearly an activity of the hotel, which is why it has been
programmed into the `Hotel` class. It is necessary to know which dog is going to be checked in, so the corresponding
Dog object (or actually a reference to the object) is passed as an argument in the method call. When the method is called,
the execution moves to the `dog_checkin` method where the dog received as a parameter is added to the dog list of the hotel.

The second dog Boi is checked in to the hotel the same way.

Now it is time for the caretaker to do a round in the hotel and greet all the dogs. To do this the corresponding method written
in the `Hotel` class is called:

```python
hotel.greet_dogs()
```

This method was implemented without parameters. The greeting is targeted to all dogs that are currently in the hotel and
the hotel itself knows which dogs its taking care of at any given time. The method iterates through the list of dogs and
tells each dog to bark once.

Finally, one dog, Boi, is checked out from the hotel. For this, the corresponding method that removes a dog from the list
in the `Hotel` class is called. Then the dogs are greeted again, but this time only Rascal is there to answer.

The operation of the program can be seen from its output:

```python
Rascal checked in
Boi checked in
Rascal barks: Woof woof
Boi barks: Yip yip yip
Boi checked out
Rascal barks: Woof woof
```

Now we have written a program that has instances (or objects) from two different classes. We can say that there is a
permanent association between the `Hotel` class and the `Dog` class: A `Hotel` object has an instance variable that
holds the references to `Dog` objects.

Here the associative relationship is unidirectional: A `Hotel` object knows which dogs are currently staying in the hotel.
On the other hand, a `Dog` object has no knowledge of the hotel it might currently be staying in. An associative relationship
can be implemented either unidirectionally or bidirectionally. A bidirectional association should only be used when absolutely
needed. Bidirectional association brings an extra burden to the programmer because the contents of the object references to 
different directions must be in sync.

## Temporary association

As was mentioned above, the `Hotel` and `Dog` classes in the example shared a static association: the dogs in the hotel
were stored as a list into the property of the hotel.

The `Hotel` and `Dog` classes also share another type of a dependency: The `Hotel` class provides to methods that
have a reference to a `Dog` object as a parameter. An associative relationship can also be valid only during a method call
when an instance of the other class is listed as a parameter of a method. When the method call finishes, the associative
relationship used during the method call would vanish if the information of the relationship wasn't stored as a property like
we did in our example. 

Let's look at an example of a situation where an associative relationship is purely temporary: the relationship between a
car and a car paint shop. In this example we will create a blue car and pass it to a paint shop to be painted red:


```python
class Car:
    def __init__(self, plate_number, colour):
        self.plate_number = plate_number
        self.colour = colour

class PaintShop:
    def paint(self, car, colour):
        car.colour = colour

paint_shop = PaintShop()
car = Car("ABC-123", "blue")
print("The car is " + car.colour)
paint_shop.paint(car, "red")
print("The car is now " + car.colour)
```

The program prints out the colour of the car before and after the paint job:

```monospace
The car is blue
The car is now red
```

In this example the paint shop knows the car it needs to paint only for time of the execution of the `paint` method as
the reference to the `Car` object was received as a parameter of the method call. Once the execution of method is finished,
the value of the parameter variable can no longer be accessed. The car has no knowledge of the paint shop either. In this 
example the associative relationship between the paint shop and the car is only temporary.
