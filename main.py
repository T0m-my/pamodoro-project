from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 2
reps = 0
check_marks = ''
timer = None
is_break_time = False


# --------------------------COMPUTE TIME, TOGGLE WORK/BREAK ------------------- #
def calc_time(num_of_min, sixty_sec=60):
    global is_break_time
    is_break_time = not is_break_time

    return sixty_sec * num_of_min


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global check_marks, is_break_time
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text='00:00')
    timer_label.config(text='Timer', fg=GREEN)
    check_marks = ''
    check_mark_label.config(text=check_marks)
    is_break_time = False


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps, is_break_time

    if is_break_time:
        count_down_min = SHORT_BREAK_MIN
        timer_label.config(text='Break', fg=PINK)
        if reps == 4:
            count_down_min = LONG_BREAK_MIN
            timer_label.config(fg=RED)
            reps = 0
    else:
        count_down_min = WORK_MIN
        timer_label.config(text='WORK', fg=GREEN)
        reps += 1

    counter = calc_time(count_down_min)
    count_down(counter)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(counter):
    min_count = math.floor(counter / 60)
    sec_count = counter % 60
    if sec_count < 10:
        sec_count = f'0{sec_count}'
    canvas.itemconfig(timer_text, text=f'{min_count}:{sec_count}')
    if counter > 0:
        global timer
        timer = window.after(1000, count_down, counter - 1)
    else:
        if is_break_time and reps > 0:
            global check_marks
            check_marks += '✓'
            check_mark_label.config(text=check_marks)
        start_timer()


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

check_mark_label = Label(bg=YELLOW, fg=GREEN)
check_mark_label.grid(column=1, row=3)

start_button = Button(text='Start', highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text='Reset', highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

window.mainloop()
