from flask import Blueprint, request, jsonify
from app.services.product_service import ProductService

product_routes = Blueprint('product_routes', __name__)

@product_routes.route('/products', methods=['POST'])
def add_product():
    data = request.get_json()
    name = data.get('name')
    description = data.get('description')
    price = data.get('price')
    dimensions = data.get('dimensions')
    stock_quantity = data.get('stock_quantity')
    category = data.get('category')
    image_url = data.get('image_url')

    result = ProductService.add_product(name, description, price, dimensions, stock_quantity, category, image_url)
    return jsonify({"message": result}), 201

@product_routes.route('/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    data = request.get_json()
    name = data.get('name')
    description = data.get('description')
    price = data.get('price')
    dimensions = data.get('dimensions')
    stock_quantity = data.get('stock_quantity')
    category = data.get('category')
    image_url = data.get('image_url')

    result = ProductService.update_product(product_id, name, description, price, dimensions, stock_quantity, category, image_url)
    return jsonify({"message": result}), 200

@product_routes.route('/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    result = ProductService.delete_product(product_id)
    return jsonify({"message": result}), 200
