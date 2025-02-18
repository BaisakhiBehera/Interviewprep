# Interview Prep Web App

This is a simple web app that helps users with interview preparation by displaying relevant links based on the selected technology and experience level.

## Tech Stack 
- **Backend**: Django (Python)
- **Frontend**: JavaScript, HTML, CSS
- **Database**: MySQL

## Quick Start Guide

### Prerequisites
- Python 3.8+
- MySQL

### Steps to Run Locally

1. **Clone the repository**:

    ```bash
    git clone https://github.com/yourusername/interviewprep.git
    cd interviewprep
    ```

2. **Set up a virtual environment**:

    For **Windows**:
    ```bash
    python -m venv venv
    venv\Scripts\activate
    ```

    For **Mac/Linux**:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Install dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

4. **Create a MySQL database**:

    ```bash
    mysql -u root -p
    CREATE DATABASE interviewprep;
    ```

5. **Set up environment variables**:

    Create a `.env` file with the following content:

    ```env
    DB_NAME=interviewprep
    DB_USER=your_mysql_user
    DB_PASSWORD=your_mysql_password
    DB_HOST=localhost
    DB_PORT=3306
    ```

6. **Apply migrations**:

    ```bash
    python manage.py migrate
    ```

7. **Run the app**:

    ```bash
    python manage.py runserver
    ```

Visit `http://127.0.0.1:8000/` in your browser to use the app.

## Contributing

Feel free to fork the repo and submit pull requests for any improvements.
