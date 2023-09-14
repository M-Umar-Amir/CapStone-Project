from django.test import TestCase
from app import models
from app import serializers


class MenuItemTest(TestCase):
    def test_get_item(self):
        item = models.menu.objects.create(
            id=4, title="IceCream", price=80, inventory=100)
        self.assertEqual(item.title, 'IceCream')
