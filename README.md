# Django Signals Project

This project demonstrates the use of Django signals for various purposes as part of an internship application. Each question has a unique implementation of Django signals located in separate folders (`question1`, `question2`, `question3`). 

## Project Structure

- **`myapp`**: The main Django app where signals are set up.
- **`question1`, `question2`, `question3`**: Each folder contains unique `signals.py` and `test_signal_sync.py` files specific to the requirements of each question.

## Prerequisites

- Python 3.8 or higher
- Django 5.1.2
- Git

## Setup Instructions

### Step 1: Clone the Repository

First, clone this repository to your local machine:
```bash
git clone <your-github-repo-url>
cd <your-repository-name>
```

### Step 2: Set Up a Virtual Environment

1. In the project directory, create a virtual environment:
   ```bash
   python -m venv .venv
   ```

2. Activate the virtual environment:
   - **On Windows**:
     ```bash
     .venv\Scripts\activate
     ```
   - **On macOS/Linux**:
     ```bash
     source .venv/bin/activate
     ```

### Step 3: Install Dependencies

Install Django and any required packages:
```bash
pip install -r requirements.txt
```

### Step 4: Database Setup

Run the following commands to set up the initial database:
```bash
python manage.py migrate
```

### Step 5: Run the Project

To start the Django server, run:
```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000` in your browser to confirm the project is running.

## Testing Each Question's Signals

Each question has a unique `signals.py` and `test_signal_sync.py` file located in `question1`, `question2`, and `question3` folders. To test each question’s code:

### Question 1

1. **Replace Files**: Copy the `question1/signals.py` file to `myapp/signals.py` and `question1/test_signal_sync.py` to the main directory.
2. **Run Test**: Execute the following command:
   ```bash
   python manage.py test_signal_sync
   ```

### Question 2

1. **Replace Files**: Copy the `question2/signals.py` file to `myapp/signals.py` and `question2/test_signal_sync.py` to the main directory.
2. **Run Test**: Execute the following command:
   ```bash
   python manage.py test_signal_sync
   ```

### Question 3

1. **Replace Files**: Copy the `question3/signals.py` file to `myapp/signals.py` and `question3/test_signal_sync.py` to the main directory.
2. **Run Test**: Execute the following command:
   ```bash
   python manage.py test_signal_sync
   ```

**Note**: Each test command will simulate the behavior of the Django signals for that question’s requirements.

## Additional Notes

- **Database**: This project uses an SQLite database for simplicity.
- **Virtual Environment**: Remember to activate your virtual environment each time you work on the project.
