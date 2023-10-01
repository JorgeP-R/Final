"""
Author:  Jorge Ramirez
Date written: 09/24/23
Assignment:   Final Project
Short Desc:   Loan Calculator 
"""
import tkinter as tk
from tkinter import messagebox

class LoanCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Loan Calculator")

        self.initial_amount_label = tk.Label(root, text="Initial Loan Amount:")
        self.initial_amount_label.pack()
        self.initial_amount_entry = tk.Entry(root)
        self.initial_amount_entry.pack()

        self.years_label = tk.Label(root, text="Number of Years:")
        self.years_label.pack()
        self.years_entry = tk.Entry(root)
        self.years_entry.pack()

        self.interest_rate_label = tk.Label(root, text="Annual Interest Rate (%):")
        self.interest_rate_label.pack()
        self.interest_rate_entry = tk.Entry(root)
        self.interest_rate_entry.pack()

        self.calculate_button = tk.Button(root, text="Calculate", command=self.calculate_loan)
        self.calculate_button.pack()

        self.clear_button = tk.Button(root, text="Clear", command=self.clear_entries)
        self.clear_button.pack()

        self.exit_button = tk.Button(root, text="Exit", command=root.quit)
        self.exit_button.pack()

        self.result_label = tk.Label(root, height=10, width=40)
        self.result_label.pack()

    def calculate_loan(self):
        try:
            initial_amount = float(self.initial_amount_entry.get())
            years = int(self.years_entry.get())
            annual_interest_rate = float(self.interest_rate_entry.get()) / 100

            total_interest = 0
            result_text = "Year\tLoan Amount\tInterest Paid\n"
            for year in range(1, years + 1):
                interest_paid = initial_amount * annual_interest_rate
                total_interest += interest_paid
                initial_amount += interest_paid
                result_text += f"{year}\t${initial_amount:.2f}\t${interest_paid:.2f}\n"

            self.result_label.config(text=result_text + f"Total Interest Paid on your Loan: ${total_interest:.2f}")
        except ValueError:
            messagebox.showerror("Error", "Invalid input. Please enter numeric values.")

    def clear_entries(self):
        self.initial_amount_entry.delete(0, tk.END)
        self.years_entry.delete(0, tk.END)
        self.interest_rate_entry.delete(0, tk.END)
        self.result_label.config(text="")

if __name__ == "__main__":
    root = tk.Tk()
    calculator = LoanCalculator(root)
    root.mainloop()