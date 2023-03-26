from fastapi.testclient import TestClient
from unittest import TestCase
from main import app


class endpoint_test(TestCase):


    def setUp(self) -> None:
        self.client = TestClient(app)

    def test_ep1(self):
        response = self.client.get("/")

        assert response.status_code==200
        assert response.text=='"hello world"'


    def test_ep2(self):
        response = self.client.get("/part_1")

        assert response.status_code==200
        assert response.text=='"Yo boys1"'

    def test_ep3(self):
        response = self.client.get("/part_2")

        assert response.status_code==200
        assert response.text=='"hi boys"'


