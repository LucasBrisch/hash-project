# Trabalho individual de Lucas Brisch Zanlorenzi 

import json
import hashlib


def login():
    print ("Login")
    username = input("Username: ")
    password = input("Password: ")
    
    with open ('users.json', "r") as file:
        users = json.loads(file.read())
        
        for user in users:
            if user["username"] == username and user["password"] == hash_pass(password):
                print("Login successful")
                return

        print("Invalid user or password")
        login()


def register():
    print ("Register")
    username = input("Username (4 digits) : ")
    
    if len(username) != 4:
        print("Username must be 4 characters long")
        register()
    
    if user_exists(username):
        print ("User already exists")
        register()
    else:
        print("create a 4 digit password")
        password = input("Password: ")
        password2 = input("Confirm Password: ")
        
        if len(password) != 4 and len(password2) != 4:
            print("Password must be at least 4 characters long")
            register()
        
        if password == password2:
            User_to_database(username, hash_pass(password))
        else:
            print ("Password does not match")
            register()
            
            
def hash_pass (password):
    hashed_pass = hashlib.sha256(password.encode('utf-8')).hexdigest()
    return hashed_pass
        
        
def user_exists(username):
    
    with open("users.json", "r") as file:
        
        users = json.load(file)
        return username in users


def User_to_database(username, password):
    with open ('users.json', "r") as file:
        users = json.loads(file.read())
    
    
    with open("users.json", "w") as file:
        
        
        users.append({"username": username, "password": password})      
        
        file.write(json.dumps(users))
        
        print ("User registered")

    


def main():
    
    print ("1 - login")
    print ("2 - register")
    
    option = input("Choose an option: ")
    if option == "1":
        login()
    elif option == "2":
        register()
        
        
main()