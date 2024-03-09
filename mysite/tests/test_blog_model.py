from django.test import TestCase
from datetime import datetime

from post.models import posttest, Category
from account.models import User , Profile

class Testpost(TestCase):

    def setUp(self):
        self.user= User.objects.create_user(
            email = 'user@test.com',
            password = '1@example.com'
            )
        self.profile= Profile.objects.create(
            user=self.user,
            first_name = 'first_name_test',
            last_name = 'last_name_test',

        )
        self.category = Category.objects.create(name='Test Category')

    def test_create_post_with_valid_data(self):
        user= User.objects.create_user(
            email = 'user@example.com',
            password = '1@example.com'
            )
        post = posttest.objects.create(
            author = user,
            titel = 'title_test',
            content ='content_test',
            status = True,
            published_date= datetime.now(),

        )
        post.category.set([self.category])
        self.assertEqual(post.titel, 'title_test')

