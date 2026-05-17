#!/usr/bin/python3

import requests

def get_users():
    response = requests.get("https://api.example.com/users")
    response.raise_for_status()  # Check if the request was successful
    return response.json()

def filter_active(users):
    return

def main():
    users = get_users()
    active=filter_active(users)

    for user in active:
        print(user['name'])

if __name__ == "__main__":
    main()

    
    

