import random


class Animal:
    def __init__(self, name):
        self.name = name

    def returnvalue(self):
        return self.name


# List of letters to generate the names.
letters = ["A", "Ą", "B", "C", "Ć", "D",
           "E", "Ę", "F", "G", "H", "I", "J", "K", "L", "Ł", "M", "N", "Ń", "O", "Ó", "P",
           "Q", "R", "S", "Ś", "T", "U", "V",
           "W", "X", "Y", "Z", "Ź", "Ż"]
user_input = input("Provide the number of objects you want to create: ")
animals = []
for i in range(0, int(user_input) + 1):
    if len(letters) == 0:
        print("List can't be empty")
        break

    if i % 2 == 0:
        temporary_animal = Animal("Person: " + "" + letters[i % len(letters)])
        animals.append(temporary_animal)
        print(f"{i} is even")
        print(f"object name " + str(temporary_animal.returnvalue()) + " has been created")
    else:
        temporary_animal = Animal("The Not Even Guy")
        print(f"{i} is not even")
        print(f"object name " + str(temporary_animal.returnvalue()) + " has been created")
