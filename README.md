# ACEest Fitness and Gym — Tkinter GUI Application

## Project Overview

This is a Python Tkinter-based GUI application designed for ACEest Fitness and Gym. It allows users to log workouts with duration and view the collected history. This project demonstrates core DevOps practices in version control, testing, containerization, and automated CI/CD using GitHub Actions.

---

## Prerequisites

- Python 3.10 or higher (with Tkinter support)
- `pip` package manager
- Docker (for containerization)
- Git and GitHub account

---

## Setup Instructions

### 1. Clone the Repository

git clone <your-github-repository-url> cd <repository-folder>

### 2. Create and Activate Virtual Environment

python3 -m venv venv source venv/bin/activate

### 3. Install Python Dependencies

pip install -r requirements.txt

---

## Running the Application Locally

Run the Tkinter GUI app with:

python ACEest_Fitness.py

You can then:

- Add workouts with name and duration
- View logged workouts

---

## Running Unit Tests

Run tests with:

pytest

This runs the basic smoke test confirming the app initializes correctly.

---

## Docker Containerization

Build the Docker image:

docker build -t aceest_fitness_gui .

Run the Docker container (GUI might not display):

docker run --rm aceest_fitness_gui

---

## Continuous Integration / Continuous Delivery (CI/CD) Pipeline

We use GitHub Actions to automate:

- Code checkout
- Python setup
- Dependency installation
- Test execution
- Docker image build

Pipeline config is in `.github/workflows/main.yml`.

Check pipeline runs on GitHub **Actions** tab.

---

## Project Structure

├── ACEest_Fitness.py # Tkinter GUI app 
├── Dockerfile # Docker container config 
├── requirements.txt # Python dependencies 
├── test_ACEest_Fitness.py # Pytest unit tests 
├── README.md # This documentation file 
└── .github/ 
└── workflows/ 
└── main.yml # GitHub Actions workflow
---

## Contact

For issues or questions, contact Swapnil Mengi <2025ht66022@wilp.bits-pilani.ac.in>.
