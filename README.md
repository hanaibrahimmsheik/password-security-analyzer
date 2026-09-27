Password Security Analyzer

A beginner-friendly Python cybersecurity project that analyzes password characteristics and provides basic security recommendations.

Project Overview

The Password Security Analyzer is a command-line Python program that evaluates a password based on its length and character composition.

It calculates a rule-based password strength score, checks whether the password appears in a small list of commonly used passwords, estimates theoretical password entropy, and provides security recommendations.

Features

- Checks password length
- Detects lowercase letters
- Detects uppercase letters
- Detects numbers
- Detects special characters
- Calculates a password strength score out of 6
- Classifies passwords as Weak, Moderate, or Strong
- Checks against a small list of commonly used passwords
- Provides security recommendations
- Calculates a theoretical entropy estimate

Technologies Used

- Python
- Python Standard Library
- VS Code

How It Works

The program asks the user to enter a password and then performs several checks.

1. Password Length

The program calculates the number of characters in the password.

2. Character Type Checks

The program checks whether the password contains:

- Lowercase letters
- Uppercase letters
- Numbers
- Special characters

Python's built-in string methods and "any()" are used for these checks.

3. Password Strength Score

The analyzer uses six rules to calculate a score:

- At least 8 characters
- At least 12 characters
- Contains lowercase letters
- Contains uppercase letters
- Contains numbers
- Contains special characters

The score is classified as:

- 0–2: Weak
- 3–4: Moderate
- 5–6: Strong

This is a rule-based classification created for this project and is not a guarantee of password security.

4. Common Password Detection

The program checks the password against a small hardcoded list of commonly used passwords.

The current list includes examples such as:

- "password"
- "123456"
- "12345678"
- "qwerty"
- "admin"
- "letmein"
- "welcome"

This is a small demonstration list and is not a comprehensive database of compromised passwords.

5. Entropy Estimate

The program calculates a theoretical password entropy estimate based on:

- Password length
- The estimated size of the character set used

The calculation assumes that characters are selected randomly.

Because human-created passwords are often predictable, the entropy value should be treated as a theoretical estimate rather than a guarantee of password security.

Example

Example input:

Hello123!

Example analysis:

Length: 9
Lowercase: True
Uppercase: True
Number: True
Special character: True
Estimated entropy: 58.99 bits

Score: 5 / 6
Strength: Strong
Common password check: Passed

How to Run

1. Install Python

Make sure Python is installed on your computer.

2. Open the project

Open the project folder in VS Code.

3. Run the Python file

Open a terminal in the project folder and run:

python password_analyzer.py

The filename should be changed to match the actual name of the Python file in the project.

4. Enter a password

The program will display the password analysis and security recommendations.

Limitations

This project is designed as a beginner cybersecurity learning project.

Current limitations include:

- The common-password detection uses only a small hardcoded list.
- The entropy calculation assumes random password generation.
- The strength score is rule-based and does not guarantee that a password is secure.
- The program does not check passwords against real-world breach databases.
- The program does not account for every possible password pattern or attack technique.

Future Improvements

Possible future improvements include:

- Expanding common-password detection
- Checking passwords against a larger password dataset
- Improving password pattern detection
- Adding a graphical user interface
- Adding unit tests
- Improving the password strength scoring model

Purpose

This project was created as a beginner cybersecurity project to practice Python programming and understand basic concepts related to password security.