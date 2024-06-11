from django.test import TestCase
from .models import Order, Category
from decimal import Decimal


class OrderModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # 设置测试数据
        Category.objects.create(name='Test Category')
        Order.objects.create(
            title='Test Order',
            price=Decimal('10.00'),
            is_digital=True,
            description='Test Description',
            category=Category.objects.get(name='Test Category')
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
        self.assertEqual(order.category.name, 'Test Category')

    def test_order_created_at(self):
        order = Order.objects.get(id=1)
        self.assertIsNotNone(order.created_at)

    def test_order_updated_at(self):
        order = Order.objects.get(id=1)
        self.assertIsNotNone(order.updated_at)

    def test_order_default_is_digital(self):
        # 测试默认值
        order = Order.objects.create(title='Default Order', price=Decimal('5.00'))
        self.assertFalse(order.is_digital)


class CategoryModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Category.objects.create(name='Test Category')

    def test_category_name(self):
        category = Category.objects.get(id=1)
        self.assertEqual(category.name, 'Test Category')
