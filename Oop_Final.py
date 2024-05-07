import random

class User:
    def __init__(self, name, email, address, account_type):
        self.name = name
        self.email = email
        self.address = address
        self.account_type = account_type
        self.balance = 0
        self.account_number = random.randint(1000, 99999)
        self.transaction_history = []
        self.loan_taken = 0
        self.loan_limit = 2

    def deposit(self, amount):
        self.balance += amount
        self.transaction_history.append(f"Deposited: {amount}$")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Withdrawal amount exceeded.")
        else:
            self.balance -= amount
            self.transaction_history.append(f"Withdrew: {amount}$")

    def check_balance(self):
        return self.balance

    def check_transaction_history(self):
        return self.transaction_history

    def take_loan(self, amount):
        if self.loan_limit > 0:
            self.balance += amount
            self.loan_taken += amount
            self.loan_limit -= 1
            self.transaction_history.append(f"Loan Taken: {amount}$")
        else:
            print("You have already taken the maximum number of loans.")

    def transfer_amount(self, amount, recipient):
        if self.balance >= amount:
            self.balance -= amount
            recipient.balance += amount
            self.transaction_history.append(f"Transferred: {amount}$ to {recipient.name}")
        else:
            print("Insufficient balance to transfer.")

class Admin:
    def __init__(self):
        self.users = []
        self.loan_feature_enabled = True

    def create_account(self, name, email, address, account_type):
        user = User(name, email, address, account_type)
        self.users.append(user)
        print("Account created successfully.")
        return user

    def delete_account(self, account_number):
        for user in self.users:
            if user.account_number == account_number:
                self.users.remove(user)
                print("Account deleted successfully.")
                return
        print("Account not found.")

    def see_all_accounts(self):
        for user in self.users:
            print(f"Name: {user.name}, Account Number: {user.account_number}")

    def check_total_balance(self):
        total_balance = sum(user.balance for user in self.users)
        return total_balance

    def check_total_loan_amount(self):
        total_loan_amount = sum(user.loan_taken for user in self.users)
        return total_loan_amount

    def toggle_loan_feature(self, status):
        self.loan_feature_enabled = status
        if status:
            print("Loan feature enabled.")
        else:
            print("Loan feature disabled.")

admin = Admin()

while True:
    print("\n1. User Operations\n2. Admin Operations\n3. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        name = input("Enter your name: ")
        email = input("Enter your email: ")
        address = input("Enter your address: ")
        account_type = input("Enter account type (Savings or Current): ").capitalize()
        user = admin.create_account(name, email, address, account_type)

        while True:
            print("\n1. Deposit\n2. Withdraw\n3. Check Balance\n4. Transaction History")
            if admin.loan_feature_enabled:
                print("5. Take Loan")
            print("6. Transfer Amount\n7. Back to Main Menu")
            user_choice = input("Enter your choice: ")

            if user_choice == '1':
                amount = float(input("Enter amount to deposit: "))
                user.deposit(amount)
                print("Deposit success...")
                
            elif user_choice == '2':
                amount = float(input("Enter amount to withdraw: "))
                user.withdraw(amount)
                print("Withdraw success...")
                
            elif user_choice == '3':
                print("Current Balance:", user.check_balance())
                
            elif user_choice == '4':
                print("Transaction History:", user.check_transaction_history())
                
            elif user_choice == '5' and admin.loan_feature_enabled:
                amount = float(input("Enter loan amount: "))
                user.take_loan(amount)
                print("Loan success...")
                
            elif user_choice == '6':
                recipient_name = input("Enter recipient's name: ")
                recipient = None
                for u in admin.users:
                    if u.name == recipient_name:
                        recipient = u
                        break
                if recipient:
                    amount = float(input("Enter amount to transfer: "))
                    user.transfer_amount(amount, recipient)
                    print("Transfer success...")
                else:
                    print("Recipient not found.")
                    
            elif user_choice == '7':
                break
            else:
                print("Invalid choice. Please try again.")

    elif choice == '2':
        while True:
            print("\n1. Create Account\n2. Delete Account\n3. See All Accounts")
            print("4. Check Total Balance\n5. Check Total Loan Amount")
            print("6. Toggle Loan Feature\n7. Back to Main Menu")
            admin_choice = input("Enter your choice: ")

            if admin_choice == '1':
                name = input("Enter user's name: ")
                email = input("Enter user's email: ")
                address = input("Enter user's address: ")
                account_type = input("Enter account type (Savings or Current): ").capitalize()
                admin.create_account(name, email, address, account_type)
                
            elif admin_choice == '2':
                account_number = int(input("Enter account number to delete: "))
                admin.delete_account(account_number)
                print("Account Delete success...")
                
            elif admin_choice == '3':
                admin.see_all_accounts()
                
            elif admin_choice == '4':
                print("Total Balance:", admin.check_total_balance())
                
            elif admin_choice == '5':
                print("Total Loan Amount:", admin.check_total_loan_amount())
                
            elif admin_choice == '6':
                status = input("Enter status (on or off): ").lower() == 'on'
                admin.toggle_loan_feature(status)
                
            elif admin_choice == '7':
                break
            else:
                print("Invalid choice. Please try again.")

    elif choice == '3':
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")
