import unittest
from unittest.mock import patch
from app.services.order_service import OrderService
from app.services.cart_service import CartService
from app.models.product import Product

class TestRegressionFurnitureStore(unittest.TestCase):
    
    # Regression test: Ensures that when an order is created, cart is cleared, and stock is updated
    @patch('app.services.cart_service.CartService.clear_cart')
    @patch('app.models.product.Product.update_stock')
    @patch('app.services.order_service.OrderService.create_order')
    def test_order_process_updates_cart_and_stock(self, mock_create_order, mock_update_stock, mock_clear_cart):
        mock_create_order.return_value = "✅ تم إتمام عملية الشراء بنجاح. إجمالي المبلغ: 300."
        mock_update_stock.return_value = None
        mock_clear_cart.return_value = None

        response = OrderService.create_order(1)
        mock_update_stock.assert_called()
        mock_clear_cart.assert_called_with(1)
        self.assertIn("✅ تم إتمام عملية الشراء", response)

if _name_ == "_main_":
    unittest.main()
