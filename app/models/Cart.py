from app.db.execute_query import execute_query


class Cart:
    def __init__(self, user_id):
        self.user_id = user_id

    def add_to_cart(self, product_id, quantity):
        query = """
        INSERT INTO Cart (UserID, ProductID, Quantity, AddedAt)
        VALUES (?, ?, ?, GETDATE())
        """
        execute_query(query, (self.user_id, product_id, quantity))
        print(f"تمت إضافة المنتج إلى السلة بنجاح.")

    def update_cart(self, product_id, new_quantity):
        query = """
        UPDATE Cart
        SET Quantity = ?
        WHERE UserID = ? AND ProductID = ?
        """
        execute_query(query, (new_quantity, self.user_id, product_id))
        print(f"تم تحديث الكمية في السلة بنجاح.")

    def remove_from_cart(self, product_id):
        query = "DELETE FROM Cart WHERE UserID = ? AND ProductID = ?"
        execute_query(query, (self.user_id, product_id))
        print(f"تم إزالة المنتج من السلة بنجاح.")
