
"""
Convert Number to Thai Text.
เขียนโปรแกรมรับค่าจาก user เพื่อแปลง input ของ user ที่เป็นตัวเลข เป็นตัวหนังสือภาษาไทย
โดยที่ค่าที่รับต้องมีค่ามากกว่าหรือเท่ากับ 0 และน้อยกว่า 10 ล้าน

*** อนุญาตให้ใช้แค่ตัวแปรพื้นฐาน, built-in methods ของตัวแปรและ function พื้นฐานของ Python เท่านั้น
ห้ามใช้ Library อื่น ๆ ที่ต้อง import ในการทำงาน(ยกเว้น ใช้เพื่อการ test การทำงานของฟังก์ชัน).

"""
def convert_number_to_thai_text(number):
    thai_digits = {
        0: 'ศูนย์',
        1: 'หนึ่ง',
        2: 'สอง',
        3: 'สาม',
        4: 'สี่',
        5: 'ห้า',
        6: 'หก',
        7: 'เจ็ด',
        8: 'แปด',
        9: 'เก้า'
    }

    thai_units = ['', 'สิบ', 'ร้อย', 'พัน', 'หมื่น', 'แสน', 'ล้าน', 'สิบล้าน']

    if number == 0:
        return thai_digits[0]

    digits = []
    while number > 0:
        digits.append(number % 10)
        number //= 10

    thai_text = ''
    for i, digit in enumerate(digits):
        if digit > 0:
            thai_text = thai_digits[digit] + thai_units[i] + thai_text

    thai_text = thai_text.replace('หนึ่งสิบ', 'สิบ')
    thai_text = thai_text.replace('สองสิบ', 'ยี่สิบ')
    thai_text = thai_text.strip()

    return thai_text
