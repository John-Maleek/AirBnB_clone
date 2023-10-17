my_dict = {"name": "siti", "age": 26, "city": "addis ababa"}

my_dict["country"] = "ethiopia"

for key in my_dict.keys():
    #value = my_dict[key]
    print("{}: {}".format(key, my_dict[key]))
