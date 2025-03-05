import unittest
from unittest.mock import patch, MagicMock
from app.services.product_service import ProductService
from app.services.order_service import OrderService
from app.services.cart_service import CartService
from app.services.checkout_service import CheckoutService
from app.services.user_service import UserService

class TestUnitFurnitureStore(unittest.TestCase):
    
    @patch('app.models.product.Product.add_product')
    def test_add_product(self, mock_add_product):
        mock_add_product.return_value = None
        response = ProductService.add_product("Table", "Wooden table", 150, "120x80", 10, 1, "image.jpg")
        self.assertEqual(response, "تمت إضافة المنتج 'Table' بنجاح.")
    
    @patch('app.models.product.Product.delete_product')
    def test_delete_product(self, mock_delete_product):
        mock_delete_product.return_value = None
        response = ProductService.delete_product(1)
        self.assertEqual(response, "تم حذف المنتج بنجاح.")
    
    @patch('app.services.cart_service.CartService.get_cart_items')
    @patch('app.services.order_service.OrderService.create_order')
    def test_create_order_from_cart(self, mock_create_order, mock_get_cart_items):
        mock_get_cart_items.return_value = [{'ProductID': 1, 'Quantity': 2}]
        mock_create_order.return_value = "✅ تم إتمام عملية الشراء بنجاح. إجمالي المبلغ: 300."
        response = OrderService.create_order(1)
        self.assertIn("✅ تم إتمام عملية الشراء", response)
    
    @patch('app.services.checkout_service.CheckoutService.checkout')
    def test_checkout_process(self, mock_checkout):
        mock_checkout.return_value = "✅ تم إتمام عملية الشراء بنجاح. إجمالي المبلغ: 500."
        response = CheckoutService.checkout(1)
        self.assertEqual(response, "✅ تم إتمام عملية الشراء بنجاح. إجمالي المبلغ: 500.")
    
    @patch('app.models.user.User.add_user')
    def test_add_user(self, mock_add_user):
        mock_add_user.return_value = None
        response = UserService.add_user("Wesam", "wesam@example.com", "password123")
        self.assertEqual(response, "تمت إضافة المستخدم 'Wesam' بنجاح.")
    
    def test_product_stock_update(self):
        with patch('app.models.product.Product.update_stock') as mock_update_stock:
            mock_update_stock.return_value = None
            response = ProductService.update_product_stock(1, 5)
            self.assertEqual(response, "تم تحديث المخزون للمنتج 1 بنجاح.")

if __name__ == '__main__':
   unittest.main()
