from rest_framework import serializers
from .models import Stanowisko, Osoba
import datetime
import pandas as pd

class StanowiskoSerializer(serializers.Serializer):
    nazwa = serializers.CharField(
        required=True
    )
    opis = serializers.CharField(
        default=''
    )

    def create(self, validated_data):
        return Stanowisko.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.nazwa = validated_data.get('nazwa', instance.name)
        instance.opis = validated_data.get('opis', instance.shirt_size)
        instance.save()
        return instance

class osobaSerializer(serializers.ModelSerializer):
    def validate_imie(self, value):
        if not value.isalpha():
            raise serializers.ValidationError(
                "Nazwa osoby powinna zawierac tylko literki!",
            )
        return value

    def validate_data_dodania(self, value):
        if value > datetime.date.today():
            raise serializers.ValidationError(
                "Miesiomc nie mosze bydz z pszyszlosci!",
            )
        return value
    
    def create(self, validated_data):
        return Osoba.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.imie = validated_data.get('imie', instance.imie)
        instance.nazwisko = validated_data.get('nazwisko', instance.nazwisko)
        instance.plec = validated_data.get('plec', instance.plec)
        instance.stanowisko = validated_data.get('stanowisko', instance.stanowisko)
        instance.data_dodanie = validated_data.get('data_dodania', instance.data_dodania)
        instance.save()
        return instance

    class Meta:
        model = Osoba
        fields = '__all__'
        read_only_fields = ['id']