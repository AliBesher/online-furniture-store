from app import execute_query

def view_users():  # حذف self
    query = "SELECT * FROM Users"
    users = execute_query(query, fetch=True)  # جلب جميع المستخدمين

    if not users:
        print("⚠️ لا يوجد مستخدمون في قاعدة البيانات.")
        return

    print("🧑‍💻 قائمة المستخدمين:")
    for user in users:
        print(user)


view_users()

