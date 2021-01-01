from django.shortcuts import render
from rest_framework import generics
from .models import Cryptocurrency
from .serializers import CryptocurrencySerializer
import requests

class ListCryptocurrencyView(generics.ListAPIView):
    queryset = Cryptocurrency.objects.all()
    serializer_class = CryptocurrencySerializer

def HomeView(request):
    url = 'http://127.0.0.1:8000/api/'
    data = requests.get(url).json()
    context = {'data': data}

    return render(request, 'CryptoAPI/main.html', context)