import os

usuarios = {}

def add_usuario(nome, senha):
    if len(senha) >= 4:
        login = len(usuarios) + 1
        usuarios[login] = {'nome': nome, 'senha': senha, 'saldo': 0}
        print(f"Usuário '{nome}' adicionado com sucesso. Número de login: {login}.")
        input('Pressione enter para retornar ao menu principal')
        os.system('cls')
        return True
    else:
        print("A senha deve ter pelo menos 4 caracteres. Por favor, reescreva a senha.")
        return False

def login():
    while True:
        login_input = input('Número de login do usuário: ')
        if login_input.isdigit():
            login_input = int(login_input)
            if login_input in usuarios:
                senha_input = input('Senha: ')
                if senha_input == usuarios[login_input]['senha']:
                    return login_input
                else:
                    print('Senha incorreta. Tente novamente.')
            else:
                print('Usuário não encontrado. Tente novamente.')
        else:
            print('Informe o NÚMERO do seu login.')

def depositar(login, valor):
    if login in usuarios:
        usuarios[login]['saldo'] += valor
        print(f"Depósito de R${valor:.2f} realizado com sucesso para o usuário '{usuarios[login]['nome']}'.")
        input('Pressione enter para retornar ao menu principal')
        os.system('cls')
    else:
        print(f"Usuário com número de login {login} não encontrado. Não foi possível realizar o depósito.")

def sacar(login, valor):
    if login in usuarios:
        if usuarios[login]['saldo'] >= valor:
            usuarios[login]['saldo'] -= valor
            print(f"Saque de R${valor:.2f} realizado com sucesso para o usuário '{usuarios[login]['nome']}'.")
            input('Pressione enter para retornar ao menu principal')
            os.system('cls')
        else:
            print(f"Usuário '{usuarios[login]['nome']}' não possui saldo suficiente para o saque.")
    else:
        print(f"Usuário com número de login {login} não encontrado. Não foi possível realizar o saque.")

def transferir(origem, destino, valor):
    if origem in usuarios and destino in usuarios:
        if usuarios[origem]['saldo'] >= valor:
            usuarios[origem]['saldo'] -= valor
            usuarios[destino]['saldo'] += valor
            print(f"Transferência de R${valor:.2f} realizada com sucesso de '{usuarios[origem]['nome']}' para '{usuarios[destino]['nome']}'.")
            input('Pressione enter para retornar ao menu principal')
            os.system('cls')
        else:
            print(f"Usuário '{usuarios[origem]['nome']}' não possui saldo suficiente para a transferência.")
    else:
        print(f"Usuário de origem ou destino não encontrado. Não foi possível realizar a transferência.")

def mostrar_saldo(login):
    if login in usuarios:
        saldo = usuarios[login]['saldo']
        print(f"Saldo do usuário '{usuarios[login]['nome']}': R${saldo:.2f}")
        input('Pressione enter para retornar ao menu principal')
        os.system('cls')
    else:
        print(f"Usuário com número de login {login} não encontrado.")

while True:
    print('=' * 33)
    print('|       BANCO PIZAPREMIUM      |')
    print('=' * 33)
    print('*-------------------------------*')
    print("|     [1]. Criar Usuário        |")
    print("|     [2]. Entrar               |")
    print("|     [3]. Sair                 |")
    print('*-------------------------------*')

    escolha_inicio = input("Escolha a opção: ")

    if escolha_inicio == '1':
        while True:
            print('Cadastrar usuário\nDigite [0] se quiser retornar ao menu principal')
            nome = input('\nNome do usuário: ').title()
            if nome == '0':
                break
            if nome.isdigit():
                print('O nome não pode conter números.')
                continue

            senha = input('Senha (pelo menos 4 caracteres): ')

            if len(senha) >= 4:
                add_usuario(nome, senha)
                break
            while not add_usuario(nome, senha):
                senha = input('Senha inválida. Por favor, reescreva a senha: ')
                break

    elif escolha_inicio == '2':
        logged_in_user = login()
        os.system('cls')
        print(f"Bem-vindo, {usuarios[logged_in_user]['nome']}!")

        while True:
            print('=' * 33)
            print('|       BANCO PIZAPREMIUM      |')
            print('=' * 33)
            print('*-------------------------------*')
            print("|     [1]. Depositar            |")
            print("|     [2]. Sacar                |")
            print("|     [3]. Transferir           |")
            print("|     [4]. Mostrar Saldo        |")
            print("|     [5]. Sair                 |")
            print('*-------------------------------*')

            escolha_menu = input("Escolha a opção: ")

            if escolha_menu == '1':
                valor_deposito = float(input('Valor a depositar: R$'))
                depositar(logged_in_user, valor_deposito)

            elif escolha_menu == '2':
                valor_saque = float(input('Valor a sacar: R$'))
                sacar(logged_in_user, valor_saque)

            elif escolha_menu == '3':
                destino = int(input('Número de login do usuário de destino: '))
                valor_transferencia = float(input('Valor a transferir: R$'))
                transferir(logged_in_user, destino, valor_transferencia)

            elif escolha_menu == '4':
                mostrar_saldo(logged_in_user)

            elif escolha_menu == '5':
                print(f"Saindo da conta de '{usuarios[logged_in_user]['nome']}'.")
                break

            else:
                print("Opção inválida. Escolha novamente.")
            input('Pressione enter para continuar...')
            os.system('cls')  # Limpar a tela após cada escolha no menu do usuário logado

    elif escolha_inicio == '3':
        print("Encerrando o programa.")
        break

    else:
        print("Opção inválida. Escolha novamente.")
