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

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito:\tR$ {valor:.2f}\n"
        print("\n=== Depósito realizado com sucesso! ===")
    else:
        print("\n*** Operação falhou! O valor informado é inválido. ***")

    return saldo, extrato

saldo = 0
n_saques = 0
limite_saque=3
limite_retirada = 500
extrato = " "
ls = 0
lr = 0
LIMITE_SAQUE = 3

usuario = []
endereco = []

    
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
    
def exibir_extrato(saldo, /, *, extrato):
    print("\n========== EXTRATO ==========")
    print("Não há movimentações em sua conta" if not extrato else extrato)
    print(f"\nSaldo:\t\t {saldo:.2f}")
    print("===============================")
    
def nova_conta(agencia, n_conta, usuario):
    cpf = input("Informe o número de CPF: ")
    usuario = listar_usuario(cpf, usuario)
    
    if usuario:
        print("\n=== Concluído! ===")
        return {"agencia": agencia, "n_conta": n_conta, "usuario": usuario}
    
    print("\n*** Não foi localizado o usuario! ***")
    
def novo_usuario(usuario):
    cpf = input("Informe o CPF (apenas numeros): ")
    usuario = filtrar_usuario(cpf, usuario)
    
    if usuario:
        print("\n*** CPF já cadastrado! ***")
        return

    nome = input("Informe o nome completo: ")
    nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço completo: ")
    
    usuario.append({"nome": nome, "nascimento": nascimento, "cpf": cpf, "endereco": endereco})
    
    print("=== Usuario cadastrado com Sucesso! ===")
    
def listar_usuario(cpf, usuarios):
    usuario_filtrado = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuario_filtrado[0] if usuario_filtrado else None
    
def listar_conta(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['n_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))
    
    
while True:
    opcao = menu()
    
    if opcao == "d":
        print("\n=== Depositar ===\n")
        valor = float(input("Qual valor que deseja depositar? "))
        saldo, extrato = depositar(saldo, valor, extrato)
    
    elif opcao == "s":
        print("\n=== Sacar ===\n")
        valor = float(input("Qual valor que deseja sacar? "))
        saldo, extrato = saque(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite_retirada=limite_retirada,
                n_saques=n_saques,
                limite_saque=LIMITE_SAQUE,
            )        
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
    
    