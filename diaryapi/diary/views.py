from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Diary
from .serializers import DiarySerializer

# Create your views here.
class DiaryView(ModelViewSet):
    serializer_class=DiarySerializer
    queryset=Diary.objects.all()

