import textwrap

def menu():
    menu = """\n
==========MENU==========
[d] - Depositar
[s] - Sacar
[e] - Extrato
[n] - Nova Conta
[f] - Sair
========================
"""
    return input(textwrap.dedent(menu))

saldo = 0
limite_saque = 3
limite_retirada = 500
extrato = ""
ls = 0
lr = 0

usuario = []
endereco = []


def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito:\tR$ {valor:.2f}\n"
        print("\n=== Depósito realizado com sucesso! ===")
    else:
        print("\n@@@ Operação falhou! O valor informado é inválido. @@@")

    return saldo, extrato
    
def saque(*, saldo, valor, extrato, limite_saque, n_saques, limite_retirada):
    if n_saques > limite_saque:
        print("\n***** Você atingiu seu limite de saques diarios *****")
    
    elif valor > limite_retirada:
        print(f"\n***** Limite para retirada é de R${limite_retirada:.2f} *****")
    
    elif valor > saldo:
        print(f"\n***** Indisponivel - Seu saldo é de R${saldo:.2f} *****")
    
    else:
        saldo -= valor
        n_saques += 1
        extrato += f"Saque: R$ {saldo:.2f}\n"
        print("\n===== Saque realizado com sucesso! =====")
        print(f"===== Seu saldo atual é de R${saldo:.2f} =====")   
    
def extrato():
    print()
    
def nova_conta():
    print()
    
def lista_usuario():
    print()
    
while True:
    opcao = menu()
    
    if opcao == "d":
        print("\n=== Depositar ===\n")
        valor = float(input("Qual valor que deseja depositar? "))
        saldo, extrato = depositar(saldo, valor, extrato)
    
    elif opcao == "s":
        print("\n=== Sacar ===\n")
        valor = float(input("Qual valor que deseja sacar? "))
        if valor <= saldo and lr < limite_retirada and ls + valor <= limite_saque:
            saldo -= valor
            ls += valor
            lr += 1
            print(f"Seu saldo atual é de: R$ {saldo:.2f}")
        else:
            if lr >= limite_retirada:
                print("Você atingiu o limite de saque diário!")
            elif ls + valor > limite_saque:
                print("Limite para saque diário é de R$", limite_saque)
            else:
                print("Sem saldo suficiente para realizar o saque!")
        
            continue
    
    elif opcao == "e":
        print("\nExtrato\n")
        print("Seu saldo atual é de: R$", saldo)
        continue
    
    elif opcao == "n":
        print()
    
    elif opcao == "f":
        print("\nSair\n")
        print("Obrigado por ser nosso cliente, até a proxima!\n")
        break
    
    else:
        print("Opção invalida!")
        continue
    
    