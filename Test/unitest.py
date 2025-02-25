import pytest
from app.services.product_service import ProductService
from app.models.Product import Product

def test_add_product():
    # Add product with valid data
    result = ProductService.add_product("Wooden Sofa", "Comfortable and stylish", 300, "200x85x90 cm", 10, 1, "image_url")
    assert "تمت إضافة المنتج 'Wooden Sofa' بنجاح" in result

def test_update_product():
    # Update product with valid data
    result = ProductService.update_product(1, "Wooden Sofa Updated", "Updated description", 350, "210x90x95 cm", 5, 1, "new_image_url")
    assert "تم تحديث المنتج 'Wooden Sofa Updated' بنجاح" in result

from app.services.order_service import OrderService
from app.services.cart_service import CartService
from app.models.product import Product
from app.models.order_item import OrderItem

def test_create_order():
    # Assuming we have cart items and products in the cart
    cart_items = CartService.get_cart_items(1)
    result = OrderService.create_order(1)  # User ID 1
    assert "تم إتمام عملية الشراء" in result
