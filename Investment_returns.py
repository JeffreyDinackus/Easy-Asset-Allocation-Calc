import tkinter as tk

# this script doesn't work

def calculate():
    try:
        principal = float(principal_entry.get())
        rate = float(interest_entry.get())
        time = float(time_entry.get())
        contributions = float(contributions_entry.get())

        # result = principal* (1+rate/12)**(12 *time)
        # result = principal * (1 + rate/(100*12))**(12*time)+((contributions*((1+rate/(100*12))**12*time)-1)/rate/(100*12))
        result_label.config(text=f"Final Amount: {round(result, 2)}")
    except ValueError:
        result_label.config(text="Please enter valid numbers")

# Create the main window
root = tk.Tk()
root.title("Investment Calculator")

root.geometry("400x300")  # Width x Height

# Create input fields and labels
principal_label = tk.Label(root, text="Principal Amount:")
principal_label.pack()
principal_entry = tk.Entry(root)
principal_entry.pack()

interest_label = tk.Label(root, text="Interest Rate (%):")
interest_label.pack()
interest_entry = tk.Entry(root)
interest_entry.pack()

time_label = tk.Label(root, text="Time Period (years):")
time_label.pack()
time_entry = tk.Entry(root)
time_entry.pack()

contributions_label = tk.Label(root, text="Contribution amount:")
contributions_label.pack()
contributions_entry = tk.Entry(root)
contributions_entry.pack()


calculate_button = tk.Button(root, text="Calculate", command=calculate)
calculate_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

# Run the main loop
root.mainloop()