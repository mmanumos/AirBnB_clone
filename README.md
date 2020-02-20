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
(The 'help' command is built into Cmd)

Output:
```bash
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update

(hbnb) 
```

## Our commands:
- 'EOF': Exit the program.
```bash
(hbnb) EOF
vagrant@vagrant-ubuntu-trusty-64:~/AirBnB_clone$ 
```

- 'all': Prints all string representation of all instances based or not on the class name.
```bash
(hbnb) all
[]
(hbnb) 
```
Shows empty square brackets when not exist instances created.

- 'create': Create a new instance.
```bash
(hbnb) create BaseModel
```
Generate an id automatically
```bash
(hbnb) create BaseModel
079572a6-d77e-4568-82f9-f090d61e45ca
(hbnb) 
```

- 'all': Prints all string representation of all instances based or not on the class name.
```bash
(hbnb) all
["[BaseModel] (079572a6-d77e-4568-82f9-f090d61e45ca) {'updated_at': datetime.datetime(2020, 2, 20, 16, 38, 47, 970448), 'created_at': datetime.datetime(2020, 2, 20, 16, 38, 47, 970419), 'id': '079572a6-d77e-4568-82f9-f090d61e45ca'}"]
(hbnb) 
```
Now shows all instances created.

- 'destroy': Deletes an instance based on the class name and id.
```bash
(hbnb) destroy BaseModel d87e3490-7937-46c5-910e-2ce3f7b898cf
```

- 'quit': Exit the program.
```bash
(hbnb) quit
vagrant@vagrant-ubuntu-trusty-64:~/AirBnB_clone$ 
```

- 'show': Print the string representation of an instance based on the class name and id.
```bash
(hbnb) show BaseModel 079572a6-d77e-4568-82f9-f090d61e45ca
[BaseModel] (079572a6-d77e-4568-82f9-f090d61e45ca) {'updated_at': datetime.datetime(2020, 2, 20, 16, 38, 47, 970448), 'created_at': datetime.datetime(2020, 2, 20, 16, 38, 47, 970419), 'id': '079572a6-d77e-4568-82f9-f090d61e45ca'}
(hbnb) 
```

- 'update': Updates an instance based on the class name an id by adding or updating attribute.
```bash
(hbnb) update BaseModel 079572a6-d77e-4568-82f9-f090d61e45ca name "Betty"
```

## Developers:
- Manuel Mosquera
- Javier Patarroyo

--------------------------------
Holberton School
AirBnB_clone
0x00. AirBnB clone - The console
Date: Started 02-13-2020, end by 02-20-2020 (in 7 days)
