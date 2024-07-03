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
reps = 0
check_mark_count = 0
clock_timer = NONE


# ---------------------------- TIMER RESET ------------------------------- #

def reset():
    global reps
    window.after_cancel(clock_timer)
    # Timer Label(work, break or long break)
    timer.config(text="Timer")
    # Time
    canvas.itemconfig(timer_text, text=f"00:00")
    # checkmarks
    check_mark.config(text="")
    # reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps, check_mark_count
    task = 0
    if reps < 7:
        if reps % 2 == 0:
            timer.config(text="Work", fg=RED)
            task = WORK_MIN
        else:
            check_mark_count += 1
            timer.config(text="Break", fg=GREEN)
            task = SHORT_BREAK_MIN
        reps += 1
    elif reps == 7:
        timer.config(text="Work", fg=PINK)
        task = LONG_BREAK_MIN
    countdown(task * 60)


# tie this command to the start button to get the button functional


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


# 'after' method is a method in which two parameters needs to be asked. the time(in milliseconds) required to wait
# and the function
# that needs to be called after that amount of particular time.
# that function may have infinite amount of arguments(*args)

# for ex:

# def something(a, b ,c):
#     print(a)
#     print(b)
#     print(c)

# # will print the below numbers in 1 second interval
# window.after(1000, something, 4, 6, 7)

# for changing a particular text in canvas which is timer text in this case you have to use syntax in the following way
def countdown(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global clock_timer
        clock_timer = window.after(1000, countdown, count - 1)
    else:
        start_timer()
        for i in range(check_mark_count):
             check_mark.config(text=cm)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

cm = "✓"
tomato_img = PhotoImage(file="tomato.png")

timer = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
timer.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
# After setting the background color, there a exists a white border.
# To remove it a parameter named highlightthickness is set to 0.
# Hint use the fg to color the foreground
canvas.create_image(100, 112, image=tomato_img, )
timer_text = canvas.create_text(100, 130, text="00:00", fill="White", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", highlightthickness=0, command=reset)
reset_button.grid(column=2, row=2)

check_mark = Label(text="")
check_mark.grid(column=1, row=3)
window.mainloop()
