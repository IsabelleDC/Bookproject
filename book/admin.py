from django.contrib import admin
from book.models import Livre, Visitor, Genre

# Register your models here.
admin.site.register(Livre)
admin.site.register(Genre)
admin.site.register(Visitor)
