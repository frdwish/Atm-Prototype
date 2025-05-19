def user_account():
    total = 0
    while True:
        print("\n<-----Welcome to ATM Banking💳----->")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            deposit = int(input("Enter amount to deposit: ₹"))
            total += deposit
            print(f"₹{deposit} deposited. Total balance: ₹{total}")

        elif choice == '2':
            withdraw = int(input("Enter amount to withdraw: ₹"))
            if withdraw <= total:
                total -= withdraw
                print(f"₹{withdraw} withdrawn. Remaining balance: ₹{total}")
            else:
                print("Insufficient balance!")

        elif choice == '3':
            print(f"Current Balance: ₹{total}")

        elif choice == '4':
            print("Thank you for banking with us!")
            break
        else:
            print("Invalid option. Try again.")
