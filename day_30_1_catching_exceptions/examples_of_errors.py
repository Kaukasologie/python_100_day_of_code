# FileNotFoundError
with open("file.txt") as file:
    file.read()

# KeyError
dictionary = {"key": "value"}
value = dictionary["non_existent_key"]

# IndexError
fruit_list = ["Apple", "Banana", "Pear"]
fruit = fruit_list[3]

# TypeError
text = "abc"
print(text + 5)
