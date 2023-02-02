from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

# Create your models here.

# المستخدم
class MyUser(AbstractUser):
    class Meta:
        db_table = 'auth_user'

    username = models.CharField(max_length=100, primary_key=True, default=str(uuid.uuid4()), editable=False)
    phone = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.username

class Customer(models.Model):
    username = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200, null=True, blank=True)
    phone = models.CharField(max_length=15, null=True, blank=True)

    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(default='author.svg')

    def __str__(self):
        return self.name

# التصنيف
class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

# الكتاب
class Book(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    category = models.ManyToManyField(Category, blank=True)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    pages = models.PositiveIntegerField(null=True, blank=True)
    image = models.ImageField(default='book.svg')
    metaphors = models.PositiveIntegerField(default=0)
    rateing = models.PositiveSmallIntegerField(null=True, blank=True)
    number_of_books = models.IntegerField(default=1)
    number_of_borrowed_books = models.IntegerField(default=0)

    def __str__(self):
        return self.name

# الاستعارات
class Metaphor(models.Model):
    events = [
        ("metaphor", "metaphor"),
        ("return", "return book")
    ]
    event = models.CharField(max_length=8, choices=events, default="metaphor")
    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL, related_name="customer_metaphor_set")
    employee = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.SET_NULL, related_name="employee_metaphor_set")
    book = models.ForeignKey(Book, null=True, on_delete=models.SET_NULL)
    date_metaphor = models.DateTimeField(auto_now_add=True, null=True)
    borrowed = models.BooleanField(default=True)

    def __str__(self):
        return self.customer.name
