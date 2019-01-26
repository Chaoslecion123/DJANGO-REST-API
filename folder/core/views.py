from rest_framework import generics
from core.models import portafolio
from core.serializers import portafolioSerializer, UserSerializer
from django.contrib.auth.models import User
from rest_framework import viewsets # el viewserts te crea el put , el post , get , patch ,etc
from rest_framework.authentication import TokenAuthentication

# Create your views here.

#IMPORT PERMISOS
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly

class portafolioList(generics.ListCreateAPIView):
    queryset = portafolio.objects.all()
    serializer_class = portafolioSerializer
    permission_classes = [IsAuthenticated]

class portafolioDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = portafolio.objects.all()
    serializer_class = portafolioSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [AllowAny]
    # authentication_classes = [TokenAuthentication]
