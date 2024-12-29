from rest_framework import status
from rest_framework.test import APITestCase
from apps.class_work.models import Work, Computer


class WorkAPITestCase(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.work1 = Work.objects.create(name="Класс 1")
        cls.work2 = Work.objects.create(name="Класс 2")

    def test_get_work_list(self):
        response = self.client.get("/api/works/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]['name'], self.work1.name)

    def test_get_work_detail(self):
        response = self.client.get(f"/api/works/{self.work1.id}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.work1.name)


class ComputerAPITestCase(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.work = Work.objects.create(name="Класс 1")
        cls.computer1 = Computer.objects.create(name="Компьютер 1",
            uuid="123e4567-e89b-12d3-a456-426614174000", work=cls.work)
        cls.computer2 = Computer.objects.create(name="Компьютер 2",
            uuid="432e4567-e89b-34d3-a456-426614174000", work=cls.work)

    def test_get_computer_list(self):
        response = self.client.get("/api/computers/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]['name'], self.computer1.name)

    def test_get_computer_detail(self):
        response = self.client.get(
            f"/api/computers/{self.computer1.id}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.computer1.name)
