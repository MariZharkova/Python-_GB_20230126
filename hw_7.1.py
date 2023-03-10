# 7.1[34]: Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм.
# Поскольку разобраться в его кричалках не настолько просто, насколько легко он их придумывает,
# Вам стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов
# (т.е. число гласных букв) в каждой фразе стихотворения одинаковое.
# Фраза может состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами.
# Фразы отделяются друг от друга пробелами.

# # Написать функцию, которая принимает строку текста и проверяет ее ритм (по Винни-Пуху)
# Если ритм есть, функция возвращает True, иначе возвращает False

# Примеры/Тесты:
#     <function_name>("пара-ра-рам рам-пам-папам па-ра-па-дам") -> True
#     <function_name>("пара-ра-рам рам-пум-пупам па-ре-по-дам") -> True
#     <function_name>("пара-ра-рам рам-пуум-пупам па-ре-по-дам") -> False
#     <function_name>("Трам-пара-папам-парам-па-пам-пам-па Пум-пурум-пу-пурум-трам-пам-па") -> False
#     <function_name>("Пам-парам-пурум Пум-пурум-карам") -> True

# Примечание.

#     Подумайте об эффективности алгоритма. Какие структуры данных будут более эффективны по скорости.
#     Алгоритм должен работать так, чтобы не делать лишних проверок.
#   Подумайте, возможно некоторые проверки не нужны.

# (*) Усложнение.

# Функция имеет параметр, который определяет, надо ли возвращать полную информацию о кол-ве гласных букв в фразах.
# Эта информация возвращается в виде списка словарей. Каждый элемент списка(словарь) соответствует фразе.

# Примеры/Тесты:
#     <function_name>("пара-ра-рам рам-пам-папам па-ра-па-дам", False) -> True
#     <function_name>("пара-ра-рам рам-пам-папам па-ра-па-дам", True) -> (True, [{'а': 4}, {'а': 4}, {'а': 4}])
#     <function_name>("пара-ра-рам рам-пум-пупам па-ре-по-дам") -> (True, [{'а': 4}, {'а': 2, 'у': 2}, {'а': 2, 'е': 1, 'о': 1}])
#     <function_name>("пара-ра-рам рам-пуум-пупам па-ре-по-дам") -> (False, [{'а': 4}, {'а': 2, 'у': 3}])
#     <function_name>("Трам-пара-папам-парам-па-пам-пам-па Пум-пурум-пу-пурум-трам-пам-па") -> (False, [{'а': 11}, {'у': 6, 'а': 3}])
#     <function_name>("Пам-парам-пурум Пум-пурум-карам") -> (True, [{'а': 3, 'у': 2}, {'у': 3, 'а': 2}])


frase = "пара-ра-рам рам-пам-папам па-ра-па-дам"  # true
# frase = "пара-ра-рам рам-пум-пупам па-ре-по-дам"  #true
# frase = "пара-ра-рам рам-пуум-пупам па-ре-по-дам" #false
# frase = "Трам-пара-папам-парам-па-пам-пам-па Пум-пурум-пу-пурум-трам-пам-па"    #false
# frase = "Пам-парам-пурум Пум-пурум-карам"   #true


def is_rithm_in_frase(phrase, is_print = True):
    vowels = {'а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я'}
    phrase = phrase.split()
    count_vowels = []
    info = []
    for i in range(0, len(phrase)):
        dict  = {}
        count = 0
        for el in phrase[i]:
            count += 1
            if el in vowels:
                if el in dict:
                    dict[el] = dict[el] + 1
                else:
                    dict[el] = 1
        count_vowels.append(count)
        info.append(dict)
    result = len(set(count_vowels)) == 1
    if is_print:
        print(f"({result}, {info})")
    else:
        print(result)

is_rithm_in_frase("пара-ра-рам рам-пам-папам па-ра-па-дам", False) # True
# is_rithm_in_frase("пара-ра-рам рам-пам-папам па-ра-па-дам", True)  # (True, [{'а': 4}, {'а': 4}, {'а': 4}])
# is_rithm_in_frase("пара-ра-рам рам-пам-папам па-ра-па-дам", True)    # (True, [{'а': 4}, {'а': 4}, {'а': 4}])
# is_rithm_in_frase("пара-ра-рам рам-пум-пупам па-ре-по-дам")   # (True, [{'а': 4}, {'а': 2, 'у': 2}, {'а': 2, 'е': 1, 'о': 1}])
# is_rithm_in_frase("пара-ра-рам рам-пуум-пупам па-ре-по-дам") # (False, [{'а': 4}, {'а': 2, 'у': 3}])
# is_rithm_in_frase("Трам-пара-папам-парам-па-пам-пам-па Пум-пурум-пу-пурум-трам-пам-па")  # (False, [{'а': 11}, {'у': 6, 'а': 3}])
# is_rithm_in_frase("Пам-парам-пурум Пум-пурум-карам")   #  (True, [{'а': 3, 'у': 2}, {'у': 3, 'а': 2}])

