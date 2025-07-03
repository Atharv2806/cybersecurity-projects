import re

def check_password_strength(password):
    score = 0
    remarks = ""

    # Criteria checks
    if len(password) >= 8:
        score += 1
    if re.search("[a-z]", password) and re.search("[A-Z]", password):
        score += 1
    if re.search("[0-9]", password):
        score += 1
    if re.search("[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1

    # Feedback
    if score == 4:
        remarks = "Strong Password 💪"
    elif score == 3:
        remarks = "Good Password 👍"
    elif score == 2:
        remarks = "Weak Password 😕"
    else:
        remarks = "Very Weak Password 🚫"

    return remarks

# User Input
user_password = input("Enter your password: ")
print(check_password_strength(user_password))