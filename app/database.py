import pyodbc

conn_str = (
    "Driver={ODBC Driver 17 for SQL Server};"
    "Server=DESKTOP-4809N4L;"
    "Database=FurnitureStore;"
    "Trusted_Connection=yes;"
)

def execute_query(query, params=None, fetch=False):
    """
    دالة لتنفيذ استعلامات على قاعدة البيانات.
    - query: نص الاستعلام.
    - params: المعاملات التي سيتم تمريرها للاستعلام (إن وجدت).
    - fetch: إذا كانت العملية تحتاج إلى جلب بيانات، يتم ضبطها على True.
    """
    try:
        with pyodbc.connect(conn_str) as connection:  # الاتصال يتم فتحه وإغلاقه تلقائيًا.
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
