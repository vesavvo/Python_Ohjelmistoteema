# Preliminary project assignment

Your goal is to build a **functional prototype of a flight simulator game**.

![Electric Airplane](img/Pipistrel_WATTsUP_airplane.jpg)

<sub><sup>An image of the Pipistrel WATTsUP electric airplane: Ymmo, CC BY-SA 4.0 <https://creativecommons.org/licenses/by-sa/4.0>, via Wikimedia Commons</sup></sub>

The prototype flight simulator is a game where the player can travel either globally or in a predefined area. The game 
uses the locations of real airports.

The project consists of four phases:

1. Defining the requirements for the game in the preliminary project. (During Software 1)
2. Implementation and testing of the preliminary project. (During Software 1)
3. A more detailed list of requirements for the final project work. (During Software 2)
4. Implementation and testing of the final project work. (During Software 2)

The first two phases are completed during the Software 1 study module. The goal of the preliminary project is to build 
a functional prototype of the flight simulator that utilizes Python and a relational database. 

The last two phases are completed over the Software 2 study module. The functional prototype built during the previous 
study module is used as a basis of the final project. The prototype is extended and modified by adding a web-based user interface (UI)
that uses a map service. Furthermore, the game is programmed using an external data source, such an online weather service.

The requirement specification phase of the preliminary project aims at finding a shared vision of what type of an application the team will
start building in the preliminary project. You will produce a written requirement specification document that describes all the functionality
of the application, meaning what can be done using the upcoming software. Furthermore, the specification lists requirements that can not be 
summarized into plain actions. These are called quality requirements and can for example relate to performance, response times or usability.

## Requirement specification document

The most important virtue of the requirement specification document is its concreteness. The operation of the software is described 
in such precision that there is as little room as possible left for interpretation. No features are typically left to be decided 
during the implementation phase. 

As said, the functionality and quality requirements are listed in the requirement specification. This is done from the user's perspective: 
the document should answer the question "What can the user do with the software?". The technical aspects of the implementation are not 
discussed.

The requirement specification document must contain at least the following chapters:
1. Introduction
2. Vision
3. Functional requirements
4. Quality requirements

Chapter 1 (Introduction) discusses what the purpose of the document is and who it is targeted to. Also the structure of the document 
can be presented in the Introduction.

Chapter 2 (Vision) describes the general idea of the the flight simulator game. What is the purpose of the game and how does it work? 
The vision can be presented also as a figure that is supported by a written description. Here you must explain the main idea of the game 
in your own words: how does the game proceed and what stages must the player go through?

Chapter 3 (Functional requirements) discusses everything the user can do with the game. The functional requirements are typically presented 
as user stories with a role (who), action (what), and benefit (why). An example of a user story would be "As a player I can choose the next 
airport from the cities showing on the map, so that my electric airplane will move there.". The example user story contains a role (player),
an action (selecting the next city) and a benefit the user can gain by completing the action (moving to the new location). There are enough 
user stories when they together describe all functionality of the game. For the flight simulator this probably means dozens of user stories.
Each user story must be unambiguous and concrete. It must be possible to look back at the user stories later to determine whether each 
planned functionality has been implemented in the software.

Chapter 4 (Quality requirements) defines other requirements besides the functional requirements the flight simulator has. Examples of these 
could be performance requirements ("Fetching airport information from the database must take a maximum of two seconds.") or usability 
requirements ("The user must get instant feedback from all actions they perform").

A requirements specification document can be evaluated with the following questions:

- Does the vision provide a general view of the game and the idea behind the game?
- Has the functionality of the game been presented in a comprehensive, unambiguous, concrete and feasible way? Does the document give an accurate 
impression of how the game works?
- Does the game contain novel ideas?
- Have the necessary quality requirements been presented in a concrete way?
- Does the game fulfill the set mandatory conditions for the game?
- Can the document be considered a high-quality, technical document in terms of language and appearance?



## Mandatory conditions for the game

A set of mandatory conditions are used as a basis for the requirement specification. The purpose of the mandatory conditions is that you will 
reach the defined learning objectives of the course when working on the game project.

Therefore, you can design and implement any type of a game you want as long as it fulfills the boundary conditions listed below:

1. The user plays the game interactively using their keyboard.
2. The game utilizes a relational database that is based on the airport database that has been used on this course. The schema of the 
database can be freely modified and extended as needed.
3. The game has a concrete goal, and it produces a good game experience.
4. The game takes sustainable development into account.
5. The game follows a good gaming etiquette and courtesy and is also suitable for young users (12+).

## Determining the Grade

The evaluation of the project follows the following guidelines:

- **Grade 1**: The work reflects an effort to meet the mandatory conditions 1-5. There are deficiencies and weaknesses in the technical implementation, or the work is modest in scope and ambition.
- **Grade 3**: The game fulfills the mandatory conditions 1-5. There are no significant shortcomings in the technical implementation. From the perspective of its scope and complexity, the work is of a good standard.
- **Grade 5**: The game fulfills the mandatory conditions 1-5. The work is of high quality in terms of technical implementation and the structural quality of the source code. The skilled and versatile use of learned technologies is emphasized in the work.

The individual grade derived from the project grade is also influenced by continuous evidence, self-assessment, and peer assessment.
