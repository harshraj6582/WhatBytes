https://www.loom.com/share/6b8a373b7e354190a52a11ca1a00b579?sid=32d1268b-9b5c-49df-b6d5-1a0f67420cb2
![image](https://github.com/user-attachments/assets/04a736e6-09f3-4075-8787-60cd3c6e70c0)
![image](https://github.com/user-attachments/assets/f1d83686-1aec-4654-8e30-07ac53a3f239)
![image](https://github.com/user-attachments/assets/f166e415-29a1-4ac8-aae3-9f0e23d3c8e1)




# Django User Authentication System

This is a simple Django user authentication system that provides functionalities for user login, sign up, password reset, and profile management.

## Features

1. **Login Page**
   - Two fields: Username/Email and Password.
   - Links for Sign Up and Forgot Password.

2. **Sign Up Page**
   - Fields for Username, Email, Password, and Confirm Password.
   - Link to go back to the Login page.

3. **Forgot Password Page**
   - Field for Email to send password reset instructions.
   - On submission, an email with a reset link is sent to the user.

4. **Change Password Page**
   - Requires user authentication.
   - Fields for Old Password, New Password, and Confirm Password.
   - Option to return to the Dashboard.

5. **Dashboard**
   - Accessible only to authenticated users.
   - Displays a greeting message like "Hi, username!".
   - Links to the Profile page and Change Password page.
   - Option to logout.

6. **Profile Page**
   - Displays user information such as Username, Email, Date Joined, and Last Updated.
   - Option to return to the Dashboard or logout.

## Requirements

To run this project, you'll need to have Python and Django installed. Follow these steps to set up the project.

1. Create a virtual environment:

   ```bash
   python -m venv .venv
   ```

2. Activate the virtual environment:

   - For Windows:
     ```bash
     .venv\Scripts\activate
     ```

   - For macOS/Linux:
     ```bash
     source .venv/bin/activate
     ```



3. Run migrations to set up the database:

   ```bash
   python manage.py migrate
   ```

4. Start the Django development server:

   ```bash
   python manage.py runserver
   ```

5. Open your browser and go to `http://127.0.0.1:8000/` to access the application.

## How It Works

- **Login Page**: Users can log in with their username/email and password. Links to Sign Up and Forgot Password are available.
- **Sign Up Page**: New users can create an account by providing their username, email, and password.
- **Forgot Password Page**: If a user forgets their password, they can request a password reset via email.
- **Change Password Page**: Authenticated users can change their password by providing the old and new password.
- **Dashboard**: Once logged in, users can view a personalized greeting, access their profile, change their password, or log out.
- **Profile Page**: Users can view their account details and return to the dashboard or log out.

---


