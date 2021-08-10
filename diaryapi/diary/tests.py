from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase
import json
from .models import Diary

# Create your tests here.
class DraftAPITest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.base_url="localhost:8000/api/"

    def setUp(self):
        title="contact"
        content="Idris 08169725751"
        contact=Diary(title=title, content=content)
        contact.save()

    def test_initial_diarydata_count_is_one(self):
        self.assertEqual(Diary.objects.count(),1)

    
    def test_post_diary_status_code_201(self):
        data={
                "title":"Address",
                "content":"Alagbaa Compound Ogbomoso",
                }
        url=reverse('diary-list')
        response=self.client.post(url,data)
        self.assertEqual(response.status_code,201)

    def test_update_diary_data_successful(self):
        data={
                "title":"contact",
                "content":"Idris 08169725751 \
                Alagbaa Compound Ogbomoso,Oyo State",
                }
        url=reverse('diary-list') + 'contact/'
        response=self.client.put(url,data)
        self.assertEqual(response.status_code,200)
        
        # try to check if update successful
        detail=Diary.objects.get(title="contact")
        content=detail.content
        self.assertIn("Alagbaa",content)

    def test_delete_diary_data_successfull(self):
        # url of "contact diary data"
        url = reverse('diary-list') + 'contact/'
        response=self.client.delete(url)
        self.assertEqual(response.status_code, 204)


        #doube check from the database
        #the diary data count should be zero
        # since we deleted the only data in it

        count=Diary.objects.count()
        self.assertEqual(count,0)



