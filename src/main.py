import sys
from tkinter import *
from time import sleep, strftime
from tkinter import messagebox


# Screen Saver windows command-line arguments https://docs.microsoft.com/en-us/troubleshoot/windows/win32/screen-saver-command-line
if len(sys.argv) == 1:
    # ScreenSaver           - Show the Settings dialog box.
    messagebox.showinfo("Settings", "We don't have settings for now.")
    exit(0)

elif len(sys.argv) >= 2 and sys.argv[1].startswith("/c"):
    # ScreenSaver /c        - Show the Settings dialog box, modal to the foreground window.
    messagebox.showinfo("Settings", "We don't have settings for now.")
    exit(0)

elif len(sys.argv) >= 2 and sys.argv[1].startswith("/p"):
    # ScreenSaver /p <HWND> - Preview Screen Saver as child of window <HWND>.
    pass

elif len(sys.argv) >= 2 and sys.argv[1] == "/s":
    # ScreenSaver /s        - Run the Screen Saver.
    pass


# Main Window
root = Tk()

# Window Attributes
root.overrideredirect(True)
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
