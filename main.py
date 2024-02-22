from tkinter import *
import math
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
def reset_counter():
    pass


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_countdown():
    counter = 60 * 3
    count_down(counter)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(counter):
    min_count = math.floor(counter / 60)
    sec_count = counter % 60
    # if min_count >= 0 and sec_count < 10:
    #     sec_count = f'0{sec_count}'
    # if min_count > 0 and sec_count == 0:
    #     sec_count = '00'
    if sec_count < 10:
        sec_count = f'0{sec_count}'
    canvas.itemconfig(timer_text, text=f'{min_count}:{sec_count}')
    if counter > 0:
        window.after(1000, count_down, counter - 1)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Pomodoro')
window.config(padx=100, pady=50, bg=YELLOW)

tomato_img = PhotoImage(file='./tomato.png')

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text='00:00', fill='white', font=(FONT_NAME, 35, 'bold'))
canvas.grid(column=1, row=1)

timer_label = Label(text='Timer', fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
timer_label.grid(column=1, row=0)

check_mark_label = Label(text="✓", bg=YELLOW, fg=GREEN)
check_mark_label.grid(column=1, row=3)

start_button = Button(text='Start', highlightthickness=0, command=start_countdown)
start_button.grid(column=0, row=2)

reset_button = Button(text='Reset', highlightthickness=0)
reset_button.grid(column=2, row=2)

window.mainloop()
