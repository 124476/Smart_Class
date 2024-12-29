from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from apps.class_work.models import Work, Computer

User = get_user_model()

class WorkAndComputerViewsTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(username="testuser", password="password")
        cls.other_user = User.objects.create_user(username="otheruser", password="password")

        cls.work = Work.objects.create(name="Класс 1", user=cls.user)
        cls.computer = Computer.objects.create(name="Компьютер 1", work=cls.work)

    def setUp(self):
        self.client.login(username="testuser", password="password")

    def test_work_list_view(self):
        response = self.client.get(reverse("class_work:list"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "class_work/work_list.html")
        self.assertContains(response, "Класс 1")

    def test_work_create_view(self):
        response = self.client.post(reverse("class_work:work_create"), {"name": "Класс 2"})
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Work.objects.filter(name="Класс 2", user=self.user).exists())

    def test_work_update_view(self):
        response = self.client.post(reverse("class_work:work_update", args=[self.work.id]), {"name": "Класс 1 Обновлен"})
        self.assertEqual(response.status_code, 302)
        self.work.refresh_from_db()
        self.assertEqual(self.work.name, "Класс 1 Обновлен")

    def test_work_delete_view(self):
        response = self.client.post(reverse("class_work:work_delete", args=[self.work.id]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Work.objects.filter(id=self.work.id).exists())

    def test_computer_create_view(self):
        response = self.client.post(reverse("class_work:computer_create"), {"name": "Компьютер 2", "work": self.work.id})
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Computer.objects.filter(name="Компьютер 2", work=self.work).exists())

    def test_computer_update_view(self):
        response = self.client.post(reverse("class_work:computer_update", args=[self.computer.id]), {"name": "Компьютер 1 Обновлен", "work": self.work.id})
        self.assertEqual(response.status_code, 302)
        self.computer.refresh_from_db()
        self.assertEqual(self.computer.name, "Компьютер 1 Обновлен")

    def test_computer_delete_view(self):
        response = self.client.post(reverse("class_work:computer_delete", args=[self.computer.id]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Computer.objects.filter(id=self.computer.id).exists())

    def test_computer_control_toggle_power(self):
        response = self.client.post(
            reverse("class_work:computer_control", args=[self.computer.id]),
            {"action": "toggle_power"}
        )
        self.assertEqual(response.status_code, 302)
        self.computer.refresh_from_db()
        self.assertFalse(self.computer.is_active)

    def test_computer_control_toggle_signal(self):
        response = self.client.post(
            reverse("class_work:computer_control", args=[self.computer.id]),
            {"action": "toggle_signal"}
        )
        self.assertEqual(response.status_code, 302)
        self.computer.refresh_from_db()
        self.assertTrue(self.computer.signal)

    def test_unauthorized_access(self):
        self.client.logout()
        response = self.client.get(reverse("class_work:list"))
        self.assertNotEqual(response.status_code, 200)
        self.assertRedirects(response, f"{reverse('users:login')}?next={reverse('class_work:list')}")
