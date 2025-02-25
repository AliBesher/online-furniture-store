from flask import Blueprint, request, jsonify
from app.services.cart_service import CartService

cart_routes = Blueprint('cart_routes', __name__)

# عرض السلة
@cart_routes.route('/cart', methods=['GET'])
def view_cart():
    user_id = request.args.get('user_id')  # الحصول على user_id من الـ query parameter
    cart_items = CartService.get_cart_items(user_id)

    if not cart_items:
        return jsonify({"message": "⚠️ لا توجد عناصر في السلة."}), 404

    return jsonify({"cart_items": cart_items}), 200

# إضافة منتج إلى السلة
@cart_routes.route('/cart', methods=['POST'])
def add_to_cart():
    data = request.get_json()
    user_id = data.get('user_id')
    product_id = data.get('product_id')
    quantity = data.get('quantity')

    CartService.add_to_cart(user_id, product_id, quantity)
    return jsonify({"message": "تم إضافة المنتج إلى السلة بنجاح."}), 201

# تحديث الكمية في السلة
@cart_routes.route('/cart/<int:product_id>', methods=['PUT'])
def update_cart(product_id):
    data = request.get_json()
    user_id = data.get('user_id')
    new_quantity = data.get('quantity')

    CartService.update_cart(user_id, product_id, new_quantity)
    return jsonify({"message": "تم تحديث الكمية في السلة بنجاح."}), 200

# إزالة منتج من السلة
@cart_routes.route('/cart/<int:product_id>', methods=['DELETE'])
def remove_from_cart(product_id):
    data = request.get_json()
    user_id = data.get('user_id')

    CartService.remove_from_cart(user_id, product_id)
    return jsonify({"message": "تم إزالة المنتج من السلة بنجاح."}), 200
