# №8.1[49]. Создать телефонный справочник с возможностью импорта и экспорта данных в формате .csv
# Информация о человеке:
#     Фамилия, Имя, Телефон, Описание
# Корректность и уникальность данных не обязательны.
# Функционал программы
# 1) телефонный справочник хранится в памяти в процессе выполнения кода. 
#     Выберите наиболее удобную структуру данных для хранения справочника.
# 2) CRUD: Create, Read, Update, Delete
#     Create: Создание новой записи в справочнике: ввод всех полей новой записи, занесение ее в справочник.
#     Read: он же Select. Выбор записей, удовлетворяющих заданном фильтру: по первой части фамилии человека. 
    #   Берем первое совпадение по фамилии.
#     Update: Изменение полей выбранной записи. Выбор записи как и в Read, заполнение новыми значениями.
#     Delete: Удаление записи из справочника. Выбор - как в Read.
# 3) экспорт данных в текстовый файл формата csv
# 4) импорт данных из текстового файла формата csv


# Используйте функции для реализации значимых действий в программе
# Усложнение.

# - Сделать тесты для функций
# - Разделить на model-view-controller

# phone_book = [["Иванов", "Иван", "890001111111", "друг"], ["Петров", "Иван", "890002222222", "враг"]]

phone_book = []

def menu(data: list):
    while True:
        print ("Возможно выполнение следующих действий: ")
        print ("1 - создать новую запись")
        print ("2 - распечатать содержимое справочника")
        print ("3 - импортировать данные из текстового файла")
        print ("4 - экспортировать данные в текстовый файл")
        print ("5 - печать записи, выбранной по первой части фамилии")
        print ("6 - изменение записи, выбранной по первой части фамилии")
        print ("7 - удаление записи, выбранной по первой части фамилии")
        print ("Для выхода из программы нажмите пробел")
        get = input ("Выберите действие и нажмите Ввод: ")
        if get == " ":
            print("До свидания!")
            break
        elif get == "1":
            data = create(data, get_data())
        elif get == "2":
            print_phone_book(data)
        elif get == "3":
            name_file = get_file_name()
            batch_data = get_batch_data(name_file)
            data = batch_create(data, batch_data)
        elif get == "4":
            name_file = get_file_name()
            write_batch_data(data, name_file)
        elif get == "5":
            selected_data = read_select_data(data, get_select_string())
            if selected_data == None:
                print('Нет такой фамилии')
            else:
                print_phone_book([selected_data])   
        elif get == "6":
            print("Введите новые данные:")
            update_data = get_data()
            update_select_data(data, get_select_string (), update_data)
        elif get == "7":
            delete_select_data(data, get_select_string ())    
        else:
            print("Некорректный ввод данных. Выберите действие: ")

def create(data: list, element: list) -> list:  # добавляет запись в существующую телефонную книгу
    data.append(element)
    return data

def print_phone_book(data: list) -> None:
    for i in range (len(data)):
        print(i + 1, end = " ")
        print(*data[i], end = '\n')

def get_data ():
    surname = (input ("Введите фамилию: ")).replace("#","")
    name = (input ("Введите имя: ")).replace("#","")
    phone = (input ("Введите телефон: ")).replace("#","")
    description = (input ("Введите описание: ")).replace("#","")
    return [surname, name, phone, description]

def get_file_name() -> str:
    return input("Введите имя файла: ")

def get_batch_data(file_name: str) -> list:
    lst = []
    with open(file_name, 'r', encoding="utf-8") as file:
        for line in file:
            lst.append(line.strip('\n').split("#"))
    return lst

def batch_create(data: list, batch_data) -> list:
    for element in batch_data:
        data = create(data, element)
    return data

def write_batch_data(data:list, file_name: str) -> None:
    with open(file_name, 'w', encoding="utf-8") as file_write:
        for surname, name, phone, description in data:
            template = f'{surname}#{name}#{phone}#{description}\n'
            file_write.write(template) 

def read_select_data (data:list, select_string: str) -> list:
    for i in range (len(data)):
        if select_string.lower() in data[i][0].lower():
            return(data[i])
    return None

def get_select_string() -> str:
    select_string = input("Введите первую часть фамилии: ")
    return select_string
 
def update_select_data(data:list, select_string: str, update_data) -> list:
    for i in range (len(data)):
        if select_string.lower() in data[i][0].lower():
           data[i] = update_data
           return(data)
    print('Нет такой фамилии')
    return(data)

def delete_select_data(data:list, select_string: str) -> list:
    for i in range (len(data)):
        if select_string.lower() in data[i][0].lower():
            data.pop(i)
            return(data)
    print('Нет такой фамилии')
    return(data)
    

menu(phone_book)


 