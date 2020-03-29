from django.contrib import admin
from .models import Client
from .models import Contact

# Register your models here.

admin.site.register(Client)
admin.site.register(Contact)

