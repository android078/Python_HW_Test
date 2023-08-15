from datetime import datetime
import os

from Note import Note


index = -1


# -------------- вывод рабочего списка в консоль ------------------------
def printArray(arr):
    print()
    print(
        "======================================================================================================="
    )
    for i in range(0, len(arr)):
        outString(arr[i])
        # print("i = ", i)


# -------------- сборка строки из рабочего списка для вывода в консоль ------------------------
def outString(n_):
    print(
        "id: ",
        str(n_.id),
        "  ",
        str(n_.date_mark),
        "  ",
        str(n_.time_mark),
        " Заголовок: ",
        str(n_.title),
        "  Заметка: ",
        str(n_.body),
    )


# -------------- редактирование заметки ------------------------
def editNote(arr, item):
    newTitle = input("Введите новое название заголовка: ")
    newBody = input("Введите новый текст заметки: ")
    item.title = newTitle
    item.body = newBody
    arr = rebuildArr(arr)
    return arr


# -------------- добавление заметки ------------------------
# дата и время сохраняются в строковом виде dd.mm.yyyy и hh:mm:ss
def addNote(arr):
    newTitle = input("Введите заголовок новой заметки: ")
    newBody = input("Введите текст новой заметки: ")
    newDate_mark = (
        str("{:02d}".format(datetime.now().day))
        + "."
        + str("{:02d}".format(datetime.now().month))
        + "."
        + str("{:4d}".format(datetime.now().year))
    )
    newTime_mark = (
        str("{:02d}".format(datetime.now().hour))
        + ":"
        + str(datetime.now().minute)
        + ":"
        + str(datetime.now().second)
    )
    newNote = Note(Note.units_num, newTitle, newBody, newDate_mark, newTime_mark)
    arr.append(newNote)
    arr = rebuildArr(arr)
    return arr


# -------------- перестроение рабочего списка (коррекция полей Note.id) ------------------------
def rebuildArr(arr):
    workId = 0
    for i in range(0, len(arr)):
        # workId += 1
        arr[i].id = i + 1
    return arr


# -------------- поиск индекса заметки ------------------------------------------------------
# (значения всех полей экземпляра Note собираются в одну строку, далее идет поиск вхождения поискового шаблона в строку
# и по введенному пользователем id метод возвращает индекс записи в главном рабочем списке)
def findNote(arr):
    index = -1
    print()
    findStr = str(
        input(
            "Введите любую часть содержимого заметки (из любого поля, включая дату или время ), несколько символов: "
        )
    )
    tempStr = ""
    tempArr = []
    for i in range(0, len(arr)):
        tempStr += str(arr[i].id) + " "
        tempStr += arr[i].title + " "
        tempStr += arr[i].body + " "
        tempStr += arr[i].date_mark + " "
        tempStr += arr[i].time_mark + " "

        if findStr.lower() in tempStr.lower():
            tempArr.append(arr[i])
        tempStr = ""

    print()
    if len(tempArr) > 0:
        print("Найдено " + str(len(tempArr)) + " похожих записей:")

        for i in range(0, len(tempArr)):
            print(
                "id: ",
                tempArr[i].id,
                " ",
                tempArr[i].title,
                " ",
                tempArr[i].body,
                " ",
                tempArr[i].date_mark,
                " ",
                tempArr[i].time_mark,
                # " ",
            )
        print()
        findId = input("Введите id нужной заметки (цифра в начале строки): ")
        out = False
        for i in range(0, len(arr)):
            if findId == str(arr[i].id):
                index = i
                break
        if index == -1:
            print("Заметка с таким id не найдена")
            pauseIt()
            # break

    else:
        print("Похожих записей не найдено")
        pauseIt()
    return index


# --------------------------- метод приостановки программы ------------------------
def pauseIt():
    str = input("...... press 'Enter', please ...............")


# --------------------------- формирование начального меню ------------------------
def promptMenu():
    print()
    print()
    print()
    print("==================================================")
    print("Выберите пункт меню, нажав соответствующую цифру и Enter.")
    print("1. Найти заметку/Изменить заметку/Удалить заметку")
    print("2. Вывести полный список заметок")
    print("3. Добавить новую заметку")
    print("Q/q - Выйти из программы")


# "Перемотка" экрана
def scrollIt():
    for i in range(0, 50):
        print()


# ======================================================================================================
# Функция главного меню ==================================
# принимает рабочий список, внутри модуля вся работа ведется с ним
def main_Menu(fileContent):
    tempList = list()
    getOut = False  # флаг для выхода из меню
    while getOut != True:
        scrollIt()
        os.system("CLS")
        printArray(fileContent)

        promptMenu()
        choice = input("Ваш выбор: ")
        choice = choice.lower()
        if choice == "Q" or choice == "q" or choice == "й" or choice == "Й":
            getOut = True
            print()
            print("До свидания")
            print()
        if choice == "1":
            index = findNote(fileContent)
            if index != -1:
                print()
                print(
                    "Выбрана запись: ",
                    "id: ",
                    str(fileContent[index].id),
                    "  ",
                    str(fileContent[index].date_mark),
                    "  ",
                    str(fileContent[index].time_mark),
                    " Заголовок: ",
                    str(fileContent[index].title),
                    "  Заметка: ",
                    str(fileContent[index].body),
                )
                print()
                print("Ведите цифру, соответствующую необходимому действию,")
                print("'1' - Редактировать")
                print("'2' - Удалить")
                print("Клавиша 'Enter' - Выйти из редактирования")
                action = input("Ваш выбор: ")
                print()
                if action == "1":
                    arr = editNote(fileContent, fileContent[index])
                    printArray(fileContent)
                elif action == "2":
                    fileContent.pop(index)
                    rebuildArr(fileContent)
                    printArray(fileContent)
                    print("len(fileContent) = ", len(fileContent))
                elif action == "":
                    getOut = True
                else:
                    print("Что-то пошло не так")
                    pauseIt()
                    break

        if choice == "2":
            printArray(fileContent)

        if choice == "3":
            fileContent = addNote(fileContent)

    return fileContent