from sqlalchemy import create_engine, Column, String, Integer, Numeric
from sqlalchemy.orm import declarative_base, sessionmaker

db_url = "sqlite:///:memory:"
engine = create_engine(db_url)

Base = declarative_base()
class Person(Base):
    __tablename__ = 'persons'
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    name = Column('name', String(45))
    country = Column(String(45))
    salary = Column(Numeric(10,2))

    def __repo__(self):
        return f"{self.name}"

Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()

session.add(Person('Anderson', country='Brazil', salary=2000.00)) # add um só registro.
session.commit()
session.close()

session.add(Person('Renata', country='Brazil', salary=5000.00)) # add um só registro.
session.commit()
session.close()

session.add_all([Person('Tina', country='USA',  salary=1000.00), Person('Jessy', country='England', salary=3000.00)]) ## add mais de um registro.
session.commit()
session.close()

person = session.get(Person, 2)
print(person.name)
session.close()

person = session.query(Person).filter_by(id=4).one_or_none()
print(person)
session.close()

print("\n")

persons = session.query(Person).order_by(Person.id.desc(), Person.name).all()
for person in persons:
    print(f"{person.id}: {person.name} - {person.country}")

print("\n")

persons = session.query(Person).order_by(-Person.id, Person.name.asc()).all()
for person in persons:
    print(f"{person.id}: {person.name} - {person.country}")

print("\n")


persons = session.query(Person).filter((Person.id > 1) & (Person.name.contains('T'))).all()
for person in persons:
    print(f"{person.id}: {person.name} - {person.country}")

print("\n")


"""
where()

Introduzido para aproximar a API ORM da API Core do SQLAlchemy.
Funciona igual ao .filter() quando usado com ORM.
Também aceita condições SQLAlchemy.
Seu uso é mais moderno, mas não tem vantagem funcional clara sobre filter() no ORM.

Pequena diferença técnica
filter() permite texto SQL bruto em certas versões (mas não recomendado):
session.query(Person).filter("age > 30")

Pequena diferença técnica
filter() permite texto SQL bruto em certas versões (mas não recomendado):

session.query(Person).filter("age > 30")

"""

persons = session.query(Person).where((Person.id > 1) & (Person.name.contains('T'))).all()
for person in persons:
    print(f"{person.id}: {person.name} - {person.country}")

print("\n")

from sqlalchemy import or_, and_, not_

persons = session.query(Person).where(or_(Person.id == 5), (Person.name.contains('T'))).all()
for person in persons:
    print(f"{person.id}: {person.name} - {person.country}")

print("\n")

persons = session.query(Person).where(and_(Person.id == 3), (Person.name.contains('J'))).all()
for person in persons:
    print(f"{person.id}: {person.name} - {person.country}")


print("\n")

persons = session.query(Person).where(not_(Person.id == 5)).all()
for person in persons:
    print(f"{person.id}: {person.name} - {person.country}")

print("\n")

from sqlalchemy import func

persons = session.query(Person.country, func.count(Person.id)).group_by(Person.country).all()
for person in persons:
    print(f"{person}")

print("\n")

print('by tuple listing...')
for name, country in persons:
    print(f"{name}: {country}")

print("\n")

# ----------

from sqlalchemy import func

sums_salary_by_country = session.query(Person.country, func.sum(Person.salary)).group_by(Person.country).all()
for sum in sums_salary_by_country:
    print(sum)

counts_persons_by_country = session.query(Person.country, func.count(Person.id)).group_by(Person.country).all()
for count in counts_persons_by_country:
    print(count)

greaters_salary_by_country = session.query(Person.country, func.max(Person.salary)).group_by(Person.country).all()
for greaters in greaters_salary_by_country:
    print(greaters)

print('listing by tuple...')
for k, v in greaters_salary_by_country:
    print(f"{k}: {v}")

# ----------



