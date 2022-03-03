from rest_framework import generics
from .serializers import *
from .models import *
from .permissions import *
from rest_framework.views import APIView
from django.http import JsonResponse
class CompanyView(generics.ListCreateAPIView):
    serializer_class = FirmSerializer
    queryset = CompanyModel.objects.all()
    permission_classes = [IsOwner]
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_queryset(self):
        if self.request.user.is_superuser:
            owner_queryset = self.queryset.all()
        else:
            owner_queryset = self.queryset.filter(author=self.request.user)
        return owner_queryset

class CompanyDetailView(APIView):
    permission_classes = [IsOwner]
    def get(self, request, *args, **kwargs):
        id = kwargs['id']
        company = list(CompanyModel.objects.filter(id=id).values())
        users = list(UsersModel.objects.filter(company=company[0]['id']).values())
        return JsonResponse({
            'company':company,
            'users':users,
            })

class UserView(generics.ListCreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsOwner]
    queryset = UsersModel.objects.all()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_queryset(self):
        if self.request.user.is_superuser:
            owner_queryset = self.queryset.all()
        else:
            owner_queryset = self.queryset.filter(author=self.request.user)
        return owner_queryset


class CompanyEditView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = FirmSerializer
    permission_classes = [IsOwner]
    queryset = CompanyModel.objects.all()

class UserEditView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsOwner]
    queryset = UsersModel.objects.all()


class CreateUserView(generics.CreateAPIView):

    model = get_user_model()
    permission_classes = [IsSuperUser]
    serializer_class = UserRegisterSerializer