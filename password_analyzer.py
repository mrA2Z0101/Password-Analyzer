import re
import math
import string
import tkinter as tk
from tkinter import messagebox

def calculate_entropy(password):
    """Calculate the entropy of a password."""
    pool = 0
    if any(char.islower() for char in password):
        pool += 26
    if any(char.isupper() for char in password):
        pool += 26
    if any(char.isdigit() for char in password):
        pool += 10
    if any(char in string.punctuation for char in password):
        pool += len(string.punctuation)
    entropy = len(password) * math.log2(pool)
    return entropy

def evaluate_password(password):
    """Evaluate the strength of a password."""
    if len(password) < 8:
        return "Very Weak", "Password is too short. Use at least 8 characters."

    if not re.search("[a-z]", password):
        return "Weak", "Add lowercase letters to your password."
    if not re.search("[A-Z]", password):
        return "Weak", "Add uppercase letters to your password."
    if not re.search("[0-9]", password):
        return "Weak", "Add digits to your password."
    if not re.search("[@#$%^&*(),.?\":{}|<>]", password):
        return "Weak", "Add special characters to your password."

    entropy = calculate_entropy(password)
    
    if entropy < 50:
        return "Medium", "Password could be stronger. Consider adding more variety."
    elif entropy < 80:
        return "Strong", "Good password. It's fairly strong."
    else:
        return "Very Strong", "Excellent password. It's very strong."

def analyze_password():
    password = password_entry.get()
    strength, feedback = evaluate_password(password)
    messagebox.showinfo("Password Strength", f"Strength: {strength}\nFeedback: {feedback}")

# Set up the GUI
root = tk.Tk()
root.title("Password Strength Analyzer")

frame = tk.Frame(root, padx=10, pady=10)
frame.pack(padx=10, pady=10)

label = tk.Label(frame, text="Enter a password to evaluate:")
label.pack(pady=5)

password_entry = tk.Entry(frame, show="*", width=30)
password_entry.pack(pady=5)

analyze_button = tk.Button(frame, text="Analyze", command=analyze_password)
analyze_button.pack(pady=10)

# Run the GUI event loop
root.mainloop()
