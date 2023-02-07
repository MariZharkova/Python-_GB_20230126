# 4.2[24]: В фермерском хозяйстве в Карелии выращивают чернику. Она растет на круглой грядке, 
# причем кусты высажены только по окружности. Таким образом, у каждого куста есть ровно два соседних. 
# Всего на грядке растет N кустов. Собирающий модуль за один заход, находясь непосредственно перед 
# некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.

# Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход 
# собирающий модуль, находясь перед некоторым кустом. На входе задано количество ягод на каждом кусте. 
# Не обязательно вводить их с клавиатуры, можно задать непосредственно в коде программы

# Примеры/Тесты:
# Input1: 1, 2, 3, 4, 5, 6, 7, 8
# Output1: Макс. кол-во ягод 21, собрано для куста 7

# Input1: 11, 92, 1, 42, 15, 12, 11, 81
# Output1: Макс. кол-во ягод 184, собрано для куста 1

# garden_bed = [1, 2, 3, 4, 5, 6, 7, 8]
garden_bed = [11, 92, 1, 42, 15, 12, 11, 81]
berries = 0
bash = 0

for i in range (- 1, len(garden_bed) - 1):
    triple = [garden_bed[i - 1], garden_bed[i], garden_bed[i + 1]]
    prev, current, next = tuple (triple)
    if berries < (prev + current + next):
        berries = prev + current + next
        bash = i + 1

print (f'Максимальное количество ягод {berries}, собрано для куста {bash}')