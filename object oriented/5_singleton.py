class SingletonClass:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            print("Criei o objeto!")
            # cls.__instance = super().__new__(cls)
            cls.__instance = object.__new__(cls)
        else:
            print("Não precisa mais criar!")
        return cls.__instance

    def __init__(self, name):
        self.name = name

obj1 = SingletonClass("first")
print(obj1.name)
obj2 = SingletonClass("second")
print(f"obj1.name: {obj1.name}") # second
print(f"obj2.name: {obj2.name}") 
print(id(obj1))
print(id(obj2))
print(obj1 is obj2)
