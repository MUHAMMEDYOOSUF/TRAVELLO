from django.contrib import admin

# Register your models here.
from travelloapp.models import place, team

admin.site.register(place)
admin.site.register(team)
