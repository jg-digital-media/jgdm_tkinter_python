# jgdm_tkinter_python - `Last Update: 14-04-2026 11:43`

## Tkinter in Python: Mood Tracker App 

### Sections 

+  [Setup](#setup) | [Project Files](#project-files) | [Code](#code) | [Links](#links)

### Setup
[Back to Top](#jgdm_tkinter_python)

+ This project requires Python and Version Control to be installed on your system.

+ Use the command `git clone https://github.com/jg-digital-media/jgdm_tkinter_python.git` to install this project to your system.

You will need to use a Terminal or Command Line Interface to run the files with python.

+ `python -version`

If Python is installed to your system you will see a message like 

+ `python`

Use this command to enter the python shell and try our Tkinter projects on your own

+ `python filename.py` to run the specified file

### Project Files
[Back to Top](#jgdm_tkinter_python)

  + ### Hello World - ```hello.py```

  + ### Basic - ```basic.py```

  + ### Temperature Calculator - ```temp.py```

  + ### Mood Tracker - ```mood.py```

Source: [Link](https://realpython.com/python-gui-tkinter/)

### Code
[Back to Top](#jgdm_tkinter_python)

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

##### `Add a label to the title frame`

```python

### Add a label to the title frame

tk.Label(
    title_frame,
    text="Tkinter Mood Tracker",
    font=("Arial", 16)
).pack()

```

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
        button.config(bg="lightblue"

```

#### 

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

##### `mood.py`

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



## create and displat the label frame
tk.Label(
    title_frame,
    text="Tkinter Mood Tracker",
    font=("Arial", 16)
).pack()

# Run the app
root.mainloop()

```

### Links 
[Back to Top](#jgdm_tkinter_python)

- [Tkinter Tutorial](https://realpython.com/python-gui-tkinter/)
- [Tkinter Documentation](https://docs.python.org/3/library/tkinter.html)
- [W3Schools Tkinter Tutorial](https://www.w3schools.com/python/ref_module_tkinter.asp)
