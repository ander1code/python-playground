from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import sessionmaker, declarative_base
import os

# Apagar banco (opcional)
if os.path.exists('database.db'):
    os.remove('database.db')

# Criar engine
db = create_engine("sqlite:///database.db")

# Declarar Base apenas UMA vez
Base = declarative_base()

# -----------------------------
# MODELS
# -----------------------------

class Person(Base):
    __tablename__ = 'persons'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)

class Car(Base):
    __tablename__ = 'cars'
    id = Column(Integer, primary_key=True, autoincrement=True)
    model = Column(String)
    person_id = Column(Integer, ForeignKey('persons.id'))
    price = Column(Float)

# Criar tabelas
Base.metadata.create_all(bind=db)

# Sessão
Session = sessionmaker(bind=db)
session = Session()

# -----------------------------
# FUNÇÕES
# -----------------------------

def add_persons():
    people = ['Anderson','Anne','Taissa','Laura','Tiffany','Jason','Paul']
    for p in people:
        session.add(Person(name=p))
    session.commit()
    print("Persons added.")

add_persons()

def add_cars():
    cars = [
        {'model':'Land Rover','price':25000.00},
        {'model':'Jip','price':30000.00},
        {'model':'Corolla','price':50000.00},
        {'model':'Corolla 2','price':40000.00},
        {'model':'Astra','price':45000.00},
        {'model':'Fusca','price':35000.00},
        {'model':'Brasília','price':15000.00},
    ]

    persons = session.query(Person).all()
    
    for i, car in enumerate(cars):
        session.add(Car(
            person_id = persons[i].id,
            model = car['model'],
            price = car['price']
        ))
    session.commit()

    print("Cars added.")

add_cars()

def get_person_by_id(id):
    person = session.query(Person).filter_by(id=id).first()
    if person:
        print(person.name)

get_person_by_id(4)

def get_person_by_name(name):
    persons = session.query(Person).filter(
        Person.name.like(f"{name}%")
    ).all()

    for person in persons:
        print(person.name)

get_person_by_name("A")

def update_person(id):
    person = session.query(Person).filter_by(id=id).first()
    if person:
        person.name = 'Anderson Conceição'
        session.add(person)
        session.commit()
        print('Successfully edited.')
    else:
        print('Person not found.')

update_person(1)

persons = session.query(Person).all()
for person in persons:
    print(f"- {person.name}")

def delete_person(id):
    person = session.query(Person).filter_by(id=id).first()
    if person:
        session.delete(person)
        session.commit()
        print('Successfully deleted.')
    else:
        print('Person not found.')

delete_person(3)


persons = session.query(Person).all()
for person in persons:
    print(f"- {person.name}")