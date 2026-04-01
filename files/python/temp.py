# Temp.py - Temperature Calculator
# Src: https://realpython.com/python-gui-tkinter/#building-a-temperature-converter-example-app

import tkinter as tk

# Functions

# The fahrenheit to celsiys calculator
def fahrenheit_to_celsius():

    # raise value error when text is entered
    try:
        fa = ent_temperature.get()
    
        ce = (5/9) * (float( fa ) - 32)
        lbl_result["text"] = f"{round(ce, 2)} \N{DEGREE CELSIUS}"
    except  ValueError:
        print("Error: please enter a number")
        lbl_result["text"] = "Error: Please enter a number"

window = tk.Tk()
window.title("Temperature Converter")
window.resizable(width=False, height=False)


frm_entry = tk.Frame(master=window)
ent_temperature = tk.Entry(master=frm_entry, width=10)
lbl_temp = tk.Label(master=frm_entry, text="\N{DEGREE FAHRENHEIT}")
lbl_title = tk.Label(master=window, text = "Temperature Calculator")

ent_temperature.grid(row=0, column=0, sticky="e")
lbl_temp.grid(row=0, column=1, sticky="w")

btn_convert = tk.Button(
    master=window,
    text= "\N{RIGHTWARDS BLACK ARROW}",
    command=fahrenheit_to_celsius

)



lbl_result = tk.Label(master=window, text="\N{DEGREE CELSIUS}")


lbl_title.grid(row=0, column=1, padx=0)
frm_entry.grid(row=1, column=0, padx=10)
btn_convert.grid(row=1, column=1, pady=10)
lbl_result.grid(row=1, column=2, padx=10)

window.mainloop()