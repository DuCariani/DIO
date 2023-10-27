saldo = 0
limite_saque= 500 # corrigir
limite_retirada = 3 # corrigir
extrato = ""
ls = 0
lr = 0

usuario = []
endereco = []

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

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {saldo:.2f}\n"
        print("\n===== Deposito realizado com Sucesso! =====")
    else:
        print("\nOperação falhou, valor invalido! Refaça operação")
    
    return saldo, extrato
    
def saque(*, saldo, valor, extrato, limite_saque, n_saques, limite_retirada):
    saque_diario = n_saques > limite_saque
    limite_saque = valor > limite_retirada
    sem_saldo = valor > saldo
    
def extrato():
    print()
    
def nova_conta():
    print()
    
def lista_usuario():
    print()
    

while True:
    opcao = input(menu())
    
    if opcao == "d":
        print("\n=== Depositar ===\n")
        valor = float(input("Qual valor que deseja depositar? "))
        saldo, extrato = depositar(saldo, valor, extrato)
        print(f"Seu saldo atual é de: R$ {saldo:.2f}")
        continue
    
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
    
    elif opcao == "f":
        print("\nSair\n")
        print("Obrigado por ser nosso cliente, até a proxima!\n")
        break
    
    else:
        print("Opção invalida!")
        continue
    
    