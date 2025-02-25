from app.services.cart_service import CartService
from app.models.order import Order
from app.models.order_item import OrderItem
from app.models.product import Product

class CheckoutService:
    @staticmethod
    def checkout(user_id):
        # 1. جلب محتويات السلة الخاصة بالمستخدم
        cart_items = CartService.get_cart_items(user_id)
        if not cart_items:
            return "⚠️ لا توجد عناصر في السلة."

        total_amount = 0
        # 2. حساب المبلغ الإجمالي للمنتجات في السلة
        for item in cart_items:
            product_id = item['ProductID']
            quantity = item['Quantity']
            product = Product.get_product_by_id(product_id)
            if product:
                total_amount += product.price * quantity
            else:
                return f"⚠️ المنتج {product_id} غير موجود."

        # 3. إنشاء الطلب
        order = Order(user_id, total_amount)
        order.add_order()  # إضافة الطلب إلى قاعدة البيانات

        # 4. إضافة عناصر الطلب (OrderItems)
        for item in cart_items:
            product_id = item['ProductID']
            quantity = item['Quantity']
            price = Product.get_product_by_id(product_id).price
            order_item = OrderItem(order.user_id, product_id, quantity, price)
            order_item.add_order_item()  # إضافة العنصر إلى الطلب في جدول OrderItems

        # 5. تحديث المخزون: تقليل الكمية المتاحة في المخزون
        for item in cart_items:
            product_id = item['ProductID']
            quantity = item['Quantity']
            Product.update_stock(product_id, quantity)

        # 6. تفريغ السلة بعد إتمام عملية الشراء
        CartService.clear_cart(user_id)

        return f"✅ تم إتمام عملية الشراء بنجاح. إجمالي المبلغ: {total_amount}."

    @staticmethod
    def get_order_by_user(user_id):
        query = "SELECT * FROM Orders WHERE UserID = ?"
        return execute_query(query, (user_id,), fetch=True)

    @staticmethod
    def get_order_by_id(order_id):
        query = "SELECT * FROM Orders WHERE OrderID = ?"
        return execute_query(query, (order_id,), fetch=True)
