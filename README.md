# AirBnB clone - The console

## Description of the project:
The goal of the project is to deploy on your server a simple copy of the AirBnB website.
This is the first part that is composed by an interpreter of command line that saves the data of instances in a JSON file. It is developed in Python language using mainly the class Cmd.
This project have implemented into the development the unit tests for its general working, used for this the Unittest framework.

## Description of the command interpreter:
- How to start it
Start the console by executing the 'console.py' file:
```bash
./console.py
```
- How to use it
The 'prompt (hbnb)' tells you that the console is ready to receive instructions, type the instruction:
```bash
(hbnb) 
```
- Example
The 'help' command shows all commands available in the console:
```bash
(hbnb) help
```
- Output:
```bash
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update

(hbnb) 
```
## Our commands:
- 'EOF': Exit the program.
- 'all': Prints all string representation of all instances based or not on the class name.
- 'create': Create a new instance.
- 'destroy': Deletes an instance based on the class name and id.
- 'help': Shows the list of commands available. (The 'help' command is built into Cmd)
- 'quit': Exit the program.
- 'show': Print the string representation of an instance based on the class name and id.
- 'update': Updates an instance based on the class name an id by adding or updating attribute.

## Developers:
- Manuel Mosquera
- Javier Patarroyo

--------------------------------
Holberton School
AirBnB_clone
0x00. AirBnB clone - The console
Date: Started 02-13-2020, end by 02-20-2020 (in 7 days)
