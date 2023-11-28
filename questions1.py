


def isEven(value):
    return value%2==0
    # + Компактность функции
    # + Простота Понимания функции 

def test_parity(value):
    num = value//2
    if num*2 != value:
        rezult = "Значение нечетное"
    else:
        rezult = "Значение четное"
    return rezult
# - Нагромаждение функции
# - Скорость выполнения функции


print(isEven(13))
print(test_parity(-16))