menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=>"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor a ser depositado \n=>"))
        saldo += valor
        extrato += f"Deposito: R$ {saldo:.2f}\n"
        print(f"O valor depositado foi R${saldo}")
    
    elif opcao == "s":
        if numero_saques <= LIMITE_SAQUES:
            valor = float(input("Informe o valor a ser retirado \n=>"))
            if saldo >= valor:
                if valor <= 500:
                    saldo -= valor
                    extrato += f"Saque: R$ {valor:.2f}\n"
                else:
                    print("@@@ Valor do saque ultrapassa o limite de R$500 @@@")
            else:
                print("@@@ Saldo insuficiente @@@")
        else:
            print("@@@ Número de saques excedido! @@@")        

    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")