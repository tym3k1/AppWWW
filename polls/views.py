from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status, generics
from .models import Osoba, Stanowisko
from .serializer import osobaSerializer, StanowiskoSerializer

class RetrieveOsobaView(generics.RetrieveAPIView):
    queryset = Osoba.objects.all()
    serializer_class = osobaSerializer

class CreateOsobaView(generics.CreateAPIView):
    queryset = Osoba.objects.all()
    serializer_class = osobaSerializer

class DestroyOsobaView(generics.DestroyAPIView):
    queryset = Osoba.objects.all()
    serializer_class = osobaSerializer

class FilterOsobaView(generics.ListAPIView):
    queryset = Osoba.objects.all()
    serializer_class = osobaSerializer

    def get_queryset(self):
        search_param = self.request.query_params.get('search', None)
        if search_param:
            # Filtruj obiekty Osoba, które zawierają dany łańcuch znaków w polu 'nazwa'
            queryset = self.queryset.filter(imie__icontains=search_param)
        else:
            queryset = self.queryset  # Jeśli nie podano parametru 'search', zwróć wszystkie obiekty Osoba
        return queryset

@api_view(['GET', 'POST'])
def osoba_list(request):
    if request.method == 'GET':
        persons = Osoba.objects.all()
        serializer = osobaSerializer(persons, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = osobaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def osoba_detail(request, pk):
    try:
        person = Osoba.objects.get(pk=pk)
    except Osoba.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = osobaSerializer(person)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = osobaSerializer(person, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        person.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

@api_view(['GET', 'POST'])
def osoba_list_filter(request):
    if request.method == 'GET':
        search_param = request.query_params.get('search', None)

        if search_param:
            persons = Osoba.objects.filter(imie__icontains=search_param)
        else:
            persons = Osoba.objects.all()

        serializer = osobaSerializer(persons, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = osobaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET', 'POST'])
def stanowisko_list(request):
    if request.method == 'GET':
        stanowisko = Stanowisko.objects.all()
        serializer = StanowiskoSerializer(stanowisko, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = StanowiskoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])   
def stanowisko_detail(request, pk):
    try:
        stanowisko = Stanowisko.objects.get(pk=pk)
        serializer = StanowiskoSerializer(stanowisko)
        return Response(serializer.data)
    except Stanowisko.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
@api_view(['POST'])
def stanowisko_create(request):
    serializer = StanowiskoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def stanowisko_delete(request, pk):
    try:
        stanowisko = Stanowisko.objects.get(pk=pk)
        stanowisko.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except Stanowisko.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
class RetrieveStanowiskoView(generics.RetrieveAPIView):
    queryset = Stanowisko.objects.all()
    serializer_class = StanowiskoSerializer

class CreateStanowiskoView(generics.CreateAPIView):
    queryset = Stanowisko.objects.all()
    serializer_class = StanowiskoSerializer

class DestroyStanowiskoView(generics.DestroyAPIView):
    queryset = Stanowisko.objects.all()
    serializer_class = StanowiskoSerializer
