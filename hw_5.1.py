# 5.1[26]: Напишите рекурсивную функцию для возведения числа a в степень b.
# Разрешается использовать только операцию умножения. Циклы использовать нельзя

# Примеры/Тесты:
# <function_name>(2,0) -> 1
# <function_name>(2,1) -> 2
# <function_name>(2,3) -> 8
# <function_name>(2,4) -> 16


def mult(a, b):
    if a == 0 and b != 0:
        return 0
    elif b == 0:
        return 1
    elif b == 1:
        return a
    else:
        return (a * mult(a, (b - 1)))

print(mult(2, 1))
print(mult(2, 3))
print(mult(2, 4))
