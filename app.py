import sys
from pathlib import Path

# Adiciona a biblioteca (submódulo) ao caminho de importação
sys.path.insert(0, str(Path(__file__).parent / "password-tools"))

from password_tools import (
    generate_password,
    check_strength,
    is_common_password,
    generate_passphrase,
)
def mostrar_menu():
    print("=" * 40)
    print("      PASSWORD TOOLS CLI")
    print("=" * 40)
    print("1 - Gerar senha segura")
    print("2 - Verificar força da senha")
    print("3 - Verificar senha comum")
    print("4 - Gerar passphrase")
    print("0 - Sair")
    print("=" * 40)
    
while True:
    mostrar_menu()

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        tamanho = int(input("Tamanho da senha: "))
        senha = generate_password(length=tamanho)
        print(f"\nSenha gerada: {senha}\n")

    elif opcao == "2":
        senha = input("Digite a senha: ")
        print(f"\nForça: {check_strength(senha)}\n")

    elif opcao == "3":
        senha = input("Digite a senha: ")

        if is_common_password(senha):
            print("\nEssa senha é muito comum!\n")
        else:
            print("\nEssa senha não está na lista de senhas comuns.\n")

    elif opcao == "4":
        print(f"\nPassphrase: {generate_passphrase()}\n")

    elif opcao == "0":
        print("\nAté logo!")
        break

    else:
        print("\nOpção inválida!\n")