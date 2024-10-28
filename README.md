# Password Strength and Leak Checker

Developed a Password Strength and Leak Checker using Python, enhancing security by evaluating password strength and checking for leaks in known data breaches. Implemented a password strength evaluation feature utilizing the `zxcvbn` library, providing users with a detailed strength score and actionable feedback. Integrated a breach check using the "Have I Been Pwned?" API to identify compromised passwords. 

## Features
- **Password Strength Evaluation:** Assesses the strength of passwords with scores ranging from Very Weak to Strong, accompanied by feedback on how to improve.
- **Breach Check:** Checks if the password has been involved in data breaches, informing users if it has been leaked and how many times.

## Tech Stack
- Python
- zxcvbn
- requests
- hashlib

## Usage
1. Run the script and enter a password when prompted.
2. Receive feedback on password strength and potential leaks.

## Requirements
- Python 3.x
- Required libraries: `zxcvbn`, `requests`
