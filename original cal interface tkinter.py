import tkinter as tk
from tkinter import messagebox

# Function to handle button clicks
def button_click(value):
    current_text = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current_text + value)

# Function to clear the display
def clear_display():
    entry.delete(0, tk.END)

# Function to calculate the result
def calculate():
    try:
        current_text = entry.get()
        result = eval(current_text)  # eval is used for simplicity, but use with caution
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception as e:
        messagebox.showerror("Error", f"Invalid input: {e}")

# Create the main application window
app = tk.Tk()
app.title("Calculator")
app.geometry("480x480")

# Create and place the display entry widget
entry = tk.Entry(app, width=16, font=('Arial', 24), bd=10, insertwidth=4, bg="powder blue", justify='right')
entry.grid(row=0, column=0, columnspan=4)

# Define buttons
buttons = [
    '7', '8', '9', '/', 
    '4', '5', '6', '*', 
    '1', '2', '3', '-', 
    '0', '.', '=', '+'
]

# Create and place buttons in the window
row_val = 1
col_val = 0

for button in buttons:
    if button == "=":
        tk.Button(app, text=button, padx=20, pady=20, bd=8, fg="black", font=('Arial', 18, 'bold'),
                  command=calculate).grid(row=row_val, column=col_val, columnspan=2)
    else:
        tk.Button(app, text=button, padx=20, pady=20, bd=8, fg="black", font=('Arial', 18, 'bold'),
                  command=lambda button=button: button_click(button)).grid(row=row_val, column=col_val)

    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Add Clear button
tk.Button(app, text='C', padx=20, pady=20, bd=8, fg="black", font=('Arial', 18, 'bold'),
          command=clear_display).grid(row=row_val, column=0, columnspan=2)

# Start the Tkinter event loop
app.mainloop()
