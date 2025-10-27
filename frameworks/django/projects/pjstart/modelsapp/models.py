from django.db import models
from .validators import validate_gender, validate_birthday_to_register, validate_salary, validate_email
from django.db.models.constraints import CheckConstraint, UniqueConstraint
from django.core.validators import RegexValidator
from django.urls import reverse
from datetime import date

from django.db.models import Max, Min, Avg, Count, Q, F

class PersonQuerySet(models.QuerySet):
    def with_pk(self, pk):
        return self.filter(id=pk)
    
    def with_name(self, name):
        return self.filter(name__istartswith=name)

    def with_salary_above(self, salary):
        return self.filter(salary__gte=salary)

    def with_salary_under(self, salary):
        return self.filter(salary__lte=salary)
    
    def with_max_salary(self):
        max_salary = self.model.objects.aggregate(Max('salary'))['salary__max']
        if max_salary is None:
            return self.none()
        return self.filter(salary=max_salary)
    
    def with_min_salary(self):
        min_salary = self.model.objects.aggregate(Min('salary'))['salary__min']
        if min_salary is None:
            return self.none()
        return self.filter(salary=min_salary)
    
    def with_salary_above_avg(self):
        avg_salary = self.model.objects.aggregate(Avg('salary'))['salary__avg']
        if avg_salary is None:
            return self.none()
        return self.filter(salary__gte=avg_salary)

    def with_salary_under_avg(self):
        avg_salary = self.model.objects.aggregate(Avg('salary'))['salary__avg']
        if avg_salary is None:
            return self.none()
        return self.filter(salary__lte=avg_salary)

class PersonAdminManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=True)

class PersonManager(models.Manager):
    def get_queryset(self): # substitui o all()
        # return super().get_queryset().none()
        # return super().get_queryset().filter(name__icontains='') # so para ilustrar!
        return PersonQuerySet(self.model, self._db) # para poder usar o PersonQuerySet
    
    def with_name(self, name):
        return self.get_queryset().with_name(name)
    
    # .... definir todos os metodos do queryset aqui para uso
    
class Person(models.Model):
    manager = PersonManager()
    admin = PersonAdminManager()

    fixture = ['people']

    queryset = PersonQuerySet.as_manager() # nao deve ser instanciado diretamente, porem, usado como manager.

    GENDER = [
        ('M','Male'),
        ('F','Female'),
        ('O','Others')
    ]
    name = models.CharField(max_length=50, null=False, error_messages={'blank': 'Name is empty.', 'null': 'Name is empty.'})
    gender = models.CharField(max_length=1, validators=[validate_gender], null=False, choices=GENDER)
    birthday = models.DateField(validators=[validate_birthday_to_register], null=False)
    email = models.EmailField(max_length=50, null=False, unique=True, validators=[RegexValidator(regex=r'^[\w\.-]+@[\w\.-]+\.\w+$', message='Invalid E-mail.')], error_messages={'unique':'E-mail already registered.'})
    salary = models.DecimalField(max_digits=10, decimal_places=2, null=False, validators=[validate_salary])
    status = models.BooleanField(null=False)

    class Meta:
        db_table = 'person'
        managed = True
        
        constraints = [
            models.UniqueConstraint(fields=['email'], name="unq_person_email"),
            models.CheckConstraint(check=models.Q(gender__in=['M','F','O']), name="chk_person_gender"),
            # models.CheckConstraint(check=models.expressions.RawSQL(r'^[\w\.-]+@[\w\.-]+\.\w+$', []), name="chk_email_person"),
            models.CheckConstraint(check=models.Q(salary__gte=1) & models.Q(salary__lte=9999999999), name="chk_person_salary"),
            models.CheckConstraint(check=models.Q(status=True) | models.Q(status=False), name='chk_person_status')
        ]

    def __str__(self):
        return f"{self.pk} - {self.name}"
    
    def get_absolute_url(self):
        return reverse('person-details', kwargs={'pk': self.pk})
    
    def save(self, *args, **kwargs):
        self.full_clean() # ja chama os validators aqui.
        super(Person, self).save(*args, **kwargs)

class MyPerson(Person):
    class Meta:
        proxy = True
        ordering = ['name']
        verbose_name = 'person'
        verbose_name_plural = 'people'

class Car(models.Model):
    CARS = [
        ("Corolla", "Corolla"),
        ("Camry", "Camry"),
        ("RAV4", "RAV4"),
        ("Hilux", "Hilux"),
        ("Civic", "Civic"),
        ("Accord", "Accord"),
        ("CR-V", "CR-V"),
        ("Fit", "Fit"),
        ("Fiesta", "Fiesta"),
        ("Focus", "Focus"),
        ("Mustang", "Mustang"),
        ("Explorer", "Explorer"),
        ("Onix", "Onix"),
        ("Cruze", "Cruze"),
        ("Malibu", "Malibu"),
        ("Tracker", "Tracker"),
        ("Gol", "Gol"),
        ("Polo", "Polo"),
        ("Golf", "Golf"),
        ("Tiguan", "Tiguan"),
        ("Série 3", "Série 3"),
        ("Série 5", "Série 5"),
        ("X3", "X3"),
        ("X5", "X5"),
        ("Classe A", "Classe A"),
        ("Classe C", "Classe C"),
        ("Classe E", "Classe E"),
        ("GLE", "GLE"),
        ("A3", "A3"),
        ("A4", "A4"),
        ("Q5", "Q5"),
        ("Q7", "Q7"),
        ("HB20", "HB20"),
        ("Creta", "Creta"),
        ("Tucson", "Tucson"),
        ("Elantra", "Elantra"),
        ("Sentra", "Sentra"),
        ("Altima", "Altima"),
        ("Kicks", "Kicks"),
        ("Frontier", "Frontier"),
    ]

    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    model = models.CharField(max_length=20, choices=CARS, null=False)

    def __str__(self):
        return f"{self.model} owned by {self.person.name}"

class Address(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    address = models.JSONField(null=True)

    def __str__(self):
        return self.address

# ----------------------- #
    
class Product(models.Model):
    name = models.CharField(null=False)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=False)    

    class Meta:
        db_table = 'product'
        managed = True
        verbose_name = 'product'
        verbose_name_plural = 'products'

class Sale(models.Model):
    products = models.ManyToManyField(Product)
    date_sale = models.DateTimeField(null=False)

    class Meta:
        db_table = 'sale'
        managed = True
        verbose_name = 'sale'
        verbose_name_plural = 'sales'

class SaleItem(models.Model):
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(null=False)

    class Meta:
        db_table = 'saleitem'
        managed = True
        verbose_name = 'saleitem'
        verbose_name_plural = 'saleitems'

"""
    1. 📦 Criando produtos

        p1 = Product.objects.create(name="Monitor", price=800.00)
        p2 = Product.objects.create(name="Mouse", price=100.00)
        p3 = Product.objects.create(name="Keyboard", price=150.00)

    2. 🧾 Criando uma venda

        sale = Sale.objects.create(date_sale=timezone.now())

    3. ➕ Adicionando produtos à venda com quantidade (via SaleItem)

        SaleItem.objects.create(sale=sale, product=p1, quantity=2)  # 2 Monitores
        SaleItem.objects.create(sale=sale, product=p2, quantity=1)  # 1 Mouse
        SaleItem.objects.create(sale=sale, product=p3, quantity=3)  # 3 Keyboards

"""

# ------------------------------------------------


