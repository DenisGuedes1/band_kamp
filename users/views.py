from rest_framework.views import APIView, Request, Response, status
from .models import User
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializer import UserSerializer
from django.shortcuts import get_object_or_404
from .permissions import IsAccountOwner
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView



class UserView(CreateAPIView):
        queryset = User.objects.all()
        serializer_class = UserSerializer

class UserDetailView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAccountOwner]
    queryser = User.objects.all()
    serializer_class = UserSerializer
    def get_queryset(self):
          return User.objects.all()
          

