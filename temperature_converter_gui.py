import tkinter as tk
window = tk.Tk()
text = tk.Label(
    text="Python rocks!", 
    background="blue",
    fg="white",
    height=10,
    width=60
)
text.pack()
window.mainloop()