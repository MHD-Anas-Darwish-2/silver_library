from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin

# Register your models here.

admin.site.register(MyUser, UserAdmin)
admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Metaphor)
admin.site.register(Category)
admin.site.register(Customer)