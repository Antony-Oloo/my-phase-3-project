# my-phase-3-project

Welcome to the Coupon Management System CLI! 
This application allows users to manage coupons, discounts, and associated products/services via a simple Command Line Interface (CLI). 
The project demonstrates the use of Python's SQLAlchemy ORM and a well-structured database to manage coupon-related operations efficiently.
The CLI application allows users to manage discounts and coupons. Stores details like coupon codes, discounts, expiry dates, and redemption status in a database.
some of the MVPs of the application include:- 

1.	Adding new records (new coupons or users).
2.	Retrieving information (list of active coupons or redeemed coupons).
3.	Updating records (extend expiry date or mark a coupon as redeemed).
4.	Deleting records (remove expired coupons).


## some of the Features that the application has includes:-

- **User Management**: Create, update, and delete users.
- **Coupon Management**: Create, update, and delete coupons.
- **Transaction Management**: Record and view transactions between users and coupons.
- **Database Initialization**: Initialize the database schema and populate initial data.
- **Validation**: Email and input validation ensure data integrity.
  

### Project Structure
```
My-phase-3-project_CLI/
├── migrations/
    ├──versions/
    ├──env.py
├── alembic.ini
├── cli.py
├── models.py
├── database.py
└── README.md

## Technologies Used
- Python 3.x
- SQLAlchemy (for ORM and database management)
- Alembic (for database migrations)
- SQLite (as the default database engine)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/my-phase-3-project_CLI.git
   cd my-phase-3-project_CLI

   Available commands:

1. Initialize Database: Initializes the database schema and tables.
2. Create User: Creates a new user by entering a name and email.
3. Update User: Updates an existing user's details (name and email).
4. Delete User: Deletes a user by their ID.
5. Create Coupon: Creates a new coupon with a discount percentage.
6. Update Coupon: Updates an existing coupon's details (code and discount percentage).
7. Delete Coupon: Deletes a coupon by its ID.
8. Create Transaction: Creates a new transaction for a user using a coupon.
9. View Transactions for User: Displays all transactions for a specific user.
10. Delete Transaction: Deletes a transaction by its ID.
11. Exit: Exits the program.

