from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase
from .models import Diary, User

# Create your tests here.
class DiaryTest(APITestCase):
    @classmethod
    def setupTestData(cls):
       ... 
    def setUp(self):
        self.name="Idris"
        self.password="9evergiveup"
        self.account_url=reverse('account')
        self.data={
                "username":self.name,
                "password":self.password
                }



    def test_diary_account_created(self):
        url=self.account_url
        data=self.data
        response=self.client.post(url,data)
        self.assertEqual(response.status_code,200)

    def test_diary_data_created(self):
        # create a new user
        user=User.objects.create_user(username="Yemi",password="1234567")
        user.save()
        key=user.key

        #send a post request to create diary content
        #for the user with the key

        url=(reverse('diary-list',kwargs={'key':key}))
        data={
                "title":"My Dream",
                "content": "My Dream is to Be a pro \
                        by 2021 ending inShaAllah"
                        }

        response=self.client.post(url,data)

        self.assertEqual(response.status_code,200)
    
    def test_lost_key_retrieved(self):
        url=self.account_url
        response=self.client.post(url,self.data)
        
        # get the key from the response
        key1=response.json()["key"]

        # send the same response again to mimic a lost
        # key that the user wants to retrieve
        response=self.client.post(url,self.data)

        key2=response.json()["key"]
        
        self.assertEqual(key1,key2)

    



        

