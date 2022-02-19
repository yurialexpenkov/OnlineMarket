from django.contrib.auth.models import User
from django.test import TestCase



class UsersTest(TestCase):


    def test_register_user(self):
        data = {
            'username': 'TestIvan',
            'first_name': 'Yuri',
            'last_name': 'last_name',
            'password1': '4ABefef3rgVM',
            'password2': '4ABefef3rgVM',
        }

        response = self.client.post('/users/register/', data)
        user = User.objects.get(username=data['username'])
        self.assertIsInstance(user, User)

