from lib.models.chama import Chama
from lib.models.member import Member


def show_menu():
    print("\n=== ChamaCycle ===")
    print("1. View members who haven't paid")
    print("2. View next payout recipient")
    print("3. View payout order")
    print("4. Exit")


def run():
    chama = Chama("Harambee Chama")

    while True:
        show_menu()

        choice = input("Choose an option: ")

        if choice == "1":
            month = input("Enter month: ")

            unpaid = chama.members_not_paid(month)

            if unpaid:
                print("\nMembers who haven't paid:")
                for member in unpaid:
                    print(f"- {member.name}")
            else:
                print("\nEveryone has paid.")

        elif choice == "2":
            member = chama.next_payout_recipient()

            if member:
                position = chama.payout_position(member)

                print("\nNext payout recipient:")
                print(f"Name: {member.name}")
                print(f"Position: {position}")
            else:
                print("\nThere is no pending payout.")

        elif choice == "3":
            print("\nPayout Order:")

            for position, member in enumerate(
                chama.payout_order,
                start=1
            ):
                print(f"{position}. {member.name}")

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    run()
