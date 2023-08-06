from tkinter import *
from time import sleep, strftime

root = Tk()

# Window Attributes
root.overrideredirect(1)
root.wm_attributes("-transparentcolor", "gray99")

running = True


# close window
def close(event):
    global running
    running = False


root.bind("<Escape>", close)
root.bind("<Motion>", close)
root.bind("<Key>", close)

root.config(cursor="none")

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

timeframe = Frame(root, width=screen_width, height=screen_height, bg="Black")
timeframe.grid(row=0, column=0)

tkintertime = StringVar()
timelabel = Label(
    timeframe,
    textvariable=tkintertime,
    fg="#808080",
    bg="Black",
    font=("NovaMono", 150),
)
timelabel.place(y=screen_height / 2 - 60, x=screen_width / 2, anchor="center")

tkinterdate = StringVar()
datelabel = Label(
    timeframe,
    textvariable=tkinterdate,
    fg="#808080",
    bg="Black",
    font=("Bahnschrift", 30),
)
datelabel.place(y=screen_height / 2 + 60, x=screen_width / 2, anchor="center")

if __name__ == "__main__":
    while running:
        tkintertime.set(value=strftime("%H:%M:%S"))
        tkinterdate.set(value=strftime("%A, %e %B"))
        root.update_idletasks()
        root.update()
        sleep(1)
