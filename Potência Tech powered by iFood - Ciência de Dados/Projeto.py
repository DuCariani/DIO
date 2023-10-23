saldo = 0
limite_saque= 500
limite_retirada = 3
ls = 0
lr = 0

menu = """

[d] - Depositar
[s] - Sacar
[e] - Extrato
[f] - Sair

"""

while True:
    opcao = input(menu)
    
    if opcao == "d":
        print("\nDepositar\n")
        deposito = float(input("Qual valor que deseja depositar? "))
        saldo += deposito
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