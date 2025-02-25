import pyodbc

from app.db.connection import get_connection

def execute_query(query, params=None, fetch=False):
    """
    دالة لتنفيذ استعلامات SQL على قاعدة البيانات.
    - query: نص الاستعلام.
    - params: المعاملات التي سيتم تمريرها للاستعلام (إن وجدت).
    - fetch: إذا كانت العملية تحتاج إلى جلب بيانات، يتم ضبطها على True.
    """
    try:
        with get_connection() as connection:  # الحصول على الاتصال باستخدام get_connection
            with connection.cursor() as cursor:  # المؤشر يتم إدارته تلقائيًا.
                if params:  # إذا كان هناك معاملات تمرير.
                    cursor.execute(query, params)
                else:  # بدون معاملات.
                    cursor.execute(query)

                if fetch:  # إذا كنت بحاجة لجلب بيانات.
                    return cursor.fetchall()  # إرجاع النتائج.

                connection.commit()  # تأكيد التغييرات عند الحاجة.
    except pyodbc.Error as e:
        print(f"حدث خطأ أثناء تنفيذ الاستعلام: {e}")
        return None
