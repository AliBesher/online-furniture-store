from app.models.product import Product

class ProductService:
    @staticmethod
    def add_product(name, description, price, dimensions, stock_quantity, category, image_url):
        """
        دالة لإضافة منتج جديد إلى قاعدة البيانات بعد التحقق من بعض البيانات.
        """
        # التحقق من أن السعر أكبر من صفر
        if price <= 0:
            return "⚠️ السعر يجب أن يكون أكبر من 0"

        # التحقق من أن الكمية أكبر من أو تساوي صفر
        if stock_quantity < 0:
            return "⚠️ الكمية يجب أن تكون أكبر من أو تساوي 0"

        # إنشاء الكائن Product واستخدام دالة add_product من كلاس Product
        product = Product(name, description, price, dimensions, stock_quantity, category, image_url)
        product.add_product()  # إضافة المنتج إلى قاعدة البيانات
        return f"تمت إضافة المنتج '{name}' بنجاح."

    @staticmethod
    def update_product(product_id, name, description, price, dimensions, stock_quantity, category, image_url):
        """
        دالة لتحديث منتج موجود بناءً على ProductID.
        """
        # التحقق من أن السعر أكبر من صفر
        if price <= 0:
            return "⚠️ السعر يجب أن يكون أكبر من 0"

        # التحقق من أن الكمية أكبر من أو تساوي صفر
        if stock_quantity < 0:
            return "⚠️ الكمية يجب أن تكون أكبر من أو تساوي 0"

        # إنشاء الكائن Product واستخدام دالة update_product من كلاس Product
        product = Product(name, description, price, dimensions, stock_quantity, category, image_url)
        product.update_product(product_id)  # تحديث المنتج في قاعدة البيانات
        return f"تم تحديث المنتج '{name}' بنجاح."

    @staticmethod
    def delete_product(product_id):
        """
        دالة لحذف منتج من قاعدة البيانات باستخدام ProductID.
        """
        product = Product("", "", 0, 0, 0, "", "")  # إنشاء كائن منتج فارغ
        product.delete_product(product_id)  # حذف المنتج باستخدام دالة delete_product من كلاس Product
        return "تم حذف المنتج بنجاح."

    @staticmethod
    def get_product_by_id(product_id):
        """
        دالة لاسترجاع منتج باستخدام ProductID.
        """
        return Product.get_product_by_id(product_id)  # استخدام دالة get_product_by_id من كلاس Product

    @staticmethod
    def update_product_stock(product_id, quantity):
        """
        دالة لتحديث المخزون للمنتج.
        """
        if quantity < 0:
            return "⚠️ الكمية يجب أن تكون أكبر من أو تساوي 0"

        # استدعاء دالة update_stock من كلاس Product لتحديث المخزون
        Product.update_stock(product_id, quantity)
        return f"تم تحديث المخزون للمنتج {product_id} بنجاح."

