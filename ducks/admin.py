from django.contrib import admin
from .models import Duck

class AdminDuck(admin.ModelAdmin):
    list_display = ('title', 'price', 'purchaser', 'timestamp', 'updated')

admin.site.register(Duck, AdminDuck)