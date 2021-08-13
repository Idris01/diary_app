from django.shortcuts import render, get_object_or_404
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Diary, User
from .serializers import DiarySerializer,UserSerializer, DiaryCreateSerializer


# Create your views here.
class DiaryListCreateView(APIView):
    def get(self,request,**kwargs):
        key=kwargs["key"]
        queryset=Diary.objects.filter(diary_key=key)
        serializer=DiarySerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self,request,**kwargs):
        diary_key=kwargs["key"]
        data={
                "title":request.data.get("title"),
                "content":request.data.get("content")
                }
        data.update({"diary_key":diary_key})
        #title=self.data.get("title")
        #content=self.data.get("content")
        serializer=DiaryCreateSerializer(data=data)
        
        if serializer.is_valid():
            diary=serializer.save()
            return Response({"msg":"Diary saved"})
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DiaryGetDestroyUpdateView(APIView):
    
    def get(self, request, **kwargs):
        diary_key=kwargs["key"]
        diary_id=kwargs["id"]
        
        try:
            diary=Diary.objects.get(diary_key=diary_key, id=diary_id)
            serialize=DiarySerializer(diary)

            return Response(serialize.data, status=200)
        except Diary.DoesNotExist:
            return Response({"msg":"No content found"}, status=status.HTTP_404_NOT_FOUND)


    def put(self, request, **kwargs):
        diary_key=kwargs["key"]
        diary_id=kwargs["id"]
        
        try:
            diary=Diary.objects.get(diary_key=diary_key, id=diary_id)

            serialize=DiarySerializer(instance=diary, data=request.data)
            if serialize.is_valid():
                serialize.save()

            else:
                return Response({"msg":"Unable to Update diary"}, status=status.HTTP_404_NOT_FOUND)



            return Response({"msg":"Diary Content Updated"}, status=200)

        except Diary.DoesNotExist:
            return Response({"msg":"Unable to Update diary"}, status=status.HTTP_404_NOT_FOUND)




    def delete(self, request, **kwargs):
        diary_key=kwargs["key"]
        diary_id=kwargs["id"]
        
        try:
            diary=Diary.objects.get(diary_key=diary_key, id=diary_id)
            diary.delete()
            return Response({"msg":"Content Deleted"}, status=status.HTTP_204_NO_CONTENT)
        except Diary.DoesNotExist:
            return Response({"msg":"Error"}, status=status.HTTP_404_NOT_FOUND)




class UserView(APIView):
    def post(self,request):
        serializer=UserSerializer(data=request.data)

        # check if the data is valid
        if serializer.is_valid():
            user=serializer.save()
            data={"key":user.key}
            return Response(data)

        elif len(request.data) == 2:
            # get the user's key
            username=request.data.get('username')
            password=request.data.get('password')

            if username == None or password==None:
                return Response({"msg": "Invalid input"},status=400)

            user=User.objects.get(username=username, password=password)
                
            data={"key":user.key}
            return Response(data)

        else:
            return Response({"msg": "Invalid input"},status=400)



