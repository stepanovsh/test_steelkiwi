"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from django.test import Client
from django.contrib.auth.models import User
from .models import Student
from group.models import Group

class SimpleTest(TestCase):
    testGroup = dict(name = 'SP-03n')

    testStudent = dict(surname='Ivanov', name='Viktor', father = 'Viktorovich',
                       birthday = '1987-02-03', student_card = 'NE234534', group='1')

    username='test'
    password='testpassword'
    email='testemail@test.com'

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(self.username,self.email, self.password)

    def test_login_user(self):

        self.login = self.client.login(username = self.username, password = self.password)
        self.assertEqual(self.login, True)

        self.elogin = self.client.login(username = self.email, password = self.password)
        self.assertEqual(self.elogin, True)


    def test_student_group_add(self):

        self.login = self.client.login(username = self.username, password = self.password)

        response = self.client.post('/group/add/', self.testGroup)
        self.assertEquals(response.status_code, 302)

        group = Group.objects.get(name=self.testGroup['name'])
        self.testStudent['group'] = group.pk

        response = self.client.post('/student/add/', self.testStudent)
        self.assertEquals(response.status_code, 302)

        student = Student.objects.get(student_card = self.testStudent['student_card'])
        self.assertEqual(student.group, group)



