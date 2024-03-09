import requests

# Replace these with the actual API URL and credentials
LOGIN_URL = "https://y99.in/web/login"
MESSAGE_URL = "https://chat.example.com/api/message"
USERNAME = "l"
PASSWORD = "

def login():
    """Function to log into the chat platform."""
    response = requests.post(LOGIN_URL, json={"username": USERNAME, "password": PASSWORD})
    if response.status_code == 200:
        return response.json()['token']
    else:
        print("Login failed")
        return None

def send_message(token, message):
    """Function to send a message."""
    headers = {'Authorization': f'Bearer {token}'}
    response = requests.post(MESSAGE_URL, headers=headers, json={"message": message})
    if response.status_code == 200:
        print("Message sent successfully")
    else:
        print("Failed to send message")

if __name__ == "__main__":
    token = login()
    if token:
        send_message(token, "Hello, world!")
