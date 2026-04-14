# jgdm_tkinter_python - `Last Update: 14-04-2026 16:08`

## Tkinter in Python: Mood Tracker App 

### Sections 

+  [Setup](#setup) | [Project Files](#project-files) | [TODOs](#todos) | [Code](#code) | [Links](#links)

### Setup
[Back to Top](#)

+ This project requires Python and Version Control to be installed on your system. You will need to use a Terminal or Command Line Interface to run `mood.py` with Python.

+ Use the command `git clone https://github.com/jg-digital-media/jgdm_tkinter_python.git` to install this project to your system.

+ Run `python -version` to check python versions. If Python is installed to your system you will see a message like `Python 3.12.2`. Use this command to enter the python shell and try these Tkinter projects on your own `python filename.py` and run the specified file.

+ Pressing the Reset Button deletes the `data.json` file which holds the data and resets the app to its initial state.

### Project Files
[Back to Top](#)

  + ### Hello World - ```hello.py```

  + ### Basic - ```basic.py```

  + ### Temperature Calculator - ```temp.py```

  + ### Mood Tracker - ```mood.py```

Source: [Link](https://realpython.com/python-gui-tkinter/)

### TODOs


### Tasks `3` Completed `1` 

#### Python Tkinter Mood Tracker App

+ `TODO:` `COMPLETED: 14-04-2026` Build mood.py basic (v1) 
+ `TODO:` Persist Mood history data by loading existing data from `data.json` file on app start
+ `TODO:` Organise mood.py code


[Back to Top](#)

### Code
[Back to Top](#)

#### `Import the Tkinter module and run app`

```python

### Run a new Tkinter app

import tkinter as tk

root = tk.Tk()
root.title("Mood Tracker")
root.geometry("500x600")

# Run the app
root.mainloop()

```

+ Enter `python mood.py` in your command line/terminal.

[Back to Code](#code)

##### `Add a label to the title frame`

```python

### Add a label to the title frame

tk.Label(
    title_frame,
    text="Tkinter Mood Tracker",
    font=("Arial", 16)
).pack()

```
[Back to Code](#code)

##### `define moods`

```python

moods = ["Ecstatic", "Happy", "Neutral", "Low", "Very Sad"]
selected_moods = set()

def toggle_mood(mood, button):
    if mood in selected_moods:
        selected_moods.remove(mood)
        button.config(bg="SystemButtonFace")
    else:
        selected_moods.add(mood)
        button.config(bg="lightblue")

```
[Back to Code](#code)

#### `display mood buttons`
```python

# display mood buttons
for mood in moods:
    btn = tk.Button(
        mood_frame,
        text=mood,
        width=10
    )
    
    btn.config(command=lambda m=mood, b=btn: toggle_mood(m, b))
    btn.pack(side="left", padx=5)
```
[Back to Code](#code)

##### `function to toggle mood button state`

```python

def toggle_mood(mood, button):
    if mood in selected_moods:
        selected_moods.remove(mood)
        button.config(bg="SystemButtonFace")
    else:
        selected_moods.add(mood)
        button.config(bg="lightblue") 
```
[Back to Code](#code)

##### `define save and reset buttons`

```python
save_btn = tk.Button(action_frame, text="Save Mood", command=save_mood)
reset_btn = tk.Button(action_frame, text="Reset App", command=reset_app)

save_btn.pack(side="left", padx=10)
reset_btn.pack(side="left", padx=10)
```
[Back to Code](#code)

##### `function to save mood choice`

```python
def save_mood():

    if not selected_moods:
        return
    
    entry = {
        "date": str(date.today()),
        "moods": list(selected_moods)
    }

    try:
        with open("data.json", "r") as f:
            data = json.load(f)
    except:
        data = []

    data.append(entry)

    with open("data.json", "w") as f:
        json.dump(data, f, indent=2)

    #update_history()
    #update_summary()
```
[Back to Code](#code)

##### `Create mood history UI frame`

```python
history_list = tk.Listbox(history_frame)
history_list.pack(fill="both", expand=True)
```
[Back to Code](#code)

##### `function to update mood history`

```python
def update_history():
    history_list.delete(0, tk.END)

    try:
        with open("data.json", "r") as f:
            data = json.load(f)
    except:
        return

    for entry in data[-10:]:
        text = f"{entry['date']} - {', '.join(entry['moods'])}"
        history_list.insert(tk.END, text)
```
[Back to Code](#code)

##### `function to update mood history`

```python

def update_history():
    history_list.delete(0, tk.END)

    try:
        with open("data.json", "r") as f:
            data = json.load(f)
    except:
        return

    for entry in data[-10:]:
        text = f"{entry['date']} - {', '.join(entry['moods'])}"
        history_list.insert(tk.END, text)
```
[Back to Code](#code)

##### `Build mood summary frame content`

```python

summary_label = tk.Label(summary_frame, text="Summary will appear here")
summary_label.pack()

```
[Back to Code](#code)

##### `function to handle updates to mood summary` Build mood summary logic

```python

from collections import Counter
from datetime import datetime, timedelta

def update_summary():
    try:
        with open("data.json", "r") as f:
            data = json.load(f)
    except:
        return

    last_7_days = datetime.now() - timedelta(days=7)

    moods = []

    for entry in data:
        entry_date = datetime.fromisoformat(entry["date"])
        if entry_date >= last_7_days:
            moods.extend(entry["moods"])

    count = Counter(moods)

    summary_text = "\n".join([f"{k}: {v}" for k, v in count.items()])
    summary_label.config(text=summary_text)
```
[Back to Code](#code)

##### `function to handle reset of app`


```python

from tkinter import messagebox
import os

def reset_app():
    confirm = messagebox.askyesno("Confirm", "Reset all data?")
    
    if confirm:
        if os.path.exists("data.json"):
            os.remove("data.json")

        history_list.delete(0, tk.END)
        summary_label.config(text="")        
```
[Back to Code](#code)

##### App - `mood.py`

```python

import tkinter as tk

root = tk.Tk()
root.title("Mood Tracker")
root.geometry("500x600")

# Main sections
title_frame = tk.Frame(root)
mood_frame = tk.Frame(root)
action_frame = tk.Frame(root)
history_frame = tk.Frame(root)
summary_frame = tk.Frame(root)

title_frame.pack(fill="x", pady=10)
mood_frame.pack(fill="x", pady=10)
action_frame.pack(fill="x", pady=10)
history_frame.pack(fill="both", expand=True, pady=10)
summary_frame.pack(fill="x", pady=10)

# define moods
moods = ["Ecstatic", "Happy", "Neutral", "Low", "Very Sad"]
selected_moods = set()

# display mood buttons
for mood in moods:
    btn = tk.Button(
        mood_frame,
        text=mood,
        width=10
    )
    
    btn.config(command=lambda m=mood, b=btn: toggle_mood(m, b))
    btn.pack(side="left", padx=5)


# function to toggle mood button state
def toggle_mood(mood, button):
    if mood in selected_moods:
        selected_moods.remove(mood)
        button.config(bg="SystemButtonFace")
    else:
        selected_moods.add(mood)
        button.config(bg="lightblue") 

## create and display the label frame
tk.Label(
    title_frame,
    text="Tkinter Mood Tracker",
    font=("Arial", 16)
).pack()


import json
from datetime import date

## function to save mood choice
def save_mood():

    if not selected_moods:
        return
    
    entry = {
        "date": str(date.today()),
        "moods": list(selected_moods)
    }

    try:
        with open("data.json", "r") as f:
            data = json.load(f)
    except:
        data = []

    data.append(entry)

    with open("data.json", "w") as f:
        json.dump(data, f, indent=2)

    update_history()
    update_summary()

## function to update mood history
def update_history():
    history_list.delete(0, tk.END)

    try:
        with open("data.json", "r") as f:
            data = json.load(f)
    except:
        return

    for entry in data[-10:]:
        text = f"{entry['date']} - {', '.join(entry['moods'])}"
        history_list.insert(tk.END, text)

# Build mood summary frame content
summary_label = tk.Label(summary_frame, text="Summary will appear here")
summary_label.pack()

## function to handle updates to mood summary

from collections import Counter
from datetime import datetime, timedelta

def update_summary():
    try:
        with open("data.json", "r") as f:
            data = json.load(f)
    except:
        return

    last_7_days = datetime.now() - timedelta(days=7)

    moods = []

    for entry in data:
        entry_date = datetime.fromisoformat(entry["date"])
        if entry_date >= last_7_days:
            moods.extend(entry["moods"])

    count = Counter(moods)

    summary_text = "\n".join([f"{k}: {v}" for k, v in count.items()])
    summary_label.config(text=summary_text)


from tkinter import messagebox
import os

## function to handle reset of app
def reset_app():
    confirm = messagebox.askyesno("Confirm", "Reset all data?")
    
    if confirm:
        if os.path.exists("data.json"):
            os.remove("data.json")

        history_list.delete(0, tk.END)
        summary_label.config(text="")

## define save and reset buttons
save_btn = tk.Button(action_frame, text="Save Mood", command=save_mood)
reset_btn = tk.Button(action_frame, text="Reset App", command=reset_app)

save_btn.pack(side="left", padx=10)
reset_btn.pack(side="left", padx=10)


## Create mood history UI frame`
history_list = tk.Listbox(history_frame)
history_list.pack(fill="both", expand=True)


# Run the app
root.mainloop()

```
[Back to Code](#code)

### Links 
[Back to Top](#)

- [Tkinter Tutorial](https://realpython.com/python-gui-tkinter/)
- [Tkinter Documentation](https://docs.python.org/3/library/tkinter.html)
- [W3Schools Tkinter Tutorial](https://www.w3schools.com/python/ref_module_tkinter.asp)