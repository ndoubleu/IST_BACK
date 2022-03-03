
from django.urls import path
from .views import *
urlpatterns = [
    path('', CompanyView.as_view()),
    path('edit/<int:pk>', CompanyEditView.as_view()),
    path('staff/', UserView.as_view()),
    path('staff/<int:pk>', UserEditView.as_view()),
    path('<int:id>/', CompanyDetailView.as_view()),

]
