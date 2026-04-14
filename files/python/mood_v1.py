## mood.py (basic) 14-04-2026 15:08

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