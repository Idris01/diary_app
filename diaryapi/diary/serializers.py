from rest_framework.serializers import ModelSerializer
from .models import Diary, User

class DiarySerializer(ModelSerializer):
    class Meta:
        model=Diary
        fields=("id", "title", "content", "created_on")
class DiaryCreateSerializer(ModelSerializer):
    class Meta:
        model=Diary
        fields=("diary_key", "title", "content")

class UserSerializer(ModelSerializer):
    class Meta:
        model=User
        fields=("username","password")

