# 1.2[4]. Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. 
# Сколько журавликов сделал каждый ребенок, если известно, 
# что Петя и Сережа сделали одинаковое количество журавликов, 
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
# Примеры/Тесты:
# 6 >>>  1  4  1
# 24 >>> 4  16  4
# 60 >>> 10  40  10

s = int (input('Введите общее количество журавликов, s = '))

piter_cranes  = round(s / 6)
serge_cranes = round(s / 6)
cate_cranes = round(s * 2 / 3)

print(f'Петя, Катя и Сережа сделали по {piter_cranes}, {cate_cranes}, {serge_cranes} журавликов соответственно')