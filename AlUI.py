import tkinter as tk
import random
import time

def create_window(array_2d):
    root = tk.Tk()
    root.title("Biggus dickus")
    root.configure(bg="black")

    return root


def display_labels(root, array_2d, delay=50, same=False):
    if array_2d is None or not array_2d:
        print("Error: array_2d is None or empty.")
        return

    if not all(isinstance(row, list) for row in array_2d) or not all(
        isinstance(item, (int, str)) for row in array_2d for item in row
    ):
        print("Error: Unexpected array_2d structure.")
        return

    bg_color = "dark red" if same else "black"
    

    count_delay = 0
    for i, row in enumerate(array_2d[1:-1]):
        for j, item in enumerate(row[1:-1]):
            label = tk.Label(
                root,
                text=str(item),
                font=("Helvetica", 16),
                width=5,
                height=2,
                relief="solid",
                borderwidth=1,
                fg="white",
                bg=bg_color,
            )
            label.grid(row=i, column=j, padx=2, pady=2)
            root.update()
            time.sleep(delay / 1000)
            
            if delay > 23:
                delay -= 3
            if count_delay > 100 and delay > 4:
                delay -= 3
            else:
                count_delay += 1
            if delay < 0:
                delay == 1


def update_display(array_2d, root, old_array):
    for widget in root.winfo_children():
        widget.destroy()
    same = array_2d == old_array
    display_labels(root, array_2d, same=same)
    time.sleep(0.2)


