from tkinter import *

# Create the main window
w = Tk()
w.title("Arithmetic Calculator")
w.geometry('800x200')

def calculate():
    # Get the numbers from the entries
    try:
        num1 = float(e1.get())
        num2 = float(e2.get())
    except ValueError:
        result_label.config(text="Please enter valid numbers.")
        return
    
    # Get the selected operation
    operation = operation_var.get()
    
    # Perform the selected operation
    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        if num2 == 0:
            result_label.config(text="Cannot divide by zero.")
            return
        result = num1 / num2
    else:
        result_label.config(text="Please select an operation.")
        return
    
    # Update the result label
    result_label.config(text=f"Result: {result}")

# First number label and entry
l1 = Label(w, text="Number 1:")
l1.grid(row=0, column=0, padx=10, pady=5)

e1 = Entry(w)
e1.grid(row=0, column=1, padx=10, pady=5)

# Second number label and entry
l2 = Label(w, text="Number 2:")
l2.grid(row=1, column=0, padx=10, pady=5)

e2 = Entry(w)
e2.grid(row=1, column=1, padx=10, pady=5)

# Operation label and radio buttons
operation_var = StringVar()
operation_var.set("+")

l3 = Label(w, text="Operation:")
l3.grid(row=2, column=0, padx=10, pady=5)

operations_frame = Frame(w)
operations_frame.grid(row=2, column=1, padx=10, pady=5)

radio_add = Radiobutton(operations_frame, text="+", variable=operation_var, value="+")
radio_add.pack(side=LEFT)

radio_subtract = Radiobutton(operations_frame, text="-", variable=operation_var, value="-")
radio_subtract.pack(side=LEFT)

radio_multiply = Radiobutton(operations_frame, text="*", variable=operation_var, value="*")
radio_multiply.pack(side=LEFT)

radio_divide = Radiobutton(operations_frame, text="/", variable=operation_var, value="/")
radio_divide.pack(side=LEFT)

# Submit button
submit_button = Button(w, text="Calculate", command=calculate)
submit_button.grid(row=3, column=0, columnspan=2, pady=10)

# Label to show the result
result_label = Label(w, text="Result: ")
result_label.grid(row=4, column=0, columnspan=2, pady=5)

w.mainloop()