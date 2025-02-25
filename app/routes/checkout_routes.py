from flask import Blueprint, request, jsonify
from app.services.checkout_service import CheckoutService

checkout_routes = Blueprint('checkout_routes', __name__)

# إتمام عملية الدفع (Checkout)
@checkout_routes.route('/checkout', methods=['POST'])
def checkout():
    data = request.get_json()
    user_id = data.get('user_id')

    # إتمام عملية الشراء
    result = CheckoutService.checkout(user_id)
    if "⚠️" in result:  # إذا كانت هناك مشكلة مثل عدم وجود عناصر في السلة
        return jsonify({"message": result}), 400

    return jsonify({"message": result}), 200
