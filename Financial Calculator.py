import tkinter as tk
from tkinter import ttk

def calculate_future_value():
    """Calculates the future value of an investment."""
    try:
        present_value = float(present_value_entry.get())
        interest_rate = float(interest_rate_entry.get()) / 100
        num_years = int(num_years_entry.get())

        future_value = present_value * (1 + interest_rate) ** num_years
        result_label.config(text=f"Future Value: ${future_value:.2f}")
    except ValueError:
        result_label.config(text="Invalid input. Please enter numbers only.")


def calculate_present_value():
    """Calculates the present value of an investment."""
    try:
        future_value = float(future_value_entry.get())
        interest_rate = float(interest_rate_entry.get()) / 100
        num_years = int(num_years_entry.get())

        present_value = future_value / (1 + interest_rate) ** num_years
        result_label.config(text=f"Present Value: ${present_value:.2f}")
    except ValueError:
        result_label.config(text="Invalid input. Please enter numbers only.")


# Create main window
window = tk.Tk()
window.title("Financial Calculator")

# --- Common Input Fields ---
# Labels and entry fields for present value, interest rate, and number of years
present_value_label = ttk.Label(window, text="Present Value:")
present_value_label.grid(row=0, column=0, padx=5, pady=5)
present_value_entry = ttk.Entry(window)
present_value_entry.grid(row=0, column=1, padx=5, pady=5)

future_value_label = ttk.Label(window, text="Future Value:")
future_value_label.grid(row=1, column=0, padx=5, pady=5)
future_value_entry = ttk.Entry(window)
future_value_entry.grid(row=1, column=1, padx=5, pady=5)

interest_rate_label = ttk.Label(window, text="Interest Rate (%):")
interest_rate_label.grid(row=2, column=0, padx=5, pady=5)
interest_rate_entry = ttk.Entry(window)
interest_rate_entry.grid(row=2, column=1, padx=5, pady=5)

num_years_label = ttk.Label(window, text="Number of Years:")
num_years_label.grid(row=3, column=0, padx=5, pady=5)
num_years_entry = ttk.Entry(window)
num_years_entry.grid(row=3, column=1, padx=5, pady=5)

# --- Buttons ---
calculate_fv_button = ttk.Button(window, text="Calculate FV", command=calculate_future_value)
calculate_fv_button.grid(row=4, column=0, pady=10)

calculate_pv_button = ttk.Button(window, text="Calculate PV", command=calculate_present_value)
calculate_pv_button.grid(row=4, column=1, pady=10)

# --- Result ---
result_label = ttk.Label(window, text="")
result_label.grid(row=5, column=0, columnspan=2, pady=5)

# Run the main loop
window.mainloop()