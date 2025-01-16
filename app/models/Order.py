class Order:
    def __init__(self, user_id, total_amount, status="pending"):
        self.user_id = user_id
        self.total_amount = total_amount
        self.status = status

    def add_order(self):
        query = """
        INSERT INTO Orders (UserID, TotalAmount, Status, CreatedAt)
        VALUES (?, ?, ?, GETDATE())
        """
        execute_query(query, (self.user_id, self.total_amount, self.status))
        print(f"تمت إضافة الطلب بنجاح.")

    def update_order(self, order_id):
        query = """
        UPDATE Orders
        SET Status = ?, TotalAmount = ?
        WHERE OrderID = ?
        """
        execute_query(query, (self.status, self.total_amount, order_id))
        print(f"تم تحديث حالة الطلب {order_id} بنجاح.")

    def delete_order(self, order_id):
        query = "DELETE FROM Orders WHERE OrderID = ?"
        execute_query(query, (order_id,))
        print(f"تم حذف الطلب بنجاح.")
