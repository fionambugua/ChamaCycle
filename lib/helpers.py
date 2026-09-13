def get_non_empty_input(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Input cannot be empty. Please try again.")


def get_positive_amount(prompt):
    while True:
        try:
            amount = float(input(prompt))
            if amount > 0:
                return amount
            print("Amount must be greater than 0.")
        except ValueError:
            print("Please enter a valid number.")


def get_month(prompt):
    while True:
        month = input(prompt).strip()

        try:
            year, month_number = month.split("-")

            if (
                len(year) == 4
                and len(month_number) == 2
                and 1 <= int(month_number) <= 12
            ):
                return month

            print("Please use the format YYYY-MM.")

        except ValueError:
            print("Please use the format YYYY-MM.")


def display_menu():
    print("\n===== ChamaCycle =====")
    print("Know your cycle. Trust your circle.")
    print("1. Add Member")
    print("2. Record Contribution")
    print("3. View Contribution History")
    print("4. View Pool Balance")
    print("5. View Who Hasn't Paid")
    print("6. View Next Payout Recipient")
    print("7. View My Chamas")
    print("8. Exit")


def pause():
    input("\nPress Enter to continue...")