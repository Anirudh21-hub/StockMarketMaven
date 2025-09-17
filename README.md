# Python Flask CI/CD

This is a basic Python Flask application with a CI/CD pipeline set up using GitHub Actions.

## CI/CD Pipeline
The `.github/workflows/main.yaml` file defines the GitHub Actions workflow, which includes:
- Linting with `flake8`
- Running tests with `unittest`
- Performing static code analysis with `Bandit`

## How to Run

1.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
    (Note: `Bandit` requires Python 3.7+; if you're using an older Python version, you may need to upgrade or remove `bandit` from `requirements.txt`.)

2.  **Run the Flask application:**
    ```bash
    c:\users\dell\appdata\local\programs\python\python36-32\python.exe app.py
    ```
    Access the application at `http://127.0.0.1:5000/` in your browser.

3.  **Run the tests:**
    ```bash
    c:\users\dell\appdata\local\programs\python\python36-32\python.exe -m unittest test_app.py
    ```

## Build Status
[![Build Status](https://github.com/<YOUR_USERNAME>/<YOUR_REPOSITORY>/workflows/Python%20Flask%20CI/CD/badge.svg)](https://github.com/<YOUR_USERNAME>/<YOUR_REPOSITORY>/actions)

## Security Scan
[![Bandit Security Scan](https://github.com/<YOUR_USERNAME>/<YOUR_REPOSITORY>/workflows/Python%20Flask%20CI/CD/badge.svg?event=push)](https://github.com/<YOUR_USERNAME>/<YOUR_REPOSITORY>/actions)
[![Secret Scan](https://github.com/<YOUR_USERNAME>/<YOUR_REPOSITORY>/workflows/Secret%20Scan/badge.svg)](https://github.com/<YOUR_USERNAME>/<YOUR_REPOSITORY>/actions?query=workflow%3A%22Secret+Scan%22)
