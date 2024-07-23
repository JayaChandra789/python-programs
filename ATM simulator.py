class ATM: 
    def __init__(self, balance=0): #Initializes an instance of the ATM class with an optional starting balance 
        self.balance = balance
    def check_balance(self):
        print(f"Your balance is ${self.balance}")
    def deposit(self, amount):
        self.balance += amount
        print(f"${amount} deposited successfully.")
        self.check_balance()
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"${amount} withdrawn successfully.")
        else:
            print("Insufficient balance.")
        self.check_balance()
def main():
    atm = ATM(balance=1000)  # Starting balance of $1000

    while True:
        print("\nATM Menu:")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            atm.check_balance()
        elif choice == '2':
            amount = float(input("Enter deposit amount: $"))
            atm.deposit(amount)
        elif choice == '3':
            amount = float(input("Enter withdrawal amount: $"))
            atm.withdraw(amount)
        elif choice == '4':
            print("Thank you for using our ATM. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()
