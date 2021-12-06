from .views import SnackListView , SnackDetailView
from django.urls import path

urlpatterns=[
    path('', SnackListView.as_view(), name='SnackList'),
    path('<int:pk>', SnackDetailView.as_view(), name='SnackDetail')
]