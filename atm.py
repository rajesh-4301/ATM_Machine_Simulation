import tkinter as tk
from tkinter import simpledialog, messagebox

class ATM:
    def __init__(self, root):
        self.balance = 0
        self.transactions = []
        self.root = root
        self.root.title("ATM Interface")

        self.create_widgets()

    def create_widgets(self):
        # Frame for the welcome message
        self.welcome_frame = tk.Frame(self.root)
        self.welcome_frame.pack(pady=10)
        self.welcome_label = tk.Label(self.welcome_frame, text="Please select a service", font=("Arial", 16))
        self.welcome_label.pack()

        # Frame for buttons
        self.button_frame = tk.Frame(self.root)
        self.button_frame.pack(pady=20)

        # Buttons for services
        self.balance_button = tk.Button(self.button_frame, text="Check Balance", font=("Arial", 12), command=self.check_balance)
        self.balance_button.grid(row=0, column=0, padx=10, pady=5)

        self.deposit_button = tk.Button(self.button_frame, text="Deposit Money", font=("Arial", 12), command=self.deposit)
        self.deposit_button.grid(row=0, column=1, padx=10, pady=5)

        self.withdraw_button = tk.Button(self.button_frame, text="Withdraw Money", font=("Arial", 12), command=self.withdraw)
        self.withdraw_button.grid(row=0, column=2, padx=10, pady=5)

        self.history_button = tk.Button(self.button_frame, text="Transaction History", font=("Arial", 12), command=self.show_history)
        self.history_button.grid(row=0, column=3, padx=10, pady=5)

        self.exit_button = tk.Button(self.button_frame, text="Exit", font=("Arial", 12), command=self.root.quit)
        self.exit_button.grid(row=0, column=4, padx=10, pady=5)

        # Frame for the balance display
        self.balance_frame = tk.Frame(self.root)
        self.balance_frame.pack(pady=10)
        self.balance_label = tk.Label(self.balance_frame, text=f"Balance: ${self.balance}", font=("Arial", 14))
        self.balance_label.pack()

    def update_balance_label(self):
        self.balance_label.config(text=f"Balance: ${self.balance}")

    def check_balance(self):
        messagebox.showinfo("Balance", f"Your current balance is: ${self.balance}")

    def deposit(self):
        amount = self.get_amount("Deposit Amount")
        if amount is not None:
            if amount > 0:
                self.balance += amount
                self.transactions.append(f"Deposited: ${amount}")
                messagebox.showinfo("Success", f"${amount} deposited successfully.")
                self.update_balance_label()
            else:
                messagebox.showwarning("Error", "Deposit amount must be greater than zero.")

    def withdraw(self):
        amount = self.get_amount("Withdrawal Amount")
        if amount is not None:
            if amount > self.balance:
                messagebox.showwarning("Error", "Insufficient funds.")
            elif amount <= 0:
                messagebox.showwarning("Error", "Withdrawal amount must be greater than zero.")
            else:
                self.balance -= amount
                self.transactions.append(f"Withdrew: ${amount}")
                messagebox.showinfo("Success", f"${amount} withdrawn successfully.")
                self.update_balance_label()

    def show_history(self):
        if self.transactions:
            history = "\n".join(self.transactions)
            messagebox.showinfo("Transaction History", history)
        else:
            messagebox.showinfo("Transaction History", "No transactions found.")

    def get_amount(self, prompt):
        amount_str = simpledialog.askstring("Amount", prompt)
        if amount_str is not None:
            try:
                return float(amount_str)
            except ValueError:
                messagebox.showwarning("Error", "Please enter a valid number.")
        return None

if __name__ == "__main__":
    root = tk.Tk()
    atm = ATM(root)
    root.mainloop()
