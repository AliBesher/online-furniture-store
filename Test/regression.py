import unittest
from unittest.mock import patch
import requests

BASE_URL = "http://localhost:5000"

class TestIntegrationFurnitureStore(unittest.TestCase):
    
    @patch('requests.post')
    def test_add_product_api(self, mock_post):
        mock_post.return_value.status_code = 201
        mock_post.return_value.json.return_value = {"message": "تمت إضافة المنتج 'Table' بنجاح."}
        
        response = requests.post(f"{BASE_URL}/products", json={
            "name": "Table",
            "description": "Wooden table",
            "price": 150,
            "dimensions": "120x80",
            "stock_quantity": 10,
            "category": 1,
            "image_url": "image.jpg"
        })
        
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json()["message"], "تمت إضافة المنتج 'Table' بنجاح.")
    
    @patch('requests.post')
    def test_checkout_api(self, mock_post):
        mock_post.return_value.status_code = 200
        mock_post.return_value.json.return_value = {"message": "✅ تم إتمام عملية الشراء بنجاح. إجمالي المبلغ: 500."}
        
        response = requests.post(f"{BASE_URL}/checkout", json={"user_id": 1})
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["message"], "✅ تم إتمام عملية الشراء بنجاح. إجمالي المبلغ: 500.")

if _name_ == "_main_":
    unittest.main()
