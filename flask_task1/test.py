import json
from app import app
import unittest
import pytest



class Testing(unittest.TestCase):

    pytest.token=""

    # check for data returned
    def test_get_valid_id(self):
        tester = app.test_client(self)
        response = tester.get("/person/103")
        self.assertTrue(response.data, {"Person_id": 103, "Person_name": "shwetha", "Age": 21,
                                        "Gender": "Female", "email": "shwetha@gmail.com",
                                        "Address": "Mangalore"})

    # check get invalid id
    def test_get_invalid_id(self):
        tester = app.test_client(self)
        response = tester.get("/person/101")
        self.assertTrue(response.data, {"message": "Person id is not available"})


    # check for deleting valid id
    def test_delete_valid_id(self):
        tester = app.test_client(self)
        response = tester.delete("/person/102")
        self.assertTrue(response.data, {"Person_id": "person_id is deleted"})

    # check for deleting invalid delete id
    def test_delete_invalid_id(self):
        tester = app.test_client(self)
        response = tester.delete("/person/101")
        self.assertTrue(response.data, {"message": "Person id is not available"})


    # check for put valid id
    def test_put_valid_id(self):
        data = {
            "Age": 23
        }
        tester = app.test_client(self)
        response = tester.put("/person/103")
        self.assertTrue(response.data, {"Person_id": 103, "Person_name": "shwetha", "Age": 23,
                                        "Gender": "Female", "email": "shwetha@gmail.com",
                                        "Address": "Mangalore"})

    # check for put invalid id
    def test_put_invalid_id(self):
        data = {
            "Person_id": 102
        }
        tester = app.test_client(self)
        response = tester.put("/person/102")
        self.assertTrue(response.data, {"message": "Person id is not available"})

    # check for post method
    def test_post(self):
        data = [{
            "Person_id": 101,
            "Person_name": "chirath",
            "Age": 2,
            "Gender": "Male",
            "email": "chirath@gmail.com",
            "Address": "Bangalore"
        }]
        tester = app.test_client()
        response = tester.post("person/101")
        self.assertTrue(response.status_code, 201)


    # check for authentication
    def test_authentication(self):
        tester = app.test_client(self)
        data1 = {"username": "rashmi", "password": "rashmi123"}
        response = tester.post("/auth", content_type='application/json', data=json.dumps(data1))
        result = response.data.decode('utf-8')
        js = json.loads(result)
        pytest.token = js["access_token"]
        self.assertTrue(True)


if __name__ =='__main__':
    unittest.main()

