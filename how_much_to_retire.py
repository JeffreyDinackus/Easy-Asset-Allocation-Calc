import tkinter as tk

# I think this script works but check your numbers

def calculate():
    try:
        net_worth = float(net_worth_entry.get())
        retirement_expenses = float(retirement_expenses_entry.get())
        time = float(time_entry.get())
        retirement_income = float(retirement_income_entry.get())
        
        result = net_worth
        i = 0
        while i < time:
            

          result = result - retirement_expenses + retirement_income
          i+=1
        result_label.config(text=f"Final Amount: {round(result, 2)}")


        pass
    except ValueError:
        result_label.config(text="Please enter valid numbers")

# Create the main window
root = tk.Tk()
root.title("Retirement Calculator")

root.geometry("400x300")  # Width x Height

# Create input fields and labels
net_worth_label = tk.Label(root, text="Net worth:")
net_worth_label.pack()
net_worth_entry = tk.Entry(root)
net_worth_entry.pack()

retirement_expenses_label = tk.Label(root, text="Yearly Expenses in Retirement:")
retirement_expenses_label.pack()
retirement_expenses_entry = tk.Entry(root)
retirement_expenses_entry.pack()

time_label = tk.Label(root, text="How long I could live:")
time_label.pack()
time_entry = tk.Entry(root)
time_entry.pack()

retirement_income_label = tk.Label(root, text="Retirement income yearly amount:")
retirement_income_label.pack()
retirement_income_entry = tk.Entry(root)
retirement_income_entry.pack()


calculate_button = tk.Button(root, text="Calculate", command=calculate)
calculate_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

# formula = tk.Label(root, text='''Formula: 
#         while i < time:
#             net_worth = (retirement_income * 12 + net_worth) * (1 + rate / 100)
#             i+=1
#             print(net_worth)")''')
# formula.pack()

# Run the main loop
root.mainloop()
