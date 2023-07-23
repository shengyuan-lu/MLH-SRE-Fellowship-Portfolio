# tests/test_app.py

import unittest
import os
os.environ['TESTING'] = 'True'

from app import app, TimelinePost
class AppTestCase(unittest.TestCase):
    def setUp(self):
        # Bind model classes to test db. Since we have a complete list of
        # all models, we do not need to recursively bind dependencies.
        self.client = app.test_client()
        # Clean up the TimelinePosts before each test
        TimelinePost.delete().execute()

    def test_home(self):
        response = self.client.get("/")
        assert response.status_code == 200
        html = response.get_data(as_text=True)
        assert "<title>Meet MLH Fellows</title>" in html
        assert "Meet MLH Fellows" in html  
        assert "Shengyuan Lu" in html  

    def test_timeline(self):
        response = self.client.get("/api/timeline_post")
        assert response.status_code == 200
        assert response.is_json
        json = response.get_json()
        assert "timeline_posts" in json
        assert len(json["timeline_posts"]) == 0

        new_post = {"name": "John", "email": "john@example.com", "content": "Test Content"}
        post_response = self.client.post("/api/timeline_post", data=new_post)
        assert post_response.status_code == 200  
        response = self.client.get("/api/timeline_post")
        json = response.get_json()
        assert len(json["timeline_posts"]) == 1 

        assert json["timeline_posts"][0]["name"] == "John"  
        assert json["timeline_posts"][0]["email"] == "john@example.com" 
        assert json["timeline_posts"][0]["content"] == "Test Content" 

    def test_malformed_timeline_post(self):
        # POST request with empty name
        response = self.client.post("/api/timeline_post", data={"name": "", "email": "john@example.com", "content": "Hello world, I'm John!"})
        assert response.status_code == 400
        html = response.get_data(as_text=True)
        assert "Invalid name" in html

        # POST request with empty content
        response = self.client.post("/api/timeline_post", data= {"name": "John Doe", "email": "john@example.com", "content": ""}) 
        assert response.status_code == 400
        html = response.get_data(as_text=True)
        assert "Invalid content" in html

        # POST request with no email
        response = self.client.post("/api/timeline_post", data= {"name": "John Doe", "email": "", "content": "Hello world, I'm John!"})
        assert response.status_code == 400
        html = response.get_data(as_text=True)
        assert "Invalid email" in html

        # POST request with incorrect email
        response = self.client.post("/api/timeline_post", data= {"name": "John Doe", "email": "not-an-email", "content": "Hello world, I'm John!"})
        assert response.status_code == 400
        html = response.get_data(as_text=True)
        assert "Invalid email" in html