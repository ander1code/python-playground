file = open("lorem.txt", "r")
print(file) # <_io.TextIOWrapper name='lorem.txt' mode='r' encoding='cp1252'>
print(file.read())
file.close()

file = open("file.txt", "w", -1, "utf-8")
file.write("Hello, World!")
file.close()
file = open("file.txt", "r", -1, "utf-8")
print(file.encoding)
print(file.read())
print(type(file)) # <class '_io.TextIOWrapper'>
print(open("file.txt", "r").read())
file.close()

# file = open("people.txt", "x", -1, "utf-8") # create new file
file = open("people.txt", "w", -1, "utf-8") # create new file

people = ("Fernanda", "Anderson", "Anne", "Sara")

for el in people:
    file = open("people.txt", "a", -1, "utf-8") # append to file
    file.write(el + " ")
    file.close()

file = open("people.txt", "r", -1, "utf-8") # read file
print(file.read())

print(f"{open("lorem.txt", "r").read(5)}")

print(open("lorem.txt", "r").readline())


name = "Anderson"
print (f"Hello, {name}!")

# class Person:
#     def __init__(self, id, name):
#         self.id = id
#         self.name = name
    
#     def __str__(self):
#         return f"ID:{self.id} | NAME:{self.name}"
    

# person = Person(123, "Anderson")
# # file = open("person.txt", "w")
# # file.write(person) # ----------------- error!
# # file.close()
# # file = open("person.txt", "r")
# # person = file.read()
# # print(person.__str__)
# # file.close()
# print(person.__str__) # <bound method Person.__str__ of <__main__.Person object at 0x0000023373C76A50>>
# print(person.__str__())


class EditorClass:
    def __init__(self, file):
        try:
            self.file = file
        except ValueError:
            print("Error initilizating.")

    def writeFile(self, param):
        try:
            with open(self.file, "w") as f:
                f.write(param)
        except ValueError:
            print("Error writing.")

    def readFile(self):
        try:
            with open(self.file, "r") as f:
                print(f.read())
        except ValueError:
            print("Error reading.")

    def deleteFile(self):
        try:
            import os
            os.remove(self.file)
        except ValueError:
            print("Error deleting.")
    
editor = EditorClass("editor.txt")
editor.writeFile("Hello, World!")
editor.readFile()
editor.deleteFile()

data = "Java"
name = data.replace("Java", "Python")
print(data)


def findFile(param):
    try:
        with open("lorem.txt", "r") as f:
            data = f.read()
            if data.find(param) != -1 :
                print("Exists!")
            else:
                print("No exists!")
    except ValueError:
        print("Error reading.")


findFile("lorem")
findFile("Lorem")

nums = "5,6,4,7,3,8,2,9,1,0"
print(nums.split(","))