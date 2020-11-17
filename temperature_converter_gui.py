import tkinter as tk
window = tk.Tk()
text = tk.Label(
    text="Python rocks!", 
    background="blue",
    fg="white",
    height=10,
    width=60
)

button = tk.Button(
    text = "Click me!",
    width = 25,
    height = 5,
    bg="blue",
    fg="yellow"
)

entry = tk.Entry(
    fg="yellow",
    bg="blue",
    width=50
)

entry.pack()
text.pack()


print("{}".format(name))

window.mainloop()