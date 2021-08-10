from rest_framework.serializers import ModelSerializer
from .models import Diary

class DiarySerializer(ModelSerializer):
    class Meta:
        model=Diary
        fields=("title", "content", "created_on")

