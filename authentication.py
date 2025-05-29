# Trabalho individual feito por Lucas Brisch Zanlorenzi

import hashlib
import json
import os

# Define o nome do arquivo onde os usuários serão armazenados
USERS_FILE = 'users.json'

def hash_password(password):
   
    hashed_pass = hashlib.sha256(password.encode('utf-8')).hexdigest()
    return hashed_pass

def load_users():
    if os.path.exists(USERS_FILE):
        try:
            with open(USERS_FILE, 'r', encoding='utf-8') as f:
                # Carrega o conteúdo do arquivo JSON para um dicionário Python.
                return json.load(f)
        except json.JSONDecodeError:
            # Em caso de erro na decodificação JSON (arquivo corrompido ou vazio),
            # imprime um aviso e retorna um dicionário vazio para evitar falhas.
            print(f"Aviso: O arquivo '{USERS_FILE}' está corrompido ou vazio. Criando um novo.")
            return {}
    return {}

def save_users(users):
    with open(USERS_FILE, 'w', encoding='utf-8') as f:
        json.dump(users, f, indent=4, ensure_ascii=False)

def register_user():
    print("--- Cadastro de Usuário ---")
    users = load_users()

    while True:
        username = input("Digite o nome de usuário (4 caracteres): ").strip()
        if len(username) == 4:
            if username not in users:
                break
            else:
                print("Nome de usuário já existe. Escolha outro.")
        else:
            print("O nome de usuário deve ter exatamente 4 caracteres.")

    while True:
        password = input("Digite a senha (4 caracteres): ")
        if len(password) == 4:
            break
        else:
            print("A senha deve ter exatamente 4 caracteres.")
    hashed_password = hash_password(password)

    users[username] = hashed_password
    save_users(users)
    print(f"Usuário '{username}' cadastrado com sucesso!")

def authenticate_user():
    print("--- Autenticação de Usuário ---")
    users = load_users()

    username = input("Digite o nome de usuário: ").strip()
    password = input("Digite a senha: ").strip()

    if username in users:
        user_password_hash = hash_password(password)
        if users[username] == user_password_hash:
            print(f"Autenticação bem-sucedida para o usuário '{username}'!")
        else:
            print("Senha ou usuario incorreto.")
    else:
        print("Senha ou usuario incorreto.")

def main():
    while True:
        print("--- Menu Principal ---")
        print("1. Cadastrar Usuário")
        print("2. Entrar com Usuário")
        print("3. Sair")

        choice = input("Escolha uma opção: ")

        if choice == '1':
            register_user()
        elif choice == '2':
            authenticate_user()
        elif choice == '3':
            print("Saindo da aplicação...")
            break
        else:
            print("Opção inválida. Por favor, tente novamente.")

if __name__ == "__main__":
    main()
