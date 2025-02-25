from flask import Blueprint, request, jsonify
from app.services.order_service import OrderService

order_routes = Blueprint('order_routes', __name__)

# إنشاء طلب جديد
@order_routes.route('/orders', methods=['POST'])
def create_order():
    data = request.get_json()
    user_id = data.get('user_id')

    result = OrderService.create_order(user_id)
    if "⚠️" in result:  # إذا كانت هناك مشكلة
        return jsonify({"message": result}), 400

    return jsonify({"message": result}), 201

# تحديث حالة الطلب
@order_routes.route('/orders/<int:order_id>', methods=['PUT'])
def update_order_status(order_id):
    data = request.get_json()
    status = data.get('status')  # حالة الطلب الجديدة (مثل: مكتمل، قيد المعالجة)

    result = OrderService.update_order_status(order_id, status)
    return jsonify({"message": result}), 200

# حذف طلب
@order_routes.route('/orders/<int:order_id>', methods=['DELETE'])
def delete_order(order_id):
    result = OrderService.delete_order(order_id)
    return jsonify({"message": result}), 200

# عرض الطلبات الخاصة بالمستخدم
@order_routes.route('/orders', methods=['GET'])
def view_orders():
    user_id = request.args.get('user_id')  # الحصول على user_id من الـ query parameter
    orders = OrderService.get_order_by_user(user_id)

    if not orders:
        return jsonify({"message": "⚠️ لا توجد طلبات لهذا المستخدم."}), 404

    return jsonify({"orders": orders}), 200
