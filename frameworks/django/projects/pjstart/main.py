import os
import django

from django.db import connection

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pjstart.settings')
django.setup()

def execute_aggregate():
    from modelsapp.models import Person, Address, Car, Sale, SaleItem
    from django.db.models import Avg, Min, Max, Count, Sum, Q, F

    print(round(Person.objects.all().aggregate(Avg('salary'))['salary__avg']))
    print(round(Person.objects.all().aggregate(Sum('salary'))['salary__sum']))
    print(round(Person.objects.all().aggregate(Min('salary'))['salary__min']))
    print(round(Person.objects.all().aggregate(Max('salary'))['salary__max']))
    print(round(Person.objects.all().aggregate(Count('name'))['name__count']))

    print(Person.objects.values('name').annotate(salary=Max('salary')))
    # print(Person.objects.annotate(num_birthdays=Count('birthday')).num_birthdays)
    # print(num_birthdays)

    # result = Person.objects.annotate(num_names=Count('name'))
    # print(result)

    print(Person.objects.filter(Q(salary_gte=5000)))


from django.db import connection, connections

def execute_cursor():
    with connection.cursor() as cursor: # usando default database!
        sql = 'SELECT * FROM PERSON'
        people = cursor.execute(sql)
        for p in people:
            print(p)

    with connections['my_database'].cursor() as cursor:
        sql = 'SELECT * FROM PERSON'
        people = cursor.execute(sql)
        for p in people:
            print(p)

# execute_cursor()

def execute_stored_procedure(name):
    with connections['my_database'].cursor() as cursor:
        cursor.callproc('get_person_by_name', [name])

from django.db.transaction import non_atomic_requests, atomic
from modelsapp.models import Person

from django.http import JsonResponse

from django.db import transaction

@non_atomic_requests('my_database') # usar nas consultas!
def get_person_by_name(name):
    people = Person.manager.filter(name__istartswith=name)
    for p in people:
        print(f"{p.id} - {p.name}")

# get_person_by_name("A")

def create_person():
    Person.manager.create(
        name="Bob",
        gender="M",
        birthday="1991-01-01",
        email="alice@example.com",  
        salary=9000.00,
        status=True
    )
    transaction.on_commit(partial(show_message, message='Successfully created.'))

def delete_person():
    Person.manager.filter(
        email="alice@example.com",  
    ).delete()
    transaction.on_commit(partial(show_message, message='Successfully deleted.'))

from functools import partial

def show_message(message):
    print(message)

@atomic
def execute_creates():
    create_person()
    try:
        with transaction.atomic():
            create_person()
    except Exception as error:
        print(f'Error: {error}')
        delete_person()

# execute_creates()

from django.db import IntegrityError
from datetime import date


def create_person():
    try:
        p = Person()
        p.name="Bob"
        p.gender="M"
        p.birthday=date(1991, 11, 12)
        p.email="alice@example.com"
        p.salary=9000.00
        p.status=True
        p.save(using='my_database')
        transaction.on_commit(partial(show_message, message='Successfully created.'))
    except Exception as error:
        print(f'Error: {error}')
       
@atomic
def execute_person():
    create_person()
    try:
        create_person()
    except IntegrityError as error:
        print(f'Error: {error}')
        transaction.rollback()
        print('rollback!')
        delete_person()

# execute_person()

from django.db.models import Max

def using_database():
    
    p = Person.manager.using('my_database').filter(
        email="alice@example.com",  
    )
    p.delete()
    transaction.on_commit(partial(show_message, message='Successfully deleted.'))

    p = Person(
        name="Bob",
        gender="M",
        birthday="1991-01-01",
        email="alice@example.com",  
        salary=9000.00,
        status=True
    )
    p.save(using='my_database')
    transaction.on_commit(partial(show_message, message='Successfully created.'))

    max_pk = Person.manager.aggregate(Max('pk'))['pk__max']
    people = Person.manager.using('my_database').get(pk=max_pk)
    print(f"{people.pk} - {people.name}")

# using_database()


# db_tablespace = "tables"  # Tablespace da tabela
# indexes = [
# models.Index(fields=["shortcut"], db_tablespace="other_indexes")  # Tablespace do índice
# ]

def delete_person_to_bulk_create():
    p = Person.manager.using('my_database').filter(
        email="alice@example.com",  
    )
    p.delete()
    p = Person.manager.using('my_database').filter(
        email="bob@example.com",  
    )
    p.delete()
    print('Successfully deleted.')

def execute_bulk_create():
    delete_person_to_bulk_create()
    people = [
        Person(
            name="Alice",
            gender="F",
            birthday=date(1990, 1, 1),
            email="alice@example.com",
            salary=10000.00,
            status=True
        ),
        Person(
                name="Bob",
                gender="M",
                birthday=date(1991, 2, 2),
                email="bob@example.com",
                salary=9500.00,
                status=True
            )
    ]
    Person.manager.bulk_create(people)
    print('Successfully created with bulk_create.')

delete_person_to_bulk_create()