from sqlalchemy import create_engine, Column, String, Integer, Numeric, Date, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base, Relationship, relationship

from datetime import datetime

database = 'database.db'

import os
if os.path.exists(database):
    os.remove(database)
    print('Database was dropped.')

db_url = f"sqlite:///{database}"
engine = create_engine(db_url)

Base = declarative_base()

class Person(Base):
    __tablename__ = 'persons'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(45), nullable=False)
    email = Column(String(45), nullable=False, unique=True) 
    salary = Column(Numeric(10,2), nullable=False)
    birthday = Column(Date, nullable=False)

class Car(Base):
    __tablename__ = 'cars'
    id = Column(Integer, primary_key=True, autoincrement=True)
    # person_id = Column(ForeignKey('persons.id'))  # atencao aqui!
    model = Column(String(45), nullable=False)
    license_plate = Column(String(7), unique=True, nullable=False)
    # person = Relationship('Person', backref='persons.id', lazy='subquery') # atencao aqui!
    person = relationship(Person)

Base.metadata.create_all(bind=engine)  # atencao aqui!
print('Database created.')