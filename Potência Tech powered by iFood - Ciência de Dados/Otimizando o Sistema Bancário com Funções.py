saldo = 0
limite_saque= 500
limite_retirada = 3
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
        print("\n=====Deposito realizado com Sucesso=====")
    else:
        print("\nOperação falhou, valor invalido! Refaça operação")
    
    return saldo, extrato
    
def saque():
    print("")
    
def extrato():
    print()
    
def nova_conta():
    print()
    
def lista_usuario():
    print()
    

while True:
    opcao = input(menu())
    
    if opcao == "d":
        print("\nDepositar\n")
        valor = float(input("Qual valor que deseja depositar? "))
        saldo += valor
        print("Seu saldo atual é de: R$", saldo)
        continue
    
    elif opcao == "s":
        print("\nSacar\n")
        retirada = float(input("Qual valor que deseja sacar? "))
        if retirada <= saldo and lr < limite_retirada and ls + retirada <= limite_saque:
            saldo -= retirada
            ls += retirada
            lr += 1
            print("Seu saldo atual é de: R$", saldo)
        else:
            if lr >= limite_retirada:
                print("Você atingiu o limite de saque diário!")
            elif ls + retirada > limite_saque:
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
    
    