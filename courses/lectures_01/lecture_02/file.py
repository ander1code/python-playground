# length
print(len("Anderson"))

lorem = '''Lorem ipsum dolor sit amet, consectetur adipisci elit, sed\n 
eiusmod tempor incidunt ut labore et dolore magna aliqua.\n 
Ut enim ad minim veniam, quis nostrum exercitationem ullam corporis\n 
suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur.\n 
Quis aute iure reprehenderit in voluptate velit esse cillum dolore\n 
eu fugiat nulla pariatur. Excepteur sint obcaecat cupiditat non proident,\n
sunt in culpa qui officia deserunt mollit anim id est laborum.'''

print(lorem)
print(len(lorem))

print("Hello,\tWorld!")

hello = "Hello, World!"
print(hello[7:])
print(hello[7:12])
print(hello[7:len(hello)])
print(hello[12:7]) # nao mostra nada!
print(hello[-6:0]) 

name = "anderson"
print(name.find("n"))
print(name.find("z"))
print(name.endswith("son"))
print(name.replace("son", "father"))
print(name.count("n"))
name = name.capitalize()
print(name)
name =name.upper()
print(name)
name = name.lower()
print(name)

age = 15
if(age >= 18):
    print("Adulto")
elif((age >= 14) and (age < 18)):
    print("Teen")
elif(age < 14):
    print("Child")
else:
    print("Nothing")




