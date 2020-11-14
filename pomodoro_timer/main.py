# ---------------------------- IMPORTS ------------------------------- #
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    pass

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    countdown(WORK_MIN*60)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):
    minutes = count // 60
    seconds = count % 60
    canvas.itemconfig(timer_text, text='{:02d}:{:02d}'.format(minutes,seconds))
    text=f''
    if count > 0:
        window.after(1000, countdown, count - 1)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Pomodoro timer')
window.config(padx=100, pady=50, bg=YELLOW)

# Labels
title_label = Label(text='Timer', fg=GREEN, bg=YELLOW, font=(FONT_NAME, 40, 'bold'))
title_label.grid(row=0, column=1)

checkmark_label = Label(text='✔', fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20))
checkmark_label.grid(row=3, column=1)

# Buttons
start_button = Button(text='start', bg=YELLOW, font=(FONT_NAME, 12), command=start_timer)
start_button.grid(row=2, column=0)

reset_button = Button(text='reset', bg=YELLOW, font=(FONT_NAME, 12), command=reset_timer)
reset_button.grid(row=2, column=2)

# Canvas
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 132, text='00:00', fill='white', font=(FONT_NAME, 35, 'bold'))
canvas.grid(row=1, column=1)

# Window loop
window.mainloop()

