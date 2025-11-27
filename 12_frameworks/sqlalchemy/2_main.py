from sqlalchemy import create_engine, Column, String, Integer, Numeric, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, Relationship

db = 'database.db'
# cria o engine para o banco
engine = create_engine(f"sqlite:///{db}")

def remove_database():
    import os
    if os.path.exists(db):
       os.remove(db)
       print('Database removed.')

"""
import os
if os.path.exists(db):
    os.remove(db)
    print('Database removed.')



# so cria o banco
Base = declarative_base()
Base.metadata.create_all(bind=engine)

print('Database created.')

from time import sleep
sleep(5)
"""

remove_database()

# criando tabelas
Base = declarative_base()

class Person(Base):
    __tablename__ = 'persons'
    id = Column('id', Integer, primary_key=True)
    name = Column('name', String(45), nullable=False)

    def __init__(self, name):
        self.name = name     

    def __repr__(self):
        return f"{self.name}"   

class Car(Base):
    __tablename__ = 'cars'
    id = Column('id', Integer, primary_key=True)
    person_id = Column('person_id', ForeignKey('persons.id'))
    model = Column('name', String(45), unique=True, nullable=False)
    price = Column('price', Numeric(precision=10, scale=2), nullable=False)
    person = Relationship('Person', backref='cars', lazy='subquery')

Base.metadata.create_all(bind=engine)

print('Database with tables created.')

# manipulando dados no banco de dados:

Session = sessionmaker(bind=engine)
# session = Session()

with Session() as session:
    def create_person():
        persons = ['Anderson', 'Leia', 'Jason', 'Jessy', 'Joyce', 'Carmen', 'Richard']
        for person in persons:
            session.add(Person(person))
        session.commit()
        print('Persons added.')
        session.close() # fechando a session!

    def create_car(person_id):
        # person = session.query(Person).filter_by(id=1).first()
        person = get_person_by_id(person_id)
        if person:
            # print(f"Adding car for {person.name}...")
            print(f"Adding car for {person}...")
            session.add(Car(model='Voyage', person_id=person.id, price=25000.00))
            session.commit()
            print('Car added.')
        else:
            print('Person not found.')
        session.close()

    def get_all_persons():
        # persons = session.query(Person).order_by(-Person.id).all() # ordenado de cima para baixo pelo ID.
        persons = session.query(Person).order_by(Person.id.desc()).all() # ordenado de cima para baixo pelo ID.
        session.close()
        return persons

    def get_person_by_id(id):
        print(f'get_person_by_id: {id}')
        person = session.get(Person, id)
        session.close()
        return person

    def get_persons_by_name(name):
        print(f'get_persons_by_name: {name}')
        persons = session.query(Person).filter(Person.name.like(f"{name}%")).all()
        session.close()
        return persons
    
    def get_cars_by_id(id):
        print(f'get_cars_by_id: {id}')
        person = session.get(Car, id)
        session.close()
        return person
    
    def get_all_cars():
        persons = session.query(Car).all()
        session.close()
        return persons

    def edit_person(id):
        person = get_person_by_id(id)
        if person:
            person.name = 'Anderson Conceição'
            session.add(person)
            session.commit()
            print("Person edited.")
            session.close()
        else:
            print('Person not found.')

    def edit_car(id):
        car = get_cars_by_id(id)
        if car:
            car.model = 'Voyage v1.0'
            car.price = 30000.00
            session.add(car)
            session.commit()
            session.close()
            print("Car edited.")
        else:
            print("Car not found.")

    def delete_car(id):
        car = get_cars_by_id(id)
        if car:
            session.delete(car)
            session.commit()
            session.close()
            print("Car deleted.")
        else:
            print("Car not found.")


    def show_persons(persons):
        if persons:
            print('SHOW PERSONS:')
            for person in persons:
                print(f" -- {person.id}: {person}")
            print("\n")
        else:
            print("No person found.")
    
    def show_cars(cars):
        if cars:
            print('SHOW CARS:')
            for car in cars:
                # print(f" -- {car.id}: {car.model}, {car.price} | Owner: {get_person_by_id(car.person_id).name}")
                print(f" -- {car.id}: {car.model}, {car.price} | Owner: {car.person.name}")
        else:
            print("No car found.")

create_person()
create_car(1)
edit_person(1)
show_persons(get_all_persons())
show_persons(get_persons_by_name('J'))
show_cars(get_all_cars())
edit_car(1)
show_cars(get_all_cars())
delete_car(1)
show_cars(get_all_cars())




