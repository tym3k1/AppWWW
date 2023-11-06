
>>> from polls.models import Osoba,Stanowisko
>>> from polls.serializer import StanowiskoSerializer, osobaSerializer  
>>> from rest_framework.renderers import JSONRenderer
>>> from rest_framework.parsers import JSONParser 
>>> osoba = Osoba(imie='Adam', nazwisko='Nawalka', plec=1, stanowisko_id=1)
>>> osoba.save()                                                            
>>> serializer = osobaSerializer(osoba) 
>>> serializer.data
{'id': 4, 'imie': 'Adam', 'nazwisko': 'Nawalka', 'plec': 1, 'data_dodania': '2023-10-30T13:31:09.534308+01:00', 
'stanowisko': 1}
>>> content = JSONRenderer().render(serializer.data)
>>> content
b'{"id":4,"imie":"Adam","nazwisko":"Nawalka","plec":1,"data_dodania":"2023-10-30T13:31:09.534308+01:00","stanowi
sko":1}'
>>> stanowisko = Stanowisko(nazwa='piekarz')                               
>>> stanowisko.save()
>>> serializerS = StanowiskoSerializer(stanowisko) 
>>> serializerS.data
{'nazwa': 'piekarz', 'opis': None}
>>> contentS = JSONRenderer().render(serializerS.data)
>>> contentS
b'{"nazwa":"piekarz","opis":null}'
>>>
