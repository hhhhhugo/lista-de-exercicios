def par_ou_impar():
    numero = int(input('me diga um numero'))
    if numero % 2 == 0:
        print (f'{numero} é par')
    else:
        print(f'{numero} é impar')
def checagem_de_idade():
    idade = int(input('qual é a sua idade?'))
    match idade:
        case idade if idade <= 12:
            print('voce é uma criança')
        case idade if idade>= 13 and idade <= 18:
            print('voce é um adolecente')
        case idade if idade > 18:
            print('voce é um adulto')
def validação_da_conta():
    nome = 'zhugue'
    senha = 'xrl'
    usuario = input('coloque seu usuario\n')
    senha_conta = input('coloque sua senha\n')

    if nome != usuario:
        print('usuario incorreto')
    if senha != senha_conta:
        print ('senha incorreta')
    if nome == usuario and senha == senha_conta:
        print(f'bem vindo {usuario}')
def plano_cartesiano():
    x = int(input('informe a coordenada x\n'))
    y = int(input('informe a coordenada y\n'))
    match x,y :
        case x,y if x > 0 and y > 0:
            print('o ponto esta no primeiro quadrante do plano cartesiano')
        case x,y if x < 0 and y > 0:
            print('o ponto esta no segundo quadrante do plano cartesiano')
        case x,y if x < 0 and y < 0:
            print ('o ponto esta no terceiro quadrante do plano cartesiano')
        case x,y if x > 0 and y < 0:
            print('o ponto esta no quarto quadrante do plano cartesiano')
        case x,y if x  == 0 and y != 0:
            print('o ponto esta no eixo do quadrante do plano cartesiano')
        case x,y if x == 0 and y == 0:
            print('o ponto esta na origem quadrante do plano cartesiano')    
def opcoes_de_escolha():
    print('1. par_ou_impar')
    print('2. checagem_de_idade')
    print('3. validação_da_conta')
    print('4. plano_cartesiano')
    opcao_selecionada = int(input('selecione a opcao\n'))
    match opcao_selecionada:
        case 1:
            par_ou_impar()
        case 2:
            checagem_de_idade()
        case 3:
            validação_da_conta()
        case 4:
            plano_cartesiano()
opcoes_de_escolha()            