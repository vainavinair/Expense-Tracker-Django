# SpendWise

The SpendWise is a web application built using Django, AJAX. It allows users to effortlessly track and manage their expenses, providing a convenient way to monitor their financial activities.

## Features

- User Authentication: Users can sign up, log in, and log out of the app. Email authentication is performed during signup by sending a verification email.
- Expense Tracking: Users can add, view, update, and delete their expenses or transactions.
- Categorization: Expenses or transactions can be categorized into different categories to organize and analyze the data effectively.
- Credit/Debit Classification: Users can classify their expenses or transactions as credit or debit to differentiate between income and expenses.
- Data Visualization: The app utilizes Chart.js to generate graphs and pie charts, providing a visual representation of the expense data.

## Technologies Used

- Django: The web framework used to build the app.
- AJAX: Asynchronous JavaScript and XML is employed for seamless CRUD operations without refreshing the entire page.
- Chart.js: A JavaScript library for data visualization, used to create graphs and pie charts.
- HTML/CSS: The app's frontend is built using HTML and CSS for structuring and styling the user interface.
- PostgreSQL: The relational database management system used to store the app's data.

## Installation

To run the SpendWise on your local machine, follow these steps:

1. Clone the repository: `git clone https://github.com/your-username/expense-tracker-app.git`
2. Navigate to the project directory: `cd expense-tracker-app`
3. Install the required dependencies: `pip install -r requirements.txt`
4. Set up the PostgreSQL database and update the database settings in the Django settings file.
5. Apply the database migrations: `python manage.py migrate`
6. Start the development server: `python manage.py runserver`
7. Access the app in your web browser at `http://localhost:8000`

Make sure you have Python and PostgreSQL installed on your system before proceeding with the installation.

## Usage

1. Sign up for an account using a valid email address.
2. Check your email for the verification email and click the verification link.
3. Log in to the app using your credentials.
4. Once logged in, you will be redirected to the expense tracking dashboard.
5. Use the navigation menu to add, view, update, or delete expenses or transactions.
6. You can categorize expenses and classify them as credit or debit.
7. The app provides graphs and pie charts to visualize your expense data.
8. Use the app to track your expenses and manage your financial data efficiently.

## Video Demo


https://github.com/vainavinair/Expense-Tracker-Django/assets/109602044/78f4359e-3d7c-4b24-9eab-1a188807468e

