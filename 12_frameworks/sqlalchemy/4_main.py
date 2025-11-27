"""

# NEW WAY TO COLUMN CREATE

from sqlalchemy import create_engine, Column, String, Integer, Numeric, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, mapped_column, DeclarativeBase, Mapped

"""

from sqlalchemy import create_engine, Column, String, Integer, Numeric
from sqlalchemy.orm import declarative_base, sessionmaker

db_url = f"sqlite:///:memory:"
engine = create_engine(db_url, echo=True)

# Base = declarative_base()

class Base(DeclarativeBase):
    pass

class Person(Base):
    __tablename__ = 'persons'
    
    # id = Column(Integer, primary_key=True, autoincrement=True)
    # id = mapped_column(Integer, primary_key=True, autoincrement=True)
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)

    # name = Column(String(45), nullable=False)
    name = mapped_column(String(45), nullable=False)

    # email = Column(String(45), nullable=False, unique=True) 
    # email = mapped_column(String(45), nullable=False, unique=True)
    email: Mapped[str] = mapped_column(nullable=False, unique=True)

    # salary = Column(Numeric(10,2), nullable=False)
    salary = mapped_column(Numeric(10,2), nullable=False)
    

class Car(Base):
    __tablename__ = 'cars'
    # id = Column(Integer, primary_key=True, autoincrement=True)
    id = mapped_column(Integer, primary_key=True, autoincrement=True)
    # person_id = Column('Person', ForeignKey('persons.id'))
    person_id = mapped_column('person_id', ForeignKey('persons.id'))

Base.metadata.create_all(engine)  # atencao aqui!
print('Database created.')
