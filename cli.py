import sys
import re
from database import session, init_db
from models import User, Coupon, Transaction

def validate_email(email: str) -> bool:
    """Validate the email format using regex."""
    regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(regex, email) is not None

def get_valid_integer(prompt: str) -> int:
    """Helper function to safely get a valid integer from user input."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def get_valid_percentage(prompt: str) -> int:
    """Helper function to get a valid discount percentage (0-100)."""
    while True:
        try:
            percentage = int(input(prompt))
            if 0 <= percentage <= 100:
                return percentage
            else:
                print("Invalid input. Please enter a percentage between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a valid percentage.")

def get_valid_id(prompt: str, model):
    """Helper function to get a valid ID and ensure the object exists."""
    while True:
        user_id = get_valid_integer(prompt)
        obj = session.get(model, user_id)
        if obj:
            return obj
        else:
            print(f"{model.__name__} with ID {user_id} not found. Please try again.")

# --- User Functions ---
def create_user():
    name = input("Enter user name: ")
    email = input("Enter user email: ")

    if not validate_email(email):
        print(f"Invalid email format: {email}")
        return

    user = User(name=name, email=email)
    session.add(user)
    session.commit()

    print(f"User '{name}' created with ID {user.id}.")

def update_user():
    user = get_valid_id("Enter user ID to update: ", User)
    user.name = input(f"Enter new name (current: {user.name}): ") or user.name
    user.email = input(f"Enter new email (current: {user.email}): ") or user.email
    session.commit()
    print(f"User with ID {user.id} updated.")

def delete_user():
    user = get_valid_id("Enter user ID to delete: ", User)
    session.delete(user)
    session.commit()
    print(f"User with ID {user.id} deleted.")

# --- Coupon Functions ---
def create_coupon():
    code = input("Enter coupon code: ")
    discount_percentage = get_valid_percentage("Enter discount percentage: ")

    coupon = Coupon(code=code, discount_percentage=discount_percentage)
    session.add(coupon)
    session.commit()

    print(f"Coupon '{code}' created with ID {coupon.id}.")

def update_coupon():
    coupon = get_valid_id("Enter coupon ID to update: ", Coupon)
    coupon.code = input(f"Enter new code (current: {coupon.code}): ") or coupon.code
    coupon.discount_percentage = get_valid_percentage(f"Enter new discount percentage (current: {coupon.discount_percentage}): ") or coupon.discount_percentage
    session.commit()
    print(f"Coupon with ID {coupon.id} updated.")

def delete_coupon():
    coupon = get_valid_id("Enter coupon ID to delete: ", Coupon)
    session.delete(coupon)
    session.commit()
    print(f"Coupon with ID {coupon.id} deleted.")

# --- Transaction Functions ---
def create_transaction():
    user = get_valid_id("Enter user ID for transaction: ", User)
    coupon = get_valid_id("Enter coupon ID for transaction: ", Coupon)
    
    status = input("Enter status for transaction (e.g., 'completed', 'pending', 'failed'): ")
    transaction = Transaction(user_id=user.id, coupon_id=coupon.id, status=status)

    session.add(transaction)
    session.commit()

    print(f"Transaction created with ID {transaction.id}.")

def view_transactions():
    user = get_valid_id("Enter user ID to view transactions: ", User)
    
    transactions = user.transactions
    if not transactions:
        print(f"No transactions found for User ID {user.id}.")
        return
    
    print(f"Transactions for User '{user.name}':")
    for transaction in transactions:
        print(f"Transaction ID: {transaction.id}, Status: {transaction.status}, Date: {transaction.transaction_date}")

def delete_transaction():
    transaction = get_valid_id("Enter transaction ID to delete: ", Transaction)
    session.delete(transaction)
    session.commit()
    print(f"Transaction with ID {transaction.id} deleted.")

# --- Main Menu ---
def main_menu():
    actions = {
        '1': init_db,
        '2': create_user,
        '3': update_user,
        '4': delete_user,
        '5': create_coupon,
        '6': update_coupon,
        '7': delete_coupon,
        '8': create_transaction,
        '9': view_transactions,
        '10': delete_transaction,
        '11': exit_program
    }

    while True:
        print("\nWelcome to the Coupon Management System")
        print("1. Initialize Database")
        print("2. Create User")
        print("3. Update User")
        print("4. Delete User")
        print("5. Create Coupon")
        print("6. Update Coupon")
        print("7. Delete Coupon")
        print("8. Create Transaction")
        print("9. View Transactions for User")
        print("10. Delete Transaction")
        print("11. Exit")
        
        choice = input("Choose an option: ")

        # Use the dictionary to handle actions
        action = actions.get(choice)
        if action:
            action()  
        else:
            print("Invalid option, please try again.")

def exit_program():
    print("Exiting...")
    sys.exit()


if __name__ == "__main__":
    init_db()
    main_menu()