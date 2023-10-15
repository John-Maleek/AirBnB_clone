# AirBnB_clone

## Project Description:

This project is the first step towards building a fullstack clone of the AirBnB product
It consists of the following: - Models (BaseModel, User, City, State, Place, Amenity, Place and Review) - Command Interpreter (console.py)

## Starting the interpreter:

In the root project folder, run the following command:

``to start the interpreter
python3 console.py

## How to use interpreter

``to create an object while in the interpreter
create <class_name>
example:
create BaseModel

``update an object
update <class_name> <object_id> <attribute> <attr_val>
ex:
update BaseModel 1234 name john_doe

``delete an object
destroy <class_name> <object_id>
ex:
destroy BaseModel 1234

``show an object
show <class_name> <oobject_id>
ex:
show BaseModel 1234

``display all objects
all

``display all objects related to a class
all <class_name>
ex:
all BaseModel
