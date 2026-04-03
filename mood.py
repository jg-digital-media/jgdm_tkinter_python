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


tk.Label(
    title_frame,
    text="Tkinter Mood Tracker",
    font=("Arial", 16)
).pack()

# Run the app
root.mainloop()