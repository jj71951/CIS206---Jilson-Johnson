import tkinter as tk
from tkinter import messagebox

# Function to handle button click
def calculate_square():
    # Retrieve inputs
    name = name_entry.get()
    number_input = number_entry.get()

    # Validate numeric input
    try:
        number = float(number_input)  # Convert to float to handle decimals
    except ValueError:
        # Show error if not a number
        messagebox.showerror("Input Error", "Please enter a valid numeric value.")
        return

    # Perform calculation
    result = number ** 2

    # Display result in a label
    result_label.config(text=f"Hi {name}, the square of {number} is {result}")

# Create main window
root = tk.Tk()
root.title("Data Entry and Calculation Form")

# Form description
description_label = tk.Label(root, text="Enter your name and a number to calculate its square:", font=("Arial", 12))
description_label.pack(pady=10)

# Name entry
name_label = tk.Label(root, text="Name:")
name_label.pack()
name_entry = tk.Entry(root, width=30)
name_entry.pack()

# Number entry
number_label = tk.Label(root, text="Number:")
number_label.pack()
number_entry = tk.Entry(root, width=30)
number_entry.pack()

# Calculate button
calculate_button = tk.Button(root, text="Calculate Square", command=calculate_square)
calculate_button.pack(pady=10)

# Result display
result_label = tk.Label(root, text="", font=("Arial", 12), fg="green")
result_label.pack(pady=10)

# Run the main event loop
root.mainloop()
