Django User Authentication System
This is a simple Django user authentication system that provides functionalities for user login, sign up, password reset, and profile management.

Features
Login Page

Two fields: Username/Email and Password.
Links for Sign Up and Forgot Password.
Sign Up Page

Fields for Username, Email, Password, and Confirm Password.
Link to go back to the Login page.
Forgot Password Page

Field for Email to send password reset instructions.
On submission, an email with a reset link is sent to the user.
Change Password Page

Requires user authentication.
Fields for Old Password, New Password, and Confirm Password.
Option to return to the Dashboard.
Dashboard

Accessible only to authenticated users.
Displays a greeting message like "Hi, username!".
Links to the Profile page and Change Password page.
Option to logout.
Profile Page

Displays user information such as Username, Email, Date Joined, and Last Updated.
Option to return to the Dashboard or logout.
Requirements
To run this project, you'll need to have Python and Django installed. Follow these steps to set up the project.

Create a virtual environment:

bash
Copy code
python -m venv .venv
Activate the virtual environment:

For Windows:

bash
Copy code
.venv\Scripts\activate


Run migrations to set up the database:

bash
Copy code
python manage.py migrate
Start the Django development server:

bash
Copy code
python manage.py runserver
Open your browser and go to http://127.0.0.1:8000/ to access the application.
