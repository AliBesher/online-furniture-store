class User:
    def __init__(self, name, email, password, role="customer"):
        self.name = name
        self.email = email
        self.password = password
        self.role = role

    def add_user(self):
        query = """
        INSERT INTO Users (Name, Email, Password, Role, CreatedAt)
        VALUES (?, ?, ?, ?, GETDATE())
        """
        execute_query(query, (self.name, self.email, self.password, self.role))
        print(f"تمت إضافة المستخدم '{self.name}' بنجاح.")

    def update_user(self, user_id):
        query = """
        UPDATE Users
        SET Name = ?, Email = ?, Password = ?, Role = ?
        WHERE UserID = ?
        """
        execute_query(query, (self.name, self.email, self.password, self.role, user_id))
        print(f"تم تحديث بيانات المستخدم '{self.name}' بنجاح.")

    def delete_user(self, user_id):
        query = "DELETE FROM Users WHERE UserID = ?"
        execute_query(query, (user_id,))
        print(f"تم حذف المستخدم بنجاح.")
