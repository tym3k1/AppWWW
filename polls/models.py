import datetime
from django.db import models
from django.utils import timezone


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    signature_text = models.CharField(max_length=200,default="user")
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text
    
# kod z oficjalnej dokumentacji Django
class Person(models.Model):
    # lista wartości do wyboru w formie krotek
    SHIRT_SIZES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )
    name = models.CharField(max_length=60)
    # wskazanie listy poprzez przypisanie do parametru choices
    shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZES)


class Stanowisko(models.Model):
    nazwa = models.CharField(max_length=100, blank=False, null=False)
    stanowisko = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.nazwa}'

class Osoba(models.Model):
    PLEC = (
        ('F', 'Female'),
        ('M', 'Male'),
        ('H', 'HelikopterSzturmowy'),
    )
    imie = models.CharField(max_length=60, blank=False, null=False)
    nazwisko = models.CharField(max_length=60, blank=False, null=False)
    plec = models.CharField(max_length=1, choices=PLEC)
    stanowisko = models.ForeignKey(Stanowisko, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.imie} {self.nazwisko}'

