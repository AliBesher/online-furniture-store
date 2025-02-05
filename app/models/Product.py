class Product:
    def __init__(self, name, description, price, dimensions , stock_quantity, category_id, image_url):
        self.name = name
        self.description = description
        self.price = price
        self.dimensions = dimensions
        self.stock_quantity = stock_quantity
        self.category_id = category_id
        self.image_url = image_url

    def add_product(self):
        query = """
        INSERT INTO Products (Name, Description, Price, dimensions , StockQuantity, CategoryID, ImageURL, CreatedAt)
        VALUES (?, ?, ?, ?, ?, ?, GETDATE())
        """
        execute_query(query, (self.name, self.description, self.price, self.dimensions, self.stock_quantity, self.category_id, self.image_url))
        print(f"تمت إضافة المنتج '{self.name}' بنجاح.")

    def update_product(self, product_id):
        query = """
        UPDATE Products
        SET Name = ?, Description = ?, Price = ?,  dimensions =?, StockQuantity = ?, CategoryID = ?, ImageURL = ?
        WHERE ProductID = ?
        """
        execute_query(query, (self.name, self.description, self.price, self.stock_quantity, self.category_id, self.image_url, product_id))
        print(f"تم تحديث المنتج '{self.name}' بنجاح.")

    def delete_product(self, product_id):
        query = "DELETE FROM Products WHERE ProductID = ?"
        execute_query(query, (product_id,))
        print(f"تم حذف المنتج بنجاح.")
