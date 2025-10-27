import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pjconcepts.settings')
django.setup()

from modelsapp.models import Person, PersonProxy

# Person.objects.create(name='Fulano 01', email='fulano@test.com', gender='M', description='Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.')

# fulana = Person.objects.create(name='Fulano 02', email='fulana@test.com', gender='F', description='Consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.')

# fulano = Person.objects.get(email__exact='fulano@test.com')

# fulano.siblings.add(fulana)

# p = Person(name='Fulando de Tal', email='hgasfdgfasgd@test.com', gender='M', description='Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.')
# print(p.full_clean())
# p.save()
# print('Successfully created!')

# print(Person.objects.get(email__exact='fulano@test.com').__dict__)

# p = Person.objects.get(email__exact='fulano@test.com')

# p = Person.objects.get(email__exact='fulana@test.com')
# p.name = 'fulana'
# p.save()

# for p in Person.objects.all():
#     print(p.__dict__)

# people = Person.manager.with_email('fulano@test.com').values_list('name', flat=True)
# for p in people:
#     print(p)

# people = Person.manager.all()
# for p in people:
#     print(p)



# p = Person.objects.get(email__exact='fulano@test.com')
# p.delete()

# p = Person(name='Fulano 01', email='fulano@test.com', gender='M', description='Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.')
# p.save()

# p = PersonProxy.objects.get(email__exact='fulano@test.com')
# p.delete()

# p = PersonProxy(name='Fulano 01', email='fulano@test.com', gender='M', address={
#   "address": {
#     "street": "Avenida Atlântica",
#     "number": 1702,
#     "neighborhood": "Copacabana",
#     "city": "Rio de Janeiro",
#     "state": "RJ",
#     "zipCode": "22021-001",
#     "country": "Brazil"
#   }
# }
# , description='Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.')
# p.save()

# p.get_description()


# from django.db.models import Q

# p = PersonProxy.objects.get(Q(email='fulano@test.com'), Q(name__startswith='fulano'))
    
# try:
#     p = PersonProxy.objects.get(Q(email='fulano@test.com'), ~Q(name__startswith='fulano'))
#     print(p)
# except PersonProxy.DoesNotExist as error:
#     print(error)


# p = PersonProxy.objects.filter(address__address__city='Rio de Janeiro')
# print(p)




from django.db.models import Max, Min, Count, Avg, Q, F


print(Person.objects.aggregate(Max('salary'))['salary__max'])
print(Person.objects.aggregate(Min('salary'))['salary__min'])
print(Person.objects.aggregate(person_salary_avg=Avg('salary'))['person_salary_avg'])
print(Person.objects.aggregate(Count('name'))['name__count'])

print(Person.objects.filter(Q(salary__gte=3000) & Q(salary__lte=5000)))

# print(Person.objects.filter(salary=F(Avg('salary'))))

people = Person.objects.annotate(person_count=Count('name'))
for p in people:
    print(p, p.person_count) # Isso imprime o nome da pessoa e o número de vezes que aquele nome 
                             # aparece no banco de dados (porque estamos contando o campo name).

