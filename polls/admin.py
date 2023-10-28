from django.contrib import admin

from .models import Question, Choice, Person, Stanowisko, Osoba

admin.site.register(Question)
admin.site.register(Choice)

class PersonAdmin(admin.ModelAdmin):
    # zmienna list_display przechowuje listę pól, które mają się wyświetlać w widoku listy danego modelu w panelu administracynym
    list_display = ('imie', 'nazwisko', 'plec', 'data_dodania','view_stanowisko_id')
    filter_list = ('plec')
    
    @admin.display(empty_value="???")
    def view_stanowisko_id(self, obj):
        return f'{obj.stanowisko.nazwa} ({obj.stanowisko.id})'
# ten obiekt też trzeba zarejestrować w module admin
admin.site.register(Osoba, PersonAdmin)

admin.site.register(Person)
admin.site.register(Stanowisko)
