from rest_framework import serializers
from .models import Osoba, Team, Person, Stanowisko
import datetime

class StanowiskoSerializer(serializers.Serializer):
    nazwa = serializers.CharField(required=True)
    opis = serializers.CharField(default='', allow_null=True, allow_blank=True)

    def create(self, validated_data):
        return Stanowisko.objects.create(**validated_data)

    def update(instance, validated_data):
        instance.nazwa = validated_data.get('nazwa', instance.nazwa)
        instance.opis = validated_data.get('opis', instance.opis)
        instance.save()
        return instance

class OsobaSerializer(serializers.ModelSerializer):
    def validate_name(self, value):
        if value.isdigit():
            raise serializers.ValidationError(
                "Nazwa osoby nie może zawierać cyfr!"
            )
        return value

    def validate_miesiac_dodania(self, value):
        if value > datetime.date.today().month:
            raise serializers.ValidationError(
                "Miesiąc nie może być z przyszłości!"
            )
        return value

    def update(self, instance, validated_data):
        instance.imie = validated_data.get('imie', instance.imie)
        instance.nazwisko = validated_data.get('nazwisko', instance.nazwisko)
        instance.plec = validated_data.get('plec', instance.plec)
        instance.stanowisko = validated_data.get('stanowisko', instance.stanowisko)
        instance.data_dodanie = validated_data.get('data_dodania', instance.data_dodania)
        instance.miesiac_dodania = validated_data.get('miesiac_dodania', instance.miesiac_dodania)
        instance.slug = validated_data.get('slug', instance.slug)
        instance.save()
        return instance

    def get_miesiac_dodania(self, obj):
        return obj.miesiac_dodania.month

    class Meta:
        model = Osoba
        fields = ['id', 'imie', 'nazwisko', 'plec', 'stanowisko', 'slug']
        read_only_fields = ['id']


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'
        read_only_fields = ['id']

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'
        read_only_fields = ['id']