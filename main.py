import tkinter
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
reps = 0
checks = ""
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset():
    window.after_cancel(timer)
    title_lable.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    global checks
    checks = ""
    check_marks.config(text=checks)
    global reps 
    reps= 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start():
    global reps
    reps += 1

    work = WORK_MIN * 60
    short = SHORT_BREAK_MIN * 60
    long = LONG_BREAK_MIN * 60

    if reps % 2 == 0:
        count_down(short)
        title_lable.config(text="Short Break", fg=RED)
    elif reps % 8 == 0:
        count_down(long)
        title_lable.config(text="Long Break", fg=PINK)
    else:
        count_down(work)
        title_lable.config(text="Work", fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):

    min = math.floor(count / 60)
    sec = count % 60
    if sec < 10:
        sec = f"0{sec}"

    canvas.itemconfig(timer_text, text=f"{min}:{sec}")
    if count > 0:
        global timer
        timer = window.after(2, count_down, count - 1)
    else:
        start()
        global checks
        if reps % 2 == 0:
            checks += "✓"
            check_marks.config(text=checks)
   
# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=100, bg=YELLOW)

canvas = tkinter.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = tkinter.PhotoImage(file="C:/Users/kev51\Documents/VSCode/Day 28 - Tkinter, Dynamic Typing and the Pomodoro GUI Application/tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1,column=1)

title_lable = tkinter.Label(text="Timer",font=(FONT_NAME, 32, "bold"),fg=GREEN, bg=YELLOW, highlightthickness=0)
title_lable.grid(row=0,column=1)

start_button = tkinter.Button(text="Start", command=start)
start_button.grid(row=2,column=0)

reset_button = tkinter.Button(text="Reset", command=reset)
reset_button.grid(row=2,column=2)

check_marks = tkinter.Label(font=64,fg=GREEN, bg=YELLOW, highlightthickness=0)
check_marks.grid(row=3,column=1)

window.mainloop()
