# tests.py
from django.test import TestCase
from django.urls import reverse
from .models import Order
from decimal import Decimal
from django.contrib.auth.models import User


class OrderTests(TestCase):

    def setUp(self):
        self.order1 = Order.objects.create(
            title="Test Order 1",
            price=Decimal('10.00'),
            poster_phone_number="12345678901",
            is_accepted=False,
            is_digital=False,
            description="Description for test order 1",
            category="Category1"
        )

        self.order2 = Order.objects.create(
            title="Test Order 2",
            price=Decimal('20.00'),
            poster_phone_number="19876543210",
            is_accepted=False,
            is_digital=False,
            description="Description for test order 2",
            category="Category2"
        )

    def test_hello_world_view(self):
        response = self.client.get(reverse('hello_world'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Hello, world!")

    def test_order_list_view(self):
        response = self.client.get(reverse('order_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.order1.title)
        self.assertContains(response, self.order2.title)

    def test_order_detail_view(self):
        response = self.client.get(reverse('order_detail', args=[self.order1.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.order1.title)
        self.assertContains(response, self.order1.description)

    def test_search_order_view(self):
        response = self.client.get(reverse('search_order'), {'query': '12345678901'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.order1.title)
        self.assertNotContains(response, self.order2.title)

    def test_mark_order_as_accepted(self):
        response = self.client.post(reverse('mark_order_as_accepted', args=[self.order1.id]))
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(
            str(response.content, encoding='utf8'),
            {'status': 'success', 'message': f'Order {self.order1.id} has been marked as accepted.'}
        )
        self.order1.refresh_from_db()
        self.assertTrue(self.order1.is_accepted)

    def test_list_orders_pending_approval(self):
        response = self.client.get(reverse('list_orders_pending_approval'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.order1.title)
        self.assertContains(response, self.order2.title)

    def test_create_order_view(self):
        response = self.client.post(reverse('post'), {
            'title': 'New Order',
            'price': '30.00',
            'poster_phone_number': '19999999999',
            'description': 'New order description',
            'category': 'New Category',
            'is_digital': False
        })
        self.assertEqual(response.status_code, 200)  # Adjust based on your redirect or render
        self.assertTrue(Order.objects.filter(title='New Order').exists())

    def test_delete_order(self):
        response = self.client.post(reverse('delete_order', args=[self.order1.id]))
        self.assertEqual(response.status_code, 200)  # Adjust based on your redirect or render
        self.assertFalse(Order.objects.filter(id=self.order1.id).exists())


    def test_pending_orders_only(self):
        self.order2.is_accepted = True
        self.order2.save()
        response = self.client.get(reverse('list_orders_pending_approval'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.order1.title)
        self.assertNotContains(response, self.order2.title)

    def test_search_order_no_results(self):
        response = self.client.get(reverse('search_order'), {'query': 'Nonexistent'})
        self.assertEqual(response.status_code, 200)
        self.assertNotContains(response, self.order1.title)
        self.assertNotContains(response, self.order2.title)

    def test_mark_order_already_accepted(self):
        self.order1.is_accepted = True
        self.order1.save()
        response = self.client.post(reverse('mark_order_as_accepted', args=[self.order1.id]))
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(
            str(response.content, encoding='utf8'),
            {'status': 'success', 'message': f'Order {self.order1.id} has been marked as accepted.'}
        )
        self.order1.refresh_from_db()
        self.assertTrue(self.order1.is_accepted)

    def test_delete_non_existent_order(self):
        non_existent_order_id = 9999
        response = self.client.post(reverse('delete_order', args=[non_existent_order_id]))
        self.assertEqual(response.status_code, 404)

    def test_order_list_empty(self):
        Order.objects.all().delete()  # Ensure no orders exist
        response = self.client.get(reverse('order_list'))
        self.assertEqual(response.status_code, 200)
        self.assertFalse(Order.objects.filter(title__isnull=False).exists())

        # self.assertContains(response, 'No orders found.')

    def test_search_order_case_insensitive(self):
        response = self.client.get(reverse('search_order'), {'query': 'test order 1'.upper()})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.order1.title)
        self.assertNotContains(response, self.order2.title)







