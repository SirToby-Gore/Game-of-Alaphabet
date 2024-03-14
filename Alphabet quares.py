import tkinter as tk
import random
import time
import AlLog
import AlUI

def try_type(inp, typ):
    try:
        return typ(inp)
    except (ValueError, TypeError):
        return None


x = try_type(input("Enter the size of the 2D array: "), int) or 6
inp = (try_type(input("Use random letters? y/n: "), str) or "Y").upper()

if inp == "N":
    array = AlLog.selected_n(x)
else:
    if (try_type(input("choice chance of blank space? y/n: "), str) or "N").upper() == "Y":
        chance = (try_type(input("Higher the number  more blanks you get? 0-1: "), float) or 0)
        array = AlLog.list_creator(x, chance)
    array = AlLog.list_creator(x)

print(array)

root = AlUI.create_window(array)

while True:
    old_array = array
    is_same = False
    if old_array != array:
        is_same = False
    else:
        is_same = True
    array = AlLog.logic_1(array)
    array[0] = [""]*(x+2)
    for i in array:
        i[0], i[len(i)-1] = "", ""
    array[len(array)-1] = [""]*(x+2)
    AlUI.update_display(array, root, is_same)
