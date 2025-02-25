from flask import Blueprint, request, jsonify
from app.services.user_service import UserService

user_routes = Blueprint('user_routes', __name__)

# إضافة مستخدم جديد
@user_routes.route('/users', methods=['POST'])
def add_user():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    password = data.get('password')
    role = data.get('role', "customer")  # افتراضيًا، تكون القيمة "customer"

    result = UserService.add_user(name, email, password, role)
    return jsonify({"message": result}), 201

# تحديث بيانات مستخدم
@user_routes.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    password = data.get('password')
    role = data.get('role')

    result = UserService.update_user(user_id, name, email, password, role)
    return jsonify({"message": result}), 200

# حذف مستخدم
@user_routes.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    result = UserService.delete_user(user_id)
    return jsonify({"message": result}), 200

# عرض جميع المستخدمين
@user_routes.route('/users', methods=['GET'])
def get_users():
    users = UserService.get_users()
    return jsonify({"users": users}), 200

# عرض مستخدم بناءً على UserID
@user_routes.route('/users/<int:user_id>', methods=['GET'])
def get_user_by_id(user_id):
    user = UserService.get_user_by_id(user_id)
    if user:
        return jsonify({"user": user}), 200
    return jsonify({"message": "⚠️ المستخدم غير موجود."}), 404
