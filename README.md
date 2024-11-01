Django Signals Example
This project demonstrates the behavior of Django signals with three specific scenarios: synchronous execution, thread behavior, and database transaction context. Follow these steps to set up and run the project.

Prerequisites
Python 3.x installed
Django installed (version 5.1.2)
A virtual environment (optional but recommended)
Setup Instructions
Clone the Repository (if applicable):

bash
Copy code
git clone <repository-url>
cd djangoProject
Set Up the Virtual Environment (optional but recommended):

bash
Copy code
python -m venv .venv
source .venv/bin/activate   # On Windows: .venv\Scripts\activate
Install Django:

bash
Copy code
pip install django==5.1.2
Apply Migrations: Initialize the SQLite database and create necessary tables:

bash
Copy code
python manage.py migrate
Run the Signal Tests: To test Django signal behaviors, use the custom management command test_signal_sync. This command will create a new user instance and trigger the post_save signal, demonstrating different scenarios.

bash
Copy code
python manage.py test_signal_sync
Expected Outputs
Synchronous Execution: You should see a 5-second delay in the output, indicating synchronous signal execution.

Thread Behavior: The output will confirm that the signal is received in the main thread.

Database Transaction Context: The output will show that the signal runs within the same transaction as the caller.

Troubleshooting
If you encounter OperationalError: no such table: auth_user, ensure you’ve run python manage.py migrate to set up the database tables.
Use exit() or Ctrl+D (Linux/Mac) / Ctrl+Z and Enter (Windows) to exit the Django shell.
Additional Notes
Feel free to extend this project or modify signals.py to explore additional signal behaviors.

Testing Each Question's Signals
Each question has a unique signals.py and test_signal_sync.py file located in question1, question2, and question3 folders. To test each question’s code:

Question 1
Replace Files: Copy the question1/signals.py file to myapp/signals.py and question1/test_signal_sync.py to the main directory.
Run Test: Execute the following command:
bash
python manage.py test_signal_sync
Question 2
Replace Files: Copy the question2/signals.py file to myapp/signals.py and question2/test_signal_sync.py to the main directory.
Run Test: Execute the following command:
bash
python manage.py test_signal_sync
Question 3
Replace Files: Copy the question3/signals.py file to myapp/signals.py and question3/test_signal_sync.py to the main directory.
Run Test: Execute the following command:
bash
python manage.py test_signal_sync
Note: Each test command will simulate the behavior of the Django signals for that question’s requirements.
