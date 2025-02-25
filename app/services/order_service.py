from app.models.order import Order
from app.models.order_item import OrderItem
from app.models.product import Product
from app.services.cart_service import CartService

class OrderService:
    @staticmethod
    def create_order(user_id):
        """
        دالة لإنشاء طلب جديد بناءً على محتويات السلة.
        """
        # 1. جلب محتويات السلة
        cart_items = CartService.get_cart_items(user_id)
        if not cart_items:
            return "⚠️ لا توجد عناصر في السلة."

        total_amount = 0
        # 2. حساب المبلغ الإجمالي
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

        # 4. إضافة عناصر الطلب إلى `OrderItems`
        for item in cart_items:
            product_id = item['ProductID']
            quantity = item['Quantity']
            price = Product.get_product_by_id(product_id).price
            order_item = OrderItem(order.user_id, product_id, quantity, price)
            order_item.add_order_item()  # إضافة العنصر إلى الطلب

        # 5. تحديث المخزون
        for item in cart_items:
            product_id = item['ProductID']
            quantity = item['Quantity']
            Product.update_stock(product_id, quantity)

        # 6. تفريغ السلة بعد إتمام العملية
        CartService.clear_cart(user_id)

        return f"✅ تم إتمام عملية الشراء بنجاح. إجمالي المبلغ: {total_amount}."

    @staticmethod
    def update_order_status(order_id, status):
        """
        دالة لتحديث حالة الطلب (مثل: "مكتمل"، "قيد المعالجة").
        """
        query = """
        UPDATE Orders
        SET Status = ?
        WHERE OrderID = ?
        """
        execute_query(query, (status, order_id))
        return f"تم تحديث حالة الطلب {order_id} إلى {status}."

    @staticmethod
    def delete_order(order_id):
        """
        دالة لحذف طلب.
        """
        # حذف العناصر المرتبطة بالطلب أولاً
        query = "DELETE FROM OrderItems WHERE OrderID = ?"
        execute_query(query, (order_id,))

        # ثم حذف الطلب نفسه
        query = "DELETE FROM Orders WHERE OrderID = ?"
        execute_query(query, (order_id,))
        return f"تم حذف الطلب {order_id} بنجاح."

    @staticmethod
    def get_order_by_user(user_id):
        """
        دالة لجلب جميع الطلبات الخاصة بالمستخدم.
        """
        query = "SELECT * FROM Orders WHERE UserID = ?"
        return execute_query(query, (user_id,), fetch=True)

    @staticmethod
    def get_order_by_id(order_id):
        """
        دالة لجلب تفاصيل طلب معين بناءً على OrderID.
        """
        query = "SELECT * FROM Orders WHERE OrderID = ?"
        return execute_query(query, (order_id,), fetch=True)
