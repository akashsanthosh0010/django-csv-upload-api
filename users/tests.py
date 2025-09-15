from django.test import TestCase
from rest_framework.test import APIClient
from django.core.files.uploadedfile import SimpleUploadedFile
import json

# Create your tests here.

class UploadCSVTest(TestCase):
    def setup(self):
        self.client = APIClient

    def test_is_valid(self):
        csv_content = b"name,email,age\nakash,akash@abx.com,13\nanoop,anoop@yxz.com,21\n"
        file = SimpleUploadedFile("test.csv", csv_content, content_type = "text/csv")
        res = self.client.post('/users-api/upload-csv/', {"file": file}, format='multipart')
        self.assertEqual(res.status_code, 200)
        res_json = json.loads(res.content) 
        self.assertEqual(res_json['saved_records'], 2)
        
