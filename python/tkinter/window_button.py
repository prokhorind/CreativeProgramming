import tkinter as tk

def on_click():
    label.config(text="Button Clicked!")

# Create the main window
root = tk.Tk()
root.title("Label and Button")

# Add a label
label = tk.Label(root, text="Hello, Tkinter!")
label.pack()

# Add a button
button = tk.Button(root, text="Click Me", command=on_click)
button.pack()

# Start the GUI event loop
root.mainloop()