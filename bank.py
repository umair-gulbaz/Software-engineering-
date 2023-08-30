import tkinter as tk

class BankAccount:
    def __init__(self):
        self.accountNumber = ""
        self.balance = 0.0

    def deposit(self, amount):
        self.balance += amount
        return True

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return True
        return False

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.bank_account = None

    def signUp(self):
        if self.bank_account is None:
            self.bank_account = BankAccount()
            self.bank_account.accountNumber = f"ACC-{len(self.username)}"
            return True
        return False

class BankingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Banking App")

        self.bank_account = BankAccount()
        self.user = None

        self.label_balance = tk.Label(root, text="Balance: $0.00")
        self.label_balance.pack()

        self.button_deposit = tk.Button(root, text="Deposit", command=self.open_deposit_window)
        self.button_deposit.pack()

        self.button_withdraw = tk.Button(root, text="Withdraw", command=self.open_withdraw_window)
        self.button_withdraw.pack()

        self.button_signup = tk.Button(root, text="Sign Up", command=self.open_signup_window)
        self.button_signup.pack()

        self.button_profile = tk.Button(root, text="Profile", command=self.open_profile_window)
        self.button_profile.pack()

        self.label_status = tk.Label(root, text="", fg="red")
        self.label_status.pack()

    def open_signup_window(self):
        signup_window = tk.Toplevel(self.root)
        signup_window.title("Sign Up")

        label_username = tk.Label(signup_window, text="Username:")
        label_username.pack()

        self.entry_username = tk.Entry(signup_window)
        self.entry_username.pack()

        label_password = tk.Label(signup_window, text="Password:")
        label_password.pack()

        self.entry_password = tk.Entry(signup_window, show="*")
        self.entry_password.pack()

        button_signup = tk.Button(signup_window, text="Sign Up", command=self.process_signup)
        button_signup.pack()

    def process_signup(self):
        username = self.entry_username.get()
        password = self.entry_password.get()
        if username and password:
            self.user = User(username, password)
            success = self.user.signUp()
            if success:
                self.label_status.config(text="Sign-up successful", fg="green")
            else:
                self.label_status.config(text="User already signed up", fg="red")
        else:
            self.label_status.config(text="Invalid input", fg="red")

    def open_deposit_window(self):
        deposit_window = tk.Toplevel(self.root)
        deposit_window.title("Deposit Cash")

        label_amount = tk.Label(deposit_window, text="Enter deposit amount:")
        label_amount.pack()

        self.entry_amount = tk.Entry(deposit_window)
        self.entry_amount.pack()

        button_deposit = tk.Button(deposit_window, text="Deposit", command=self.process_deposit)
        button_deposit.pack()

    def process_deposit(self):
        try:
            amount = float(self.entry_amount.get())
            if amount > 0:
                success = self.bank_account.deposit(amount)
                if success:
                    self.label_status.config(text="Deposit successful", fg="green")
                    self.update_balance()
                else:
                    self.label_status.config(text="Deposit failed", fg="red")
            else:
                self.label_status.config(text="Invalid amount", fg="red")
        except ValueError:
            self.label_status.config(text="Invalid input", fg="red")

    def open_withdraw_window(self):
        withdraw_window = tk.Toplevel(self.root)
        withdraw_window.title("Withdraw Cash")

        label_amount = tk.Label(withdraw_window, text="Enter withdrawal amount:")
        label_amount.pack()

        self.entry_amount = tk.Entry(withdraw_window)
        self.entry_amount.pack()

        button_withdraw = tk.Button(withdraw_window, text="Withdraw", command=self.process_withdraw)
        button_withdraw.pack()

    def process_withdraw(self):
        try:
            amount = float(self.entry_amount.get())
            if amount > 0:
                success = self.bank_account.withdraw(amount)
                if success:
                    self.label_status.config(text="Withdrawal successful", fg="green")
                    self.update_balance()
                else:
                    self.label_status.config(text="Insufficient balance", fg="red")
            else:
                self.label_status.config(text="Invalid amount", fg="red")
        except ValueError:
            self.label_status.config(text="Invalid input", fg="red")

    def open_profile_window(self):
        profile_window = tk.Toplevel(self.root)
        profile_window.title("Profile")

        if self.user:
            label_username = tk.Label(profile_window, text=f"Username: {self.user.username}")
            label_username.pack()

            if self.user.bank_account:
                label_account_number = tk.Label(profile_window, text=f"Account Number: {self.user.bank_account.accountNumber}")
                label_account_number.pack()
        else:
            label_message = tk.Label(profile_window, text="No user signed up.")
            label_message.pack()

    def update_balance(self):
        self.label_balance.config(text=f"Balance: ${self.bank_account.balance:.2f}")

if __name__ == "__main__":
    root = tk.Tk()
    app = BankingApp(root)
    root.geometry("300x200")  # Set initial window size
    root.mainloop()
