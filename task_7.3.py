# №7.3[###]. Имея список вида [['Иванов', 'Иван', 'Иванович'], ['Петров', 'Петр', 'Петрович']...]
# преобразовать его в списки вида
# 1) ['Иванов-И-И', 'Петров-П-П', 'Соколов-И-Г'...]
# 2) ['Иванов И.И.', 'Петров П.П.', 'Соколов И.Г.'...]
# с использованием Comprehension; Comprehension + функция; Comprehension + lambda; map
# [**] Усложнение. Дополнить обработку списка условием: Выбираем только те элементы, в которых первая буква П 

lst = [['Иванов', 'Иван', 'Иванович'],
       ['Петров', 'Петр', 'Петрович'],
       ['Соколов', 'Илья', 'Григорьевич'], ]


def template1(man):
    surname, name, parent = man
    return f"{surname}-{name[0]}-{parent[0]}"


def filter1(man):
    surname, name, parent = man
    if surname[0] == "П": return True
    return False

lst2 = [f"{man[0]}-{man[1][0]}-{man[2][0]}" for man in lst]
lst3 = [f"{surname}-{name[0]}-{parent[0]}" for surname, name, parent in lst]
lst4 = [template1(man) for man in lst]
lst5 = [(lambda x, y, z: f"{x}-{y[0]}-{z[0]}")(x, y, z) for x, y, z in lst]
lst6 = list(map(template1, lst))
print(lst2, lst3, lst4, lst5, lst6)

print("*" * 20)
lst7 = [f"{man[0]}-{man[1][0]}-{man[2][0]}" for man in lst if man[0][0] == "П"]
lst8 = [f"{surname}-{name[0]}-{parent[0]}" for surname, name, parent in lst if surname[0] == "П"]
lst9 = [template1(man) for man in lst if man[0][0] == "П"]
lst10 = [(lambda x, y, z: f"{x}-{y[0]}-{z[0]}")(x, y, z) for x, y, z in lst if x[0][0] == "П"]
lst11 = list(map(template1, filter(filter1,lst)))


print(lst7, lst8, lst9, lst10, lst11)