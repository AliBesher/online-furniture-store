from app.models.user import User

class UserService:
    @staticmethod
    def add_user(name, email, password, role="customer"):
        """
        دالة لإضافة مستخدم جديد.
        """
        # التأكد من أن البريد الإلكتروني ليس موجودًا بالفعل في قاعدة البيانات
        query = "SELECT * FROM Users WHERE Email = ?"
        result = execute_query(query, (email,), fetch=True)

        if result:
            return "⚠️ البريد الإلكتروني مستخدم بالفعل."

        # إنشاء كائن User واستخدام دالة add_user لإضافته إلى قاعدة البيانات
        user = User(name, email, password, role)
        user.add_user()
        return f"تمت إضافة المستخدم '{name}' بنجاح."

    @staticmethod
    def update_user(user_id, name, email, password, role):
        """
        دالة لتحديث بيانات المستخدم بناءً على UserID.
        """
        # التحقق من أن البريد الإلكتروني لا يتكرر مع مستخدم آخر
        query = "SELECT * FROM Users WHERE Email = ? AND UserID != ?"
        result = execute_query(query, (email, user_id), fetch=True)

        if result:
            return "⚠️ البريد الإلكتروني مستخدم بالفعل من قبل مستخدم آخر."

        # إنشاء كائن User واستخدام دالة update_user لتحديث البيانات
        user = User(name, email, password, role)
        user.update_user(user_id)
        return f"تم تحديث بيانات المستخدم '{name}' بنجاح."

    @staticmethod
    def delete_user(user_id):
        """
        دالة لحذف مستخدم من قاعدة البيانات باستخدام UserID.
        """
        user = User("", "", "", "")  # إنشاء كائن User فارغ
        user.delete_user(user_id)  # حذف المستخدم باستخدام دالة delete_user
        return "تم حذف المستخدم بنجاح."

    @staticmethod
    def get_users():
        """
        دالة لجلب جميع المستخدمين.
        """
        query = "SELECT * FROM Users"
        return execute_query(query, fetch=True)

    @staticmethod
    def get_user_by_id(user_id):
        """
        دالة لاسترجاع بيانات مستخدم بناءً على UserID.
        """
        query = "SELECT * FROM Users WHERE UserID = ?"
        result = execute_query(query, (user_id,), fetch=True)
        if result:
            return result[0]
        return None
