from django.test import TestCase
from users.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse

class UserRegisterationAPIViewTestCase(APITestCase):
    def test_registration(self):
        url = reverse("test")
        user_data={
            "username":"testuser",
            "fullname":"테스터",
            "email":"test@test.com",
            "password":"password",
        }
        response= self.client.post(url, user_data)
        print(response.data)
        self.assertEqual(response.data["message"], '가입 완료!!')

# class UserRegisteration(APITestCase):
#     def test_registration(self):
#         url = reverse("user_view")
#         user_data={
#             "username":"testuser",
#             "fullname":"테스터",
#             "email":"test@test.com",
#             "password":"password",
#         }
#         response= self.client.post(url, user_data)
#         self.assertEqual(response.status_code, 200)

#     def test_login(self):
#         url=reverse("token_obtain_pair")
#         user_data={
#             "username":"testuser",
#             "fullname":"테스터",
#             "email":"test@test.com",
#             "password":"password",
#         }
#         response =self.client.post(url, user_data)
#         print(response.data)
#         self.assertEqual("가입완료",response.status_code, 200)

# class LoginUserTest(APITestCase):
#     def setUp(self):
#         self.data={"username":"minsu","password":"123"}
#         self.user= User.objects.create_user("minsu","123")

#     def test_login(self):
#         response = self.client.post(reverse('token_obtain_pair'), self.data)
#         self.assertEqual("가입 완료!!", response.status_code, 200)
        