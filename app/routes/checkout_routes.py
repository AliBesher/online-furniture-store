from flask import Blueprint, request, jsonify
from app.services.checkout_service import process_payment, finalize_order

checkout_bp = Blueprint('checkout', __name__)

@checkout_bp.route('/checkout', methods=['POST'])
def checkout():
    """
    API لإنهاء الطلب وإتمام الدفع
    """
    data = request.json
    user_id = data.get("user_id")
    payment_method = data.get("payment_method")
    card_number = data.get("card_number")
    cvv = data.get("cvv")
    expiry_date = data.get("expiry_date")

    # تنفيذ محاكاة الدفع
    payment_result = process_payment(payment_method, card_number, cvv, expiry_date)

    if payment_result["status"] == "failed":
        return jsonify(payment_result), 400  # فشل الدفع

    # حساب السعر الإجمالي من السلة
    from app.db import cursor
    cursor.execute("SELECT SUM(f.price * c.quantity) FROM Cart c JOIN Furniture f ON c.furniture_id = f.id WHERE c.user_id = ?", (user_id,))
    total_price = cursor.fetchone()[0]

    if not total_price:
        return jsonify({"status": "failed", "message": "Cart is empty"}), 400

    # إتمام الطلب بعد نجاح الدفع
    order_result = finalize_order(user_id, total_price)

    return jsonify(order_result)
