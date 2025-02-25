import pyodbc

# إعداد الاتصال بقاعدة البيانات
conn_str = (
    "Driver={ODBC Driver 17 for SQL Server};"
    "Server=DESKTOP-4809N4L;"
    "Database=FurnitureStore;"
    "Trusted_Connection=yes;"
)

def get_connection():
    """دالة للحصول على الاتصال بقاعدة البيانات"""
    return pyodbc.connect(conn_str)
