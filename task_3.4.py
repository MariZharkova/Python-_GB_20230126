# №3.4[23]. Дан список, состоящий из целых чисел. Напишите программу, которая сформирует список из тех элементов,
# которые больше предыдущего (элемента с предыдущим номером)
# Примечание: Пользователь может вводить значения списка или список задан изначально.
#     Примеры/Тесты:
#     Input: [0, -1, 5, 2, 1]
#     Output: [5]

#     Input: [-2, -1, 5, 2, 3]
#     Output: [-1, 5, 3]
# [*] Усложнение: Запишите алгоритм в одну строку, используйте Comprehension

list_1 = [0, -1, 5, 2, 1]
count = 0
result = []

for i in range(1, len(list_1)):
    if list_1[i] > list_1[i - 1]:
        result.append(list_1[i])
print(*result)

list_3 = [list_1[i] for i in range(1, len(list_1)) if list_1[i] > list_1[i-1]]

