#  Mini ATM Project using Python & Tkinter

##  Project Overview

This is a beginner-friendly **Graphical User Interface (GUI)-based ATM simulation** created using Python and Tkinter. The application allows users to:
- Create an account (username & password)
- Login with hidden password input and toggle visibility
- Deposit money
- Withdraw money
- Check account balance

The project is an excellent practice exercise for building logic in Python, integrating GUI, and handling user interactions securely.

---

## Case Study

### Problem:
A user-friendly desktop ATM interface is required for managing simple banking operations like deposits, withdrawals, and checking balance. It should include login authentication with password visibility toggle for better UX.

### Solution:
This project uses Python and Tkinter to simulate ATM behavior:
- Users must first create and verify their credentials.
- Upon successful login, they are presented with a menu of operations.
- Password is hidden by default, but can be toggled to visible using an "eye" button.
- The session ends after the selected transaction is complete.


    ↓
mini-atm-project/
│
├── main.py            # GUI login and main transaction logic
├── user_data.py       # Stores user credentials
├── README.md          # Project documentation
└── requirements.txt   # (Optional, if dependencies are added later)

## How to Run

### 1. Clone the project or download ZIP

```bash
git clone https://github.com/your-repo/mini-atm-project.git

2. Navigate to the project directory
cd mini-atm-project

3. (Optional) Create a virtual environment
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows

4. Install required libraries
sudo apt install python3-tk

5. Run the Application
python main.py


🧪 Simulation Example
On launching the app, a window will prompt you to enter username and password.
Enter:
Username: fardwish
Password: 212
Use the 👁️ button to toggle password visibility.
After login:
Choose to Deposit, Withdraw, or Check Balance.
Follow on-screen prompts to complete your transaction.


Features
GUI login system with password security
Toggle password visibility
Basic transaction operations
Beginner-friendly Python code structure (DSA-style logic)
Modular file organization



