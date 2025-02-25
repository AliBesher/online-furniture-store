from app.db.execute_query import execute_query

class CartService:
    @staticmethod
    def add_to_cart(user_id, product_id, quantity):
        # تحقق إذا كان المنتج موجودًا في السلة
        cart_item = CartService.get_cart_item(user_id, product_id)
        if cart_item:
            CartService.update_cart(user_id, product_id, cart_item['Quantity'] + quantity)
        else:
            CartService.create_cart_item(user_id, product_id, quantity)

    @staticmethod
    def create_cart_item(user_id, product_id, quantity):
        query = """
        INSERT INTO Cart (UserID, ProductID, Quantity, AddedAt)
        VALUES (?, ?, ?, GETDATE())
        """
        execute_query(query, (user_id, product_id, quantity))
        print(f"تم إضافة المنتج {product_id} إلى السلة.")

    @staticmethod
    def update_cart(user_id, product_id, new_quantity):
        query = """
        UPDATE Cart
        SET Quantity = ?
        WHERE UserID = ? AND ProductID = ?
        """
        execute_query(query, (new_quantity, user_id, product_id))
        print(f"تم تحديث الكمية للمنتج {product_id} في السلة.")

    @staticmethod
    def remove_from_cart(user_id, product_id):
        query = "DELETE FROM Cart WHERE UserID = ? AND ProductID = ?"
        execute_query(query, (user_id, product_id))
        print(f"تم إزالة المنتج {product_id} من السلة.")

    @staticmethod
    def get_cart_item(user_id, product_id):
        query = "SELECT * FROM Cart WHERE UserID = ? AND ProductID = ?"
        result = execute_query(query, (user_id, product_id), fetch=True)
        if result:
            return result[0]
        return None

    @staticmethod
    def get_cart_items(user_id):
        query = "SELECT * FROM Cart WHERE UserID = ?"
        return execute_query(query, (user_id,), fetch=True)
