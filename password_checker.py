import zxcvbn
import requests
import hashlib

def check_password_strength(password):
    results = zxcvbn.zxcvbn(password)
    score = results['score']
    feedback = results['feedback']['warning']

    if score == 0:
        strength = "Very Weak"
    elif score == 1:
        strength = "Weak"
    elif score == 2:
        strength = "Fair"
    elif score == 3:
        strength = "Good"
    else:
        strength = "Strong"

    return strength, feedback

def check_password_leak(password):
    sha1_password = hashlib.sha1(password.encode()).hexdigest().upper()
    first5_char, tail = sha1_password[:5], sha1_password[5:]
    url = f'https://api.pwnedpasswords.com/range/{first5_char}'
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f'Error fetching: {res.status_code}, {res.text}')
    hashes = (line.split(':') for line in res.text.splitlines())
    count = next((int(count) for tail_part, count in hashes if tail_part == tail), 0)
    if count:
        return True, [{'Name': f'This password has been leaked {count} times'}]
    else:
        return False, None

def main():
    password = input("Enter a password: ")

    strength, feedback = check_password_strength(password)
    print(f"Password strength: {strength}")
    print(f"Feedback: {feedback}")

    is_pwned, breach_data = check_password_leak(password)
    if is_pwned:
        print("Warning: This password has been leaked in the following breaches:")
        for breach in breach_data:
            print(f"- {breach['Name']}")
    else:
        print("This password has not been leaked (as far as we know).")

if __name__ == "__main__":
    main()