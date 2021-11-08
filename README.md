# AirBnB

## Project Description

This is the first step towards building a full web application: the AirBnB clone. This first step is very important because you will use what you build during this project with all other following projects: HTML/CSS templating, database storage, API, front-end integration

Each task is linked and will help you to:

- put in place a parent class (called BaseModel) to take care of the initialization, serialization and deserialization of your future instances
- create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
- create all classes used for AirBnB (User, State, City, Place) that inherit from BaseModel
- create the first abstracted storage engine of the project: File storage.
- create all unittests to validate all our classes and storage engine

## Description of the command interpreter

Its exactly the same as the shell but limited to a specific use-case. In our case, we want to be able to manage the objects of our project:

- Create a new object (ex: a new User or a new Place)
- Retrieve an object from a file, a database etc
- Do operations on objects (count, compute stats, etc)
- Update attributes of an object
- Destroy an object

### How to start it, How to use it, with Examples.
**Execution**
Your shell should work like this in interactive mode:

```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb)
(hbnb)
(hbnb) quit
$
```
But also in non-interactive mode: (like the Shell project(simple shell) in C)

```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
```

All tests should also pass in non-interactive mode:
```
$ echo "python3 -m unittest discover tests" | bash
```