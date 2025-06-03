# Hash Project

This project was developed as part of a Cybersecurity course assignment. It demonstrates the importance of using hashing and salting to securely store user passwords and protect against brute-force attacks.

---

## 📝 Project Overview

This project consists of three main stages:

1️⃣ **Basic Authentication System (No Salt)**  
A simple login and registration system that hashes user passwords and stores them in a JSON file.

2️⃣ **Brute-Force Attack Script**  
A script that attempts to crack user passwords by brute-forcing the hashed passwords stored in the JSON file.

3️⃣ **Authentication System with Salt**  
An improved login and registration system that uses a unique salt for each password before hashing, making brute-force attacks significantly harder.

---

## 📂 Project Structure

- **authentication.py** — Basic login and registration system without salt.
- **hash-break.py** — Brute-force attack script to crack user passwords.
- **salted_hash.py** — Improved login and registration system that uses salted hashes.
- **users.json** — JSON file that stores user credentials (username, hashed password and the users`s random salt (if generated).

---

## 🔑 How It Works

### 1. `authentication.py`
- Users can register and log in.
- Passwords are hashed (using a hash algorithm) before being stored in `users.json`.
- **Weakness:** Because no salt is used, identical passwords produce identical hashes, making brute-force attacks feasible.

### 2. `hash-break.py`
- Attempts to brute-force hashed passwords by trying possible combinations until it finds a match.
- Demonstrates how weak password hashing (without salt) is vulnerable to attacks.

### 3. `salted_hash.py`
- Enhances security by generating a random salt for each password before hashing.
- Each user’s password is stored as a unique hash, even if multiple users share the same password.
- This makes brute-force attacks much more difficult.
