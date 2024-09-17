import tkinter as tk

def show_input():
    label.config(text=f"You entered: {entry.get()}")

# Create the main window
root = tk.Tk()
root.title("Entry Example")

# Create an Entry widget
entry = tk.Entry(root)
entry.pack()

# Create a button
button = tk.Button(root, text="Submit", command=show_input)
button.pack()

# Create a label to display the input
label = tk.Label(root, text="")
label.pack()

# Start the GUI event loop
root.mainloop()