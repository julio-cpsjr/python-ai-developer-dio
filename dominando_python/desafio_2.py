import textwrap

def menu():
    menu = """\n
    ================ MENU ================
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova conta
    [lc]\tListar contas
    [nu]\tNovo usuário
    [q]\tSair
    => """
    return input(textwrap.dedent(menu))


def depositar(saldo, valor, extrato):
    if valor > 0:
        saldo += valor
        extrato += f"Deposito:\tR${saldo:.2f}\n"
        print("\n==========Deposito realizado com sucesso==========")
    else:
        print("\n@@@ Operação falhou! O valor informado é inválido.  @@@")
    return saldo, extrato

def sacar(saldo,valor,extrato,numero_saques,limite_saques,limite):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saque = numero_saques > limite_saques
    
    if excedeu_saldo:
        print("@@@ Saldo insuficiente @@@")
    
    elif excedeu_limite:
        print("@@@ Valor do saque ultrapassa o limite de R$500 @@@")
    
    elif excedeu_saque:
        print("@@@ Número de saques excedido! @@@")

    elif valor > 0:
        numero_saques +=1
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"

    else:
       print("\n@@@ Operação falhou! O valor informado é inválido.  @@@")   
    return saldo, extrato
    
def exibir_extrato(saldo,extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente número): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n@@@ Já existe usuário com esse CPF! @@@")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("=== Usuário criado com sucesso! ===")

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n=== Conta criada com sucesso! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("\n@@@ Usuário não encontrado, fluxo de criação de conta encerrado! @@@")


def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))

def main(): 
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []
    while True:

        opcao = menu()

        if opcao == "d":
            valor = float(input("Informe o valor a ser depositado: "))
            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "s":
            valor = float(input("Informe o valor a ser retirado: "))
            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                limite=limite,
                extrato=extrato,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES)
            
        elif opcao == "e":
            exibir_extrato(saldo,extrato=extrato)

        elif opcao == "q":
            break
        
        elif opcao == "nu":
            criar_usuario(usuarios)

        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "lc":
            listar_contas(contas)
            
        else:
            print("@@@ Operação inválida! Por favor selecione novamente a operação desejada. @@@")


main()