from django.contrib import admin

from .models import Question, Choice, Person, Stanowisko, Osoba

admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Person)
admin.site.register(Stanowisko)
admin.site.register(Osoba)