# Final project assignment

The goal of the final project work is to modify and complete the functional prototype you created during the preliminary 
project so that the outcome is **a web-based flight simulator game that uses a map service and an external data source**.

![Hot-air Balloon](img/640px-Hot_Air_Balloon_Launch_(Unsplash).jpg)

<sub><sup>Kuumailmapallon kuva: Songeunyoung songeunyoung, CC0, via Wikimedia Commons</sup></sub>


## Requirements specification

The requirement specification document describes what the final, extended flight simulator game can be used for. 
You may use the contents and parts of the requirement specification of the preliminary project in your new requirement 
specification document.

The requirements document must include at least the following chapters:
1. Introduction
2. Current State
3. Vision
4. Functional Requirements
5. Quality Requirements

Chapter 1 (Introduction) discusses the purpose and target audience of the document. Also the structure of the document can be 
described in the Introduction.

Chapter 2 (Current State) explains the current state of the project work: What can your prototype of the flight simulator be used for?

Chapter 3 (Vision) describes the general idea of the new, extended flight simulator game. How does the user play the game and what 
happens in the game? The vision can again be presented as an image with a supporting text description.

Chapter 4 (Functional Requirements) describes what the user can do with the extended game. Write more user stories the same way 
as in the requirement specification of the preliminary project.

Chapter 5 (Quality requirements) specifies what requirements the game has other than the functional requirements. These could for example be
requirements relating to response time or usability.kattavuus

## Boundary conditions for the game

The finished flight simulator game must follow the boundary conditions listed below. You are again free to design and implement any type 
of a game you want as long as it fulfills these conditions:

1. The user playes the game in an interactive way on a browser.
2. The user interface (UI) is implemented using HTML language and CSS style sheets. JavaScript is used for implementing the necessary 
browser functionality.
3. The operation logic of the game is implemented as a Python-based backend service that provides an API for the browser.
4. The communication between the backend service and the browser is implemented using API requests and JSON responses.
5. The game's backend service utilizes a relational database that is based on the airport database used on this course. The schema of 
the database can be modified and extended freely as needed.
6. The game has a concrete goal and it offers a good gaming experience.
7. The game takes sustainable development factors into account.
8. The game follows a good gaming etiquette and courtesy and is also suitable for young users (12+).

The following criteria are not mandatory but they will be regarded as merits:
1. Satellite or map data is shown graphically on the browser.
2. The program utilizes the object-oriented features of Python.
3. The game's backend service communicates with at least one external data source and/or the map service.


## Evaluation of the requirements specification document

The requirement specification document for the final project applies the same criteria as the document written in the preliminary project. 
The evaluation of the requirement specification document is again based on coverage and quality. Especially the following factors are considered:
- Does the vision provide a general view of the game and the idea behind the game?
- Has the functionality of the game been presented in a comprehensive, unambiguous, concrete and feasible way? Does the document give an accurate 
impression of how the game works?
- Does the game contain novel ideas?
- Have the necessary quality requirements been presented in a concrete way?
- Does the game fulfill the set boundary conditions for the game?
- Can the document be considered a high-quality, technical document in terms of language and appearance?
