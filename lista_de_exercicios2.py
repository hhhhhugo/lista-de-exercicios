import os;
def opcao_invalida():
    print('opcao invalida\n')
    reiniciar()
def escolher_opcoes():
    try:
        opcao_escolhida = int(input('\nescolha um exercicio\n'))
        match opcao_escolhida:
            case 1:
                numeros_de_1_a_10()
            case 2:
                lista_com_quatro_nome()
            case 3:
                ano_de_nascimento_e_ano_atual()        
    except:
        opcao_invalida()            

def exibir_opcoes():
    print('1. numero de uma a 10')
    print('2. lista com quatro nomes')
    print('3. ano de nascimento e ano atual')
def exibir_o_nome_do_programa():
    print('Listas de exercicio 2\n ')
def numeros_de_1_a_10():
    numero = [1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 ,9 , 10]
    for numeros in numero:
        print('.' + f'{numeros}')
       
    reiniciar()    
def lista_com_quatro_nome():
    nomes = ['Leandro','Gustavo','Geovani','Zhugue']
    for index, nome in enumerate(nomes):
        print(f'{index+1}'+ '. ' + f'{nome}')
    reiniciar()    
def ano_de_nascimento_e_ano_atual():
    anos = []
    ano_de_nascimento = int(input('Informe seu ano de nascimento\n'))
    anos.append(ano_de_nascimento)
    ano_atual = int(input('Qual e o ano atual\n'))
    anos.append(ano_atual)
    print(f'voce nasceu em {str(ano_de_nascimento)}, o ano atual e {str(ano_atual)}\n voce tem {str(ano_atual - ano_de_nascimento)} anos ')
def reiniciar():
    input('\nDigite uma tecla para reiniciar')
    main()
def main():
    os.system('cls')
    exibir_o_nome_do_programa()
    exibir_opcoes()
    escolher_opcoes()
main()
