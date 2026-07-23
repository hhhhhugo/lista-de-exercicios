import os;
numero = [1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 ,9 , 10]
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
            case 4:            
                soma_dos_numeros_impares()
            case 5:
                tabuada()
    except:
        opcao_invalida()            

def exibir_opcoes():
    print('1. numero de uma a 10')
    print('2. lista com quatro nomes')
    print('3. ano de nascimento e ano atual')
    print('4. soma dos numeros impares')
def exibir_o_nome_do_programa():
    print('Listas de exercicio 2\n ')
def numeros_de_1_a_10():
    
    ordem_decrescente = input('em ordem decrescente? y/n?')
    decrescente_numero = sorted(numero, reverse=True)
    match ordem_decrescente:
        case 'y':
            numeros_listagem(decrescente_numero)

        case 'n':
            numeros_listagem(numero)

    reiniciar()
def numeros_listagem(tipo):
    for numeros in tipo:
        print('.' + f'{numeros}')
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
def soma_dos_numeros_impares():
    numero_impares = [num for num in numero if num % 2 != 0]
    print(f'a soma dos numeros impares de 1 a 10 e {str(sum(numero_impares))}')
    reiniciar()
def tabuada():
    numero_tabuada = int(input('digite um numero'))
    for numeros in numero:
        print(f'eis a tabuada de {str(numero_tabuada)}')
        print(numeros*numero_tabuada)
        reiniciar()
def reiniciar():
    input('\nDigite uma tecla para reiniciar')
    main()
def main():
    os.system('cls')
    exibir_o_nome_do_programa()
    exibir_opcoes()
    escolher_opcoes()
main()
