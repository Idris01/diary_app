from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Diary, User
from .serializers import DiarySerializer,UserSerializer


# Create your views here.
class DiaryView(ModelViewSet):
    def get_queryset(self):
        key=self.kwargs["key"]
        queryset=Diary.objects.filter(diary_key=key)
        return queryset
    serializer_class=DiarySerializer


class UserView(APIView):
    def post(self,request):
        serializer=UserSerializer(data=request.data)

        # check if the data is valid
        if serializer.is_valid():
            
            try:
                # get the user's key
                username=request.data.get('username')
                password=request.data.get('password')

                user=User.objects.get(username=username, password=password)
                
                data={"key":user.key}
                return Response(data)

            except User.DoesNotExist:

                user=serializer.save()
                data={"key":user.key}
                return Response(data)



