# -----------------------------
# Simple Python Invoice Program
# -----------------------------
# This program calculates the total amount for a list of products,
# applies a discount if the total is greater than or equal to 100,
# and prints a detailed invoice.
# Concepts used: input, lists, loops, conditionals, functions
# -----------------------------

# دالة لإدخال أسعار المنتجات وحساب المجموع
def get_total(num_products):
    prices = []  # قائمة لتخزين أسعار المنتجات
    for i in range(num_products):
        # إدخال سعر كل منتج وتحويله إلى float
        price = float(input(f"Enter price for product {i + 1}: "))
        prices.append(price)  # إضافة السعر للقائمة
    total = sum(prices)  # جمع كل الأسعار للحصول على المجموع الكلي
    return prices, total  # إعادة القائمة والمجموع

# دالة لتطبيق الخصم
def apply_discount(total):
    if total >= 100:  # إذا كان المجموع ≥ 100
        final_total = total * 0.9  # خصم 10%
    else:
        final_total = total  # بدون خصم
    return final_total  # إعادة المبلغ النهائي

# دالة لطباعة الفاتورة المفصلة
def print_invoice(prices, total, final_total):
    print("\n--- Invoice ---")
    for idx, price in enumerate(prices):  # طباعة كل منتج وسعره
        print(f"Product {idx + 1}: ${price}")
    print(f"Total before discount: ${total}")  # المجموع قبل الخصم
    print(f"Final amount after discount: ${final_total}")  # المبلغ النهائي بع_
# -----------------------------
# البرنامج الرئيسي
# -----------------------------
num_products = int(input("Enter the number of products: "))  # عدد المنتجات
prices, total = get_total(num_products)  # استدعاء الدالة لإدخال الأسعار وحساب المجموع
final_total = apply_discount(total)  # استدعاء الدالة لتطبيق الخصم
print_invoice(prices, total, final_total)  # طباعة الفاتورة
