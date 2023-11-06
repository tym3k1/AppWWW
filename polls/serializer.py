from rest_framework import serializers
from .models import Stanowisko, Osoba
import datetime

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

    def validate_miesiac_dodania(self, value):
        if value > datetime.date.today().month:
            raise serializers.ValidationError(
                "Miesiomc nie mosze bydz z pszyszlosci!",
            )
        return value

    class Meta:
        model = Osoba
        fields = '__all__'