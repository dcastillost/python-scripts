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

# WORK_ITER = [1, 3, 5, 7]
# SHORT_BREAK_ITER = [2, 4, 6]
# LONG_BREAK_ITER = [8]

timer = None
timer_iter = 0

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global timer_iter
    window.after_cancel(timer)
    timer_iter = 0
    title_label.config(text='Timer', fg = GREEN)
    canvas.itemconfig(timer_text, text='00:00')
    checkmark_label.config(text='')

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global timer_iter
    timer_iter += 1

    work_sec = WORK_MIN*60
    short_break_sec = SHORT_BREAK_MIN*60
    long_break_sec = LONG_BREAK_MIN*60 

    if timer_iter % 8 == 0:
        title_label.config(text='Break', fg = RED)
        countdown(long_break_sec)
    elif timer_iter % 2 == 0:
        title_label.config(text='Break', fg = PINK)
        countdown(short_break_sec)
    else:
        title_label.config(text='Work', fg = GREEN)
        countdown(work_sec)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):
    global timer
    minutes = count // 60
    seconds = count % 60
    canvas.itemconfig(timer_text, text='{:02d}:{:02d}'.format(minutes, seconds))
    if count > 0:
        timer = window.after(1000, countdown, count - 1)
    else:
        start_timer()
        marks = ''
        work_sessions = timer_iter // 2
        for _ in range(work_sessions):
            marks += '✔'
        checkmark_label.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Pomodoro timer')
window.config(padx=100, pady=50, bg=YELLOW)

# Labels
title_label = Label(text='Timer', fg=GREEN, bg=YELLOW, font=(FONT_NAME, 40, 'bold'))
title_label.grid(row=0, column=1)

checkmark_label = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20))
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

