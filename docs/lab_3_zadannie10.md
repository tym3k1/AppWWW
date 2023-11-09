ex.1
>>> from polls.models import Osoba
>>> Osoba.objects.all()
ex.2
>>> Osoba.objects.filter(id=1)
ex.3
>>> Osoba.objects.filter(nazwisko__startswith="J") 
ex.4
>>> Osoba.objects.values('stanowisko').distinct()
>>> Osoba.objects.values_list('stanowisko', flat=True).distinct()
ex.4
>>> Osoba.objects.values('stanowisko__nazwa').order_by('-stanowisko__nazwa') 
ex.5
ValueError: save() prohibited to prevent data loss due to unsaved related object 'stanowisko'.
>>> n_stanowisko = Stanowisko(nazwa='trener', opis='')
>>> n_stanowisko.save()
>>> nowa_osoba = Osoba(imie="Jacek", nazwisko="Magiera", plec=1, stanowisko=n_stanowisko)  
>>> nowa_osoba.save()  