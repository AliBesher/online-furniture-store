from app.db.execute_query import execute_query


class OrderItem:
    def __init__(self, order_id, product_id, quantity, price):
        self.order_id = order_id
        self.product_id = product_id
        self.quantity = quantity
        self.price = price

    # دالة لإضافة عنصر إلى الطلب
    def add_order_item(self):
        query = """
        INSERT INTO OrderItems (OrderID, ProductID, Quantity, Price)
        VALUES (?, ?, ?, ?)
        """
        execute_query(query, (self.order_id, self.product_id, self.quantity, self.price))
        print(f"تمت إضافة عنصر الطلب للمنتج {self.product_id} بنجاح.")

    # دالة لتحديث عنصر الطلب
    def update_order_item(self, order_item_id, quantity, price):
        query = """
        UPDATE OrderItems
        SET Quantity = ?, Price = ?
        WHERE OrderItemID = ?
        """
        execute_query(query, (quantity, price, order_item_id))
        print(f"تم تحديث عنصر الطلب {order_item_id} بنجاح.")

    # دالة لحذف عنصر الطلب
    @staticmethod
    def delete_order_item(order_item_id):
        query = "DELETE FROM OrderItems WHERE OrderItemID = ?"
        execute_query(query, (order_item_id,))
        print(f"تم حذف عنصر الطلب {order_item_id} بنجاح.")
