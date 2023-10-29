saldo = 0
limite_saque= 500
limite_retirada = 3
ls = 0
lr = 0

menu = """\n
==========MENU==========
[d] - Depositar
[s] - Sacar
[e] - Extrato
[f] - Sair
========================
"""

while True:
    opcao = input(menu)
    
    if opcao == "d":
        print("\nDepositar\n")
        deposito = float(input("Qual valor que deseja depositar? "))
        saldo += deposito
        print(f"Seu saldo atual é de: R$ {saldo:.2f}")
        continue
    
    elif opcao == "s":
        print("\nSacar\n")
        retirada = float(input("Qual valor que deseja sacar? "))
        if retirada <= saldo and lr < limite_retirada and ls + retirada <= limite_saque:
            saldo -= retirada
            ls += retirada
            lr += 1
            print(f"Seu saldo atual é de: R$ {saldo:.2f}")
        else:
            if lr >= limite_retirada:
                print("Você atingiu o limite de saque diário!")
            elif ls + retirada > limite_saque:
                print(f"Limite para saque diário é de R$ {limite_saque:.2f}")
            else:
                print("Sem saldo suficiente para realizar o saque!")
        
            continue
    
    elif opcao == "e":
        print("\nExtrato\n")
        print(f"Seu saldo atual é de: R$ {saldo:.2f}")
        continue
    
    elif opcao == "f":
        print("\nSair\n")
        print("\nObrigado por ser nosso cliente, até a proxima!\n")
        break
    
    else:
        print("Opção invalida!")
        continue