from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Category, Channel, Server

# Create your tests here.


def create_user():
    return get_user_model().objects.create_user(username="testuser", password="12345")


def create_category():
    return Category.objects.create(
        name="category_name", description="category_description"
    )


def create_server(user, category):
    return Server.objects.create(
        name="server_name",
        owner=user,
        category=category,
        description="server_description",
    )


def create_channel(user, server):
    return Channel.objects.create(
        name="channel_name", owner=user, topic="channel_topic", server=server
    )


class CategoryTestCase(TestCase):
    """
    Category Test Case
    """

    def setUp(self):
        """
        Setting Up Category
        """
        cat1 = create_category()

    def test_create_category(self):
        """
        Test Creating Category
        """
        cat1 = Category.objects.get(pk=1)
        self.assertTrue(isinstance(cat1, Category))
        self.assertEqual(cat1.name, "category_name")
        self.assertEqual(cat1.description, "category_description")


class ServerTest(TestCase):
    """
    Server Test Case
    """

    def setUp(self):
        """
        Setting Up Server
        """
        user = create_user()
        cat1 = create_category()
        ser1 = create_server(user, cat1)
        ser1.members.add(user)

    def test_create_server(self):
        """
        Test Creating Server
        """
        ser1 = Server.objects.get(pk=1)
        self.assertTrue(isinstance(ser1, Server))
        self.assertEqual(ser1.name, "server_name")
        self.assertEqual(ser1.description, "server_description")


class ChannelTest(TestCase):
    """
    Channel Test Case
    """

    def setUp(self):
        """
        Setting Up Channel
        """
        self.user = create_user()
        cat1 = create_category()
        ser1 = create_server(self.user, cat1)
        ser1.members.add(self.user)
        ch1 = create_channel(self.user, ser1)

    def test_create_channel(self):
        """
        Test Creating Channel
        """
        ch1 = Channel.objects.get(pk=1)
        self.assertTrue(isinstance, Channel)
        self.assertEqual(ch1.name, "channel_name")
        self.assertEqual(ch1.owner, self.user)
