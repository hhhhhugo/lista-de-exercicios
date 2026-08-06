import os;

dados_de_pessoas = [{'nome':'Fernando','idade':'17','cidade':'Londrina'}]

def exibir_opcoes():
    print('.1 exercicios relacionados a lista dados_de_pessoas')
    print('.2 dicionario de 1 ao 5')
    print('.3 verificao de chave no dicionario')
    print('.4 frequencia de cada palavra em uma frase utilizando um dicionario')

def exibir_opcoes_ex1():
    os.system('cls')
    print('.1 alterar a idade')
    print('.2 Adicionar um campo de profissao para essa pessoa')
    print('.3 Remover um item do dicionario')

    escolha_uma_opcao_ex1()

def escolha_uma_opcao_ex1():
    opcao_escolhida = int(input('escolha uma opcao'))
    match opcao_escolhida:
            case 1:
                print('.1 alterar a idade')
            case 2:
                print('.2 Adicionar um campo de profissao para essa pessoa')
            case 3:
                print('.3 Remover um item do dicionario')

def escolha_uma_opcao():
    opcao_escolhida = int(input('escolha uma opcao'))
    match opcao_escolhida:
        case 1:
            exibir_opcoes_ex1()
        case 2:
            print('.2 dicionario de 1 ao 5')
        case 3:
            print('.3 verificao de chave no dicionario')
        case 4:
            print('.4 frequencia de cada palavra em uma frase utilizando um dicionario')

def alterar_idade():
    for pessoa in dados_de_pessoas:
        nome_pessoa = pessoa['nome']
        print('- '+ f'{nome_pessoa}')
    nome_pessoa_alt = input('qual o nome da pessoa para alterar a idade')
    nome_econtrado = False

    for pessoa in dados_de_pessoas:
        if nome_pessoa_alt == pessoa['nome']:
            nome_econtrado = True   

def main():
    os.system('cls')
    exibir_opcoes()
    escolha_uma_opcao()

def reiniciar():
    input('\npressione uma tecla para voltar ao menu principal')
    main()