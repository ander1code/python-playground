# NamedTuple:

from collections import namedtuple

Course = namedtuple("Course", ["language", "database"])
course1 = Course("Python", "MySQL")
print(course1)

# formatacao de impressao:
print(course1._asdict()) # dictionary

course2 = ["C#", "SQL Serve"]
print(Course._make(course2)._asdict())

# --------

Person = namedtuple("Person", ["id","name","birthday","address","gender","status",])
Person.__doc__ += "Person namedtuple"
Person.id.__doc__ += "Person ID"
Person.name.__doc__ += "Person name"
Person.birthday.__doc__ += "Person birthday"
Person.address.__doc__ += "Person address" 
Person.gender.__doc__ += "Person gender" 
Person.status.__doc__ += "Person status" 
print(Person.__doc__)

# ----------

# namedtuple:

from collections import namedtuple

req = namedtuple("Requirement", ["language", "database"])
rq1 = req("python", "sqlite3")
print(rq1._asdict())
for r in rq1:
    print(r)

import datetime
person = namedtuple("person",["id","name","salary","gender","birthday","status"])
person.name.__doc__ = "name!!!"
person.name = "Anderson"
print(person.__dict__)
print(person)
