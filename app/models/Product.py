class Product:
    def __init__(self, name, description, price, dimensions, stock_quantity, category_id, image_url):
        self.name = name
        self.description = description
        self.price = price
        self.dimensions = dimensions
        self.stock_quantity = stock_quantity
        self.category_id = category_id
        self.image_url = image_url

    def add_product(self):
        query = """
        INSERT INTO Products (Name, Description, Price, Dimensions, StockQuantity, CategoryID, ImageURL, CreatedAt)
        VALUES (?, ?, ?, ?, ?, ?, GETDATE())
        """
        execute_query(query, (self.name, self.description, self.price, self.dimensions, self.stock_quantity, self.category_id, self.image_url))

    def update_product(self, product_id):
        query = """
        UPDATE Products
        SET Name = ?, Description = ?, Price = ?, Dimensions = ?, StockQuantity = ?, CategoryID = ?, ImageURL = ?
        WHERE ProductID = ?
        """
        execute_query(query, (self.name, self.description, self.price, self.dimensions, self.stock_quantity, self.category_id, self.image_url, product_id))

    def delete_product(self, product_id):
        query = "DELETE FROM Products WHERE ProductID = ?"
        execute_query(query, (product_id,))

    @staticmethod
    def get_product_by_id(product_id):
        """
        استرجاع منتج من قاعدة البيانات باستخدام ProductID
        """
        query = "SELECT * FROM Products WHERE ProductID = ?"
        result = execute_query(query, (product_id,), fetch=True)

        if result:
            # تحويل النتائج إلى كائن منتج
            return Product(result[0][1], result[0][2], result[0][3], result[0][4], result[0][5], result[0][6], result[0][7])

        return None  # إذا لم يتم العثور على المنتج، نرجع None

    @staticmethod
    def update_stock(product_id, quantity):
        """
        تحديث المخزون للمنتج بناءً على quantity
        """
        query = """
        UPDATE Products
        SET StockQuantity = StockQuantity - ?
        WHERE ProductID = ?
        """
        execute_query(query, (quantity, product_id))
        print(f"تم تحديث المخزون للمنتج {product_id} بنجاح.")

