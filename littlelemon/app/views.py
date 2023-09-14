from django.shortcuts import render
from .serializers import MenuSerializer, BookingSerializer
from rest_framework import generics
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .models import menu, booking
# Create your views here.


def index(request):
    return render(request, 'index.html')


class MenuItemView(generics.ListCreateAPIView):
    serializer_class = MenuSerializer
    queryset = menu.objects.all()


class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MenuSerializer
    queryset = menu.objects.all()


class BookingViewSet(ModelViewSet):
    serializer_class = BookingSerializer
    queryset = booking.objects.all()
    permission_classes = [IsAuthenticated]
