# Trabalho individual de Lucas Brisch Zanlorenzi 

import time

import random
import json
import hashlib

character = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
PASSWORD_SIZE = 4



def get_users ():
    with open ('users.json', "r") as file:
            users = json.loads(file.read())
            return users

def get_targets ():
    users = get_users()
    targets = []
    
    if len(users) == 0:
        print ("No users were found at the database")
        exit()
    
    count = min(4, len(users))
    
    while len(targets) < count: 
        user = random.choice(users)
        
        if user not in targets:
            targets.append(user) 
            print (f"User {user['username']} added to the target list...")
            time.sleep(0.5)
            
    return targets
            
def brute_force ():
    targets_to_attack = get_targets() 
    results = []
    total_time_start = time.perf_counter()
    print (f"Getting ready to attack {len(targets_to_attack)} users...")
    for current_user_target in targets_to_attack:
        print(f"Attacking user {current_user_target['username']}")
        found_password = False
        user_time_start = time.perf_counter()
        for a in character:
            if found_password: break
            for b in character:
                if found_password: break
                for c in character:
                    if found_password: break
                    for d in character:
                        password_attempt = a + b + c + d
                        if try_login (password_attempt, current_user_target['password'] ): 
                            user_time_end = time.perf_counter()
                            user_time_taken = user_time_end - user_time_start
                            print(f"Password found for {current_user_target['username']}: {password_attempt} in {user_time_taken:.2f} seconds")
                            results.append({"username": current_user_target["username"], "password": password_attempt, "time_taken": user_time_taken})
                            found_password = True
                            break 
        if not found_password:
            print(f"No password found for {current_user_target['username']}")
    
    
    
    print("--- Results ---")
    if results:
        total_time_end = time.perf_counter()
        total_time = total_time_end - total_time_start
        for result in results:
            print(f"Username: {result['username']}, Found password: {result['password']}, time: {result['time_taken']:.2f} Seconds")
            
        print (f"total time taken: {total_time:.2f} seconds")
    else:
        print("No passwords were found")

                            
                            
                        
           
def try_login (password_to_try, actual_hashed_password): 
    
    if hash_pass(password_to_try) == actual_hashed_password: 
        return True 
    return False 
  
    
                    
def hash_pass (password):
    hashed_pass = hashlib.sha256(password.encode('utf-8')).hexdigest()
    return hashed_pass


brute_force()
