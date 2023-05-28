import random
import string
import webbrowser

def generate_random_string(length):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

def generate_random_gmail():
    username = generate_random_string(10)
    domain = "gmail.com"
    return f"{username}@{domain}"

def generate_random_password():
    return generate_random_string(12)

def open_website(url):
    webbrowser.open(url)

if __name__ == "__main__":
    gmails = []
    passwords = []

    for _ in range(1000):
        gmail = generate_random_gmail()
        password = generate_random_password()
        gmails.append(gmail)
        passwords.append(password)

    for i in range(1000):
        print(f"Gmail: {gmails[i]} | Password: {passwords[i]}")

    website_url = "https://github.com/mode4kill"  # Replace with the actual URL you want to open
    open_website(website_url)
input('Press ENTER to exit')