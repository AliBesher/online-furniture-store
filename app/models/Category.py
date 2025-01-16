class Category:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def add_category(self):
        query = """
        INSERT INTO Categories (Name, Description, CreatedAt)
        VALUES (?, ?, GETDATE())
        """
        execute_query(query, (self.name, self.description))
        print(f"تمت إضافة الفئة '{self.name}' بنجاح.")

    def update_category(self, category_id):
        query = """
        UPDATE Categories
        SET Name = ?, Description = ?
        WHERE CategoryID = ?
        """
        execute_query(query, (self.name, self.description, category_id))
        print(f"تم تحديث الفئة '{self.name}' بنجاح.")

    def delete_category(self, category_id):
        query = "DELETE FROM Categories WHERE CategoryID = ?"
        execute_query(query, (category_id,))
        print(f"تم حذف الفئة بنجاح.")
