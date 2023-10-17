#!/usr/bin/python3
from models.base_model import BaseModel

my = BaseModel()
my.name = "My_first_Model"
my.number = 89
print(my.id)
print(my)
print(type(my.created_at))
print("--")
my_json = my.to_dict()
print(my_json)
print("JSON of my_model:")
for key in my_json.keys():
    print("\t{}: ({}) - {}".format(key, type(my_json[key]), my_json[key]))

print("---")
my_new = BaseModel(**my_json)
print(my_new.id)
print(my_new)
print(type(my_new.created_at))

print("--")
print(my is my_new)
