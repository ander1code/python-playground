import os
import django
import random
from datetime import date, timedelta
from faker import Faker
from decimal import Decimal, ROUND_HALF_UP

# Configuração do Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pjstart.settings')  # substitua 'seu_projeto' pelo nome do seu projeto
django.setup()

from modelsapp.models import Person, Car  # substitua 'seu_app' pelo nome do seu app

fake = Faker('pt_BR')

def generate_birthday(min_age=18, max_age=65):
    today = date.today()
    age = random.randint(min_age, max_age)
    birthday = today - timedelta(days=365 * age)
    return birthday

def create_fake_person():
    gender = random.choice(['M', 'F', 'O'])
    name = fake.name_male() if gender == 'M' else fake.name_female()
    email = fake.unique.email()
    birthday = generate_birthday()
    salary = Decimal(random.uniform(1500, 20000)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
    status = random.choice([True, False])

    person = Person(
        name=name,
        gender=gender,
        birthday=birthday,
        email=email,
        salary=salary,
        status=status
    )
    person.save()
    return person

def create_fake_car(person):
    car_model = random.choice([choice[0] for choice in Car.CARS])
    car = Car(person=person, model=car_model)
    car.save()

def populate(n=10):
    for _ in range(n):
        try:
            person = create_fake_person()
            create_fake_car(person)
            print(f"Adicionado: {person.name} com carro {person.car_set.first().model}")
        except Exception as e:
            print(f"Erro ao adicionar dados: {e}")

if __name__ == '__main__':
    populate(30)  # Altere o número para quantos registros quiser
