import tkinter as tk
from tkinter import messagebox

# Calculator logic functions
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "invalid command"
    return x / y

# Function to handle button click and perform calculation
def calculate():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        operation = operation_var.get()

        if operation == "Add":
            result = add(num1, num2)
        elif operation == "Subtract":
            result = subtract(num1, num2)
        elif operation == "Multiply":
            result = multiply(num1, num2)
        elif operation == "Divide":
            result = divide(num1, num2)

        result_var.set(f"Result: {result}")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers.")

# Create the main application window
app = tk.Tk()
app.title("Simple Calculator")
app.geometry("480x480")

# Create and place widgets in the window
tk.Label(app, text="Number 1:").pack(pady=5)
entry1 = tk.Entry(app)
entry1.pack(pady=5)

tk.Label(app, text="Number 2:").pack(pady=5)
entry2 = tk.Entry(app)
entry2.pack(pady=5)

tk.Label(app, text="Operation:").pack(pady=5)
operation_var = tk.StringVar(value="Add")
operations = [("Add", "Add"), ("Subtract", "Subtract"), ("Multiply", "Multiply"), ("Divide", "Divide")]

for text, mode in operations:
    tk.Radiobutton(app, text=text, variable=operation_var, value=mode).pack(anchor=tk.W)

tk.Button(app, text="Calculate", command=calculate).pack(pady=20)

result_var = tk.StringVar()
tk.Label(app, textvariable=result_var).pack(pady=5)

# Start the Tkinter event loop
app.mainloop()
