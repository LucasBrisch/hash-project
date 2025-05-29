# Trabalho individual de Lucas Brisch Zanlorenzi 

import hashlib
import json
import os
import time
import itertools

USERS_FILE = 'users.json'
CHARACTER_SET = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
PASSWORD_LENGTH = 4

def hash_password(password):
    return hashlib.sha256(password.encode('utf-8')).hexdigest()

def load_users():
    if os.path.exists(USERS_FILE):
        try:
            with open(USERS_FILE, 'r', encoding='utf-8') as file:
                return json.load(file)
        except json.JSONDecodeError:
            print(f"Aviso: O arquivo '{USERS_FILE}' está vazio ou corrompido.")
            return {}
    print(f"Erro: Arquivo '{USERS_FILE}' não encontrado.")
    return {}

def brute_force(target_hash, character_set, length):
    start = time.perf_counter()
    
    for attempt in itertools.product(character_set, repeat=length):
        password = ''.join(attempt)
        hashed = hash_password(password)
        
        if hashed == target_hash:
            end = time.perf_counter()
            return password, end - start

    end = time.perf_counter()
    return None, end - start

def run_attack():
    print("=== Força Bruta ===")
    users = load_users()

    if not users:
        print("Nenhum usuário encontrado. Cadastre pelo menos um usuário.")
        return

    targets = []
    for username, password_hash in list(users.items())[:4]:
        targets.append({
            'username': username,
            'hash': password_hash
        })

    if len(targets) < 4:
        print("Poucos usuários cadastrados. Adicione mais usuários.")
        return

    print(f"Tentando quebrar senhas...")

    total_time = 0
    results = []

    for target in targets:
        username = target['username']
        target_hash = target['hash']

        print(f"Quebrando senha do usuário: '{username}'...")

        found_password, time_taken = brute_force(target_hash, CHARACTER_SET, PASSWORD_LENGTH)
        total_time += time_taken

        if found_password:
            print(f"  Senha encontrada: '{found_password}' em {time_taken:.6f} segundos.")
            results.append({
                'username': username,
                'hash': target_hash,
                'password': found_password,
                'time': time_taken
            })
        else:
            print(f"  Senha NÃO encontrada. Tempo decorrido: {time_taken:.6f} segundos.")
            results.append({
                'username': username,
                'hash': target_hash,
                'password': "Não encontrada",
                'time': time_taken
            })

    print("=== Relatório Final ===")
    print(f"Tempo total: {total_time:.6f} segundos.")
    if results:
        print(f"Tempo médio por senha: {total_time / len(results):.6f} segundos.")

    print("\nResumo das Quebras:")
    print("{:<12} {:<64} {:<18} {:<20}".format("Usuário", "Hash", "Senha Descoberta", "Tempo (s)"))
    print("-" * 120)
    for result in results:
        short_hash = result['hash'][:16]
        print(f"{result['username']:<12} {short_hash:<64} {result['password']:<18} {result['time']:.6f}")

if __name__ == "__main__":
    run_attack()
