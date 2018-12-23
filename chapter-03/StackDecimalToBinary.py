from structures.stack import Stack


def convert_decimal_to_binary(decimal_number):
    s = Stack()
    while decimal_number > 0:
        s.push(decimal_number % 2)
        decimal_number = decimal_number // 2

    num = ""
    while not s.is_empty():
        num = num + str(s.pop())

    return num


def convert_decimal_to_base(decimal_number, base):
    digits = "0123456789ABCDE"
    s = Stack()
    while decimal_number > 0:
        s.push(decimal_number % base)
        decimal_number = decimal_number // base

    num = ""
    while not s.is_empty():
        num = num + digits[s.pop()]

    return num


print(convert_decimal_to_binary(100))
print(convert_decimal_to_binary(42))
print(convert_decimal_to_base(233, 2))
print(convert_decimal_to_base(233, 8))
print(convert_decimal_to_base(233, 16))

print(convert_decimal_to_base(26, 26))
