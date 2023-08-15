# Модуль, формирующий текстовый список записей

from Note import Note
import csv
import pathlib
from pathlib import Path

def makeArray(count):
    arr = []
    for i in range(1, count + 1):
        arr.append(
            Note("", "Заметка " + str(i) + ": ", "Текст заметки №" + str(i), "", "")
        )
    return arr


# Сохранение рабочего списка в файл
def saveToCSV(array, file):
    # Записываем массив экземпляров Note в файл с разделителем ';'
    dir_path = pathlib.Path.cwd()
    filePath = Path(dir_path, file)
    with open(filePath, "w", encoding="utf8", newline="") as file:
        writer = csv.writer(file, delimiter=";")
        writer.writerow(["id", "title", "body", "date_mark", "time_mark"])
        # Записываем заголовки столбцов
        for note in array:
            writer.writerow(
                [note.id, note.title, note.body, note.date_mark, note.time_mark]
            )  # Записываем значения заметок
    file.close()


# Чтение информации из файла
def readFromCSV(file):
    # Читаем данные из файла
    dir_path = pathlib.Path.cwd()
    filePath = Path(dir_path, file)
    with open(filePath, "r", encoding="utf8") as file:
        if FileExistsError == False:
            print("Файл не найден")
            notes_from = []
        reader = csv.reader(file, delimiter=";")
        notes_from = []
        # next(reader)  
        # Пропускаем заголовки столбцов
        for row in reader:
            id, title, body, date_mark, time_mark = row
            note = Note(id, title, body, date_mark, time_mark)
            notes_from.append(note)
    print("Прочитано заметок: ", str(len(notes_from)))
    Note.units_num = len(notes_from)
    file.close()
    return notes_from
    