import random

class BankAccount:
    def __init__(self, name, email, address, account_type):
        self.name = name
        self.email = email
        self.address = address
        self.account_type = account_type
        self.balance = 0
        self.account_number = random.randint(100000, 999999)
        self.transaction_history = []
        self.loan_taken = 0

    def deposit(self, amount):
        self.balance += amount
        self.transaction_history.append(f"Deposit: +${amount}")
        print(f"Deposited ${amount} successfully. Current balance: ${self.balance}")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            self.transaction_history.append(f"Withdrawal: -${amount}")
            print(f"Withdrew ${amount} successfully. Current balance: ${self.balance}")
        else:
            print("Withdrawal amount exceeded")

    def check_balance(self):
        print(f"Available balance: ${self.balance}")

    def check_transaction_history(self):
        print("Transaction History:")
        for transaction in self.transaction_history:
            print(transaction)

    def take_loan(self, amount):
        if self.loan_taken < 2:
            self.balance += amount
            self.loan_taken += 1
            self.transaction_history.append(f"Loan: +${amount}")
            print(f"Loan of ${amount} taken successfully. Current balance: ${self.balance}")
        else:
            print("You have already taken the maximum number of loans.")

    def transfer(self, amount, recipient):
        if recipient is None:
            print("Error: Account does not exist.")
        elif self.balance >= amount:
            self.balance -= amount
            recipient.balance += amount
            self.transaction_history.append(f"Transfer: -${amount} to {recipient.name}")
            recipient.transaction_history.append(f"Transfer: +${amount} from {self.name}")
            print(f"Transferred ${amount} to {recipient.name} successfully.")
        else:
            print("Insufficient funds to make the transfer.")

class Admin:
    def __init__(self):
        self.users = []

    def create_account(self, name, email, address, account_type):
        new_user = BankAccount(name, email, address, account_type)
        self.users.append(new_user)
        print("Account created successfully.")

    def delete_account(self, account_number):
        for user in self.users:
            if user.account_number == account_number:
                self.users.remove(user)
                print("Account deleted successfully.")
                return
        print("Account not found.")

    def see_all_accounts(self):
        print("All User Accounts:")
        for user in self.users:
            print(f"Name: {user.name}, Email: {user.email}, Account Type: {user.account_type}")

    def total_available_balance(self):
        total_balance = sum(user.balance for user in self.users)
        print(f"Total Available Balance of the Bank: ${total_balance}")

    def total_loan_amount(self):
        total_loan = sum(user.balance for user in self.users if user.loan_taken > 0)
        print(f"Total Loan Amount: ${total_loan}")

    def toggle_loan_feature(self, status):
        BankAccount.take_loan = status
        print(f"Loan feature is {'enabled' if status else 'disabled'}.")

# Replica system
admin = Admin()

while True:
    user_choice = input("Choose 'user' or 'admin' (or 'exit' to quit): ").lower()

    if user_choice == "exit":
        print("Exiting program...")
        break

    elif user_choice == "user":
        num_users = int(input("Enter the number of users to create accounts for: "))
        for _ in range(num_users):
            name = input("Enter your name: ")
            email = input("Enter your email: ")
            address = input("Enter your address: ")
            account_type = input("Enter your account type (Savings/Current): ")

            user = BankAccount(name, email, address, account_type)
            admin.users.append(user)
            print("Account created successfully.")

            print(f"\nUser: {user.name}")
            while True:
                print("Choose an action:")
                print("1. Deposit")
                print("2. Withdraw")
                print("3. Check Balance")
                print("4. Take Loan")
                print("5. Transaction History")
                print("6. Switch to Admin")
                user_choice = input("Enter your choice: ").lower()

                if user_choice == '1':
                    amount = float(input("Enter the amount to deposit: "))
                    user.deposit(amount)
                elif user_choice == '2':
                    amount = float(input("Enter the amount to withdraw: "))
                    user.withdraw(amount)
                elif user_choice == '3':
                    user.check_balance()
                elif user_choice == '4':
                    amount = float(input("Enter the amount to take as a loan: "))
                    user.take_loan(amount)
                elif user_choice == '5':
                    user.check_transaction_history()
                elif user_choice == '6':
                    break
                else:
                    print("Invalid choice.")

    elif user_choice == "admin":
        # Perform admin tasks
        admin_actions = {
            'see_all_accounts': admin.see_all_accounts,
            'total_available_balance': admin.total_available_balance,
            'total_loan_amount': admin.total_loan_amount,
            'toggle_loan_feature': lambda: admin.toggle_loan_feature(True),
            'delete_account': lambda: admin.delete_account(int(input("Enter the account number to delete: "))),
        }
        while True:
            print("Choose an action:")
            print("1. See all user accounts")
            print("2. Check total available balance")
            print("3. Check total loan amount")
            print("4. Toggle loan feature")
            print("5. Delete user account")
            print("6. Switch to User")
            admin_choice = input("Enter your choice: ").lower()

            if admin_choice == '6':
                break

            if admin_choice in admin_actions:
                admin_actions[admin_choice]()
            else:
                print("Invalid choice.")

    else:
        print("Invalid choice. Please choose 'user' or 'admin'.")
