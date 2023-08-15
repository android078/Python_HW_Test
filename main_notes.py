from menu import main_Menu
from Note import *
from dump import *
import os

os.system("CLS")
print()
print()
print()
print()

work_array = readFromCSV("notes.csv")
saveToCSV(work_array, "notes.bak")
print()
work_array = main_Menu(work_array)
saveToCSV(work_array, "notes.csv")
