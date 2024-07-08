import re

def check_password_complexity(password):
    """
    Evaluate the complexity of the provided password based on specific criteria.
    
    Args:
    password (str): The password to be evaluated.
    
    Returns:
    str: Feedback on the password strength.
    """
    # Criteria for password strength
    length_criteria = len(password) >= 8
    uppercase_criteria = re.search(r'[A-Z]', password) is not None
    lowercase_criteria = re.search(r'[a-z]', password) is not None
    digit_criteria = re.search(r'\d', password) is not None
    special_char_criteria = re.search(r'[!@#$%^&*(),.?":{}|<>]', password) is not None

    # Collect feedback based on criteria
    feedback = []
    if not length_criteria:
        feedback.append("- Password should be at least 8 characters long")
    if not uppercase_criteria:
        feedback.append("- Include at least one uppercase letter")
    if not lowercase_criteria:
        feedback.append("- Include at least one lowercase letter")
    if not digit_criteria:
        feedback.append("- Include at least one digit")
    if not special_char_criteria:
        feedback.append("- Include at least one special character (!@#$%^&*(),.?\":{}|<>)")

    if not feedback:
        return "Your password is strong."
    else:
        return "Your password is weak. Consider the following improvements:\n" + "\n".join(feedback)

def main():
    """
    Main function to run the password complexity checker.
    """
    print("Welcome to the Password Complexity Checker")

    # Prompt user for password input
    password = input("Please enter your password: ")

    # Evaluate and provide feedback on password complexity
    result = check_password_complexity(password)
    print(result)

if __name__ == "__main__":
    main()

