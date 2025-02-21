name = str(input("Enter Name: "))
initial_balance = float(input("Enter Your Balance: "))

while initial_balance <= 0:
    print("Balance Should be > than 0")
    initial_balance = float(input("Enter Your Balance: "))

pin = input("Enter Your Pin: ")

while len(pin) != 4 or not pin.isdigit():
    print("Invalid Pin! Enter a 4-digit PIN (Numbers only).")
    pin = input("Enter the PIN: ")

while True:
    print("1. Deposit")
    print("2. Withdrawal")
    print("3. Exit")
    choice = int(input("Enter Your Choice (1/2/3): "))

    if choice == 1:
        deposit = float(input("Enter Your Deposit Amount: "))
        initial_balance += deposit
        print(f"Balance after deposit: ₹{initial_balance}")

    elif choice == 2:
        withdrawal = float(input("Enter Withdrawal Amount: "))

        while withdrawal > initial_balance:
            print("Withdrawal amount should be less than or equal to the available balance.")
            withdrawal = float(input("Enter Withdrawal Amount: "))

        initial_balance -= withdrawal
        print(f"Balance after withdrawal: ₹{initial_balance}")

    elif choice == 3:
        print("Thanks for Visiting!")
        break

    else:
        print("Invalid choice. Please enter 1, 2, or 3.")