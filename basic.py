import tkinter

root = tkinter.Tk()

# The TK in Tkinter is for TK, which is
# a widget library for the TCL language.

hi_there = tkinter.Label(
    root,
    text="Hi there!!",
    bg="red",
    fg="white"

)

hi_there.pack(fill=tkinter.BOTH, expand=True)