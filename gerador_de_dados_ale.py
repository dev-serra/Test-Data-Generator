import random
import os

print('Bem-vindo ao Gerador de Dados de Testes - Para finalizar o programa, digite "parar')
print('-'*83)

arquivos = ['nomes.txt','emails.txt','telefones.txt','cidades.txt','estados.txt']

def gerador_de_nomes(nome_do_arquivo):
    try:
        with open(nome_do_arquivo, 'r') as arquivo:
            nome = arquivo.readlines()
        nome_aleatorio = random.choice(nome).strip()
        return nome_aleatorio
    except FileExistsError:
        print(f'O arquivo {nome_do_arquivo} não foi encontrado!')
        return None
    
def gerador_de_emails(nome_do_arquivo):
    try:
        with open(nome_do_arquivo, 'r') as arquivo:
            email = arquivo.readlines()
        email_aleatorio = random.choice(email).strip()
        return email_aleatorio
    except FileExistsError:
        print(f'O arquivo {nome_do_arquivo} não foi encontrado!')
        return None
    
def gerador_de_telefones(nome_do_arquivo):
    try:
        with open(nome_do_arquivo, 'r') as arquivo:
            telefone = arquivo.readlines()
        telefone_aleatorio = random.choice(telefone).strip()
        return telefone_aleatorio
    except FileExistsError:
        print(f'O arquivo {nome_do_arquivo} não foi encontrado!')
        return None
    
def gerador_de_cidades(nome_do_arquivo):
    try:
        with open(nome_do_arquivo, 'r') as arquivo:
            cidade = arquivo.readlines()
        cidade_aleatorio = random.choice(cidade).strip()
        return cidade_aleatorio
    except FileExistsError:
        print(f'O arquivo {nome_do_arquivo} não foi encontrado!')
        return None
    
def gerador_de_estados(nome_do_arquivo):
    try:
        with open(nome_do_arquivo, 'r') as arquivo:
            estado = arquivo.readlines()
        estado_aleatorio = random.choice(estado).strip()
        return estado_aleatorio
    except FileExistsError:
        print(f'O arquivo {nome_do_arquivo} não foi encontrado!')
        return None

def salvar_dados(texto):
    with open('dados.txt', 'a', encoding='utf-8', newline='') as arquivo:
        arquivo.write(texto + os.linesep)

nome = 'nomes.txt'
email = 'emails.txt'
telefone = 'telefones.txt'
cidade = 'cidades.txt'
estado = 'estados.txt'

while True:
    print('''
Escolhe uma ou mais opções abaxio a sere geradas aleatóriamente:
            
[1] - Nome
[2] - E-mail
[3] - Telefone
[4] - Cidade
[5] - Estado
''')
    resposta = input('Digite uma ou mais opções (separadas por vírgula) ou "parar" para finalizar: ')
    if resposta.lower() == "parar":
        break       

    print('-' * 83)
    try:
        respostas = [int(opcao.strip()) for opcao in resposta.split(',')]
        resultados = []

        for opcao in respostas:
            if opcao == 1:
                nome_aleatorio = gerador_de_nomes(nome)
                resultados.append(f"Nome: {nome_aleatorio}")
                print(f"Nome: {nome_aleatorio}")
            elif opcao == 2:
                email_aleatorio = gerador_de_emails(email)
                resultados.append(f"E-mail: {email_aleatorio}")
                print(f"E-mail: {email_aleatorio}")
            elif opcao == 3:
                telefone_aleatorio = gerador_de_telefones(telefone)
                resultados.append(f"Telefone: {telefone_aleatorio}")
                print(f"Telefone: {telefone_aleatorio}")
            elif opcao == 4:
                cidade_aleatoria = gerador_de_cidades(cidade)
                resultados.append(f"Cidade: {cidade_aleatoria}")
                print(f"Cidade: {cidade_aleatoria}")
            elif opcao == 5:
                estado_aleatorio = gerador_de_estados(estado)
                resultados.append(f"Estado: {estado_aleatorio}")
                print(f"Estado: {estado_aleatorio}")
            else:
                print(f"Opção: {opcao} não existe. Digite apenas um ou mais números separados por vírgula entre 1 e 5.")

        if resultados:
            salvar = input("Deseja salvar os resultados em um arquivo txt? (s/n): ").strip().lower()
            if salvar == 's':
                nome_arquivo = input("Digite o nome do arquivo (sem extensão): ").strip()
                with open(f"{nome_arquivo}.txt", "a", encoding='utf-8') as arquivo:
                    for resultado in resultados:
                        arquivo.write(resultado+'\n')
                print(f"Resultados salvos em {nome_arquivo}.txt")
                pergunta = input('Deseja gerar mais dados aleatóriamente ? (s/n): ')
                if pergunta.lower() == 's':
                    resposta
                elif pergunta.lower() == 'n':
                    break
            elif salvar == 'n':
                    break
    except ValueError:
        print('Opção inválida, digite apenas um ou mais números separados por vírgula!')