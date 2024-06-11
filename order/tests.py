from django.core.exceptions import ValidationError
from django.test import TestCase
from .models import Order
from decimal import Decimal


class OrderModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # 设置测试数据
        Order.objects.create(
            title='Test Order',
            price=Decimal('10.00'),
            is_digital=True,
            description='Test Description',
            category='Test Category',
            poster_phone_number='12345678901'
        )

    def test_order_title(self):
        order = Order.objects.get(id=1)
        self.assertEqual(order.title, 'Test Order')

    def test_order_price(self):
        order = Order.objects.get(id=1)
        self.assertEqual(order.price, Decimal('10.00'))

    def test_order_is_digital(self):
        order = Order.objects.get(id=1)
        self.assertTrue(order.is_digital)

    def test_order_description(self):
        order = Order.objects.get(id=1)
        self.assertEqual(order.description, 'Test Description')

    def test_order_category(self):
        order = Order.objects.get(id=1)
        self.assertEqual(order.category, 'Test Category')

    def test_order_created_at(self):
        order = Order.objects.get(id=1)
        self.assertIsNotNone(order.created_at)

    def test_order_updated_at(self):
        order = Order.objects.get(id=1)
        self.assertIsNotNone(order.updated_at)

    def test_order_default_is_digital(self):
        # 测试默认值
        order = Order.objects.create(title='Default Order', price=Decimal('5.00'), poster_phone_number='12345678901')
        self.assertFalse(order.is_digital)

    def test_order_valid_phone_number(self):
        order = Order.objects.get(id=1)
        self.assertEqual(order.poster_phone_number, '12345678901')

    def test_order_invalid_phone_number(self):
        with self.assertRaises(ValidationError):
            order = Order(
                title='Invalid Phone Order',
                price=Decimal('20.00'),
                is_digital=False,
                description='Invalid Phone Number',
                category='Test Category',
                poster_phone_number='0987654321'
            )
            order.full_clean()  # This will trigger the validation
