from django.contrib import admin
from .models import Question, Choice, Person
# Register your models here.

admin.site.register(Question)

class PersonAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "SoSec_number",)

admin.site.register(Person, PersonAdmin)