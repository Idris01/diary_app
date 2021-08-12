from rest_framework.serializers import ModelSerializer
from .models import Diary, User

class DiarySerializer(ModelSerializer):
    class Meta:
        model=Diary
        fields=("title", "content", "created_on")

class UserSerializer(ModelSerializer):
    class Meta:
        model=User
        fields=("username","password")

