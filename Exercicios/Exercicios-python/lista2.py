import os

projetos = ['jogos', 'python', 'analise de dados', None, 'aplicativo movel']
dados = {'nome': 'Pedro', 
         'idade': 30, 
         'cidade': 'Porto Alegre'
}





def lista_exercicios():
    print('########################')
    print('1. Numero par ou impar')
    print('2. Categoria de idade')
    print('3. Usuario e senha')
    print('4. Quadrantes')
    print('5. Portifolio')
    print('6. Validação de encomenda')
    print('7. Listas')
    print('8 Tabuada')
    print('9. Soma com valores invalidos')
    print('10. Calcular Média')
    print('11. Manipulação de Dicionário')
    print('12. Dicionario Quadrado')
    print('13. Verificar Dicionario')
    print('14. Numero da frequencia de palavras no Dicionario')
    print('15. Sair')
    print('########################')

def escolher_opcao():
    opcao_escolhida = int(input('\nEscolha uma opção: '))
    match opcao_escolhida:
        case 1:
            par_ou_impar()
        case 2:
            categoria_idade()
        case 3:
            login()
        case 4:
            quadrante()
        case 5:
            portifolio()
        case 6:
            validacao_encomenda()
        case 7:
            listas()
        case 8:
            tabuada()
        case 9:
            soma_execpt()
        case 10:
            calcular_media()
        case 11:
            manipulando_dicionario()
        case 12:
            dicionario_quadrado()
        case 13:
            dicionario_verificar()
        case 14:
            dicionario_frequencia()
        case 15:
            finalizar_app()
        case _:
            print('Opcao invalida.')


def finalizar_app():
    os.system('cls')
    print('Encerrando o programa\n')

def par_ou_impar():
    # Exercicio 1
    numero = int(input('Digite um numero: '))
    if numero % 2 == 0:
        print('Numero par')
    else:
        print('Numero impar')

def categoria_idade():
    #Exercicio 2
    idade = int(input('Digite a sua idade: '))
    if idade >= 0 and idade <= 12:
        print('Você é criança')
    elif idade >= 13 and idade <= 18:
        print('Você é adolescente')
    elif idade > 18:
        print('Adulto')
    else:
        print('Idade invalida.')

def login():
    usuario = 'pedro'
    senha = 'boris'

    entrada_usuario = input('Digite o seu usuário: ')
    entrada_senha = input('Digite a sua senha: ')

    if entrada_usuario == usuario and entrada_senha == senha:
        print('Bem-vindo')
    else:
        print('Usuário ou senha invalidos')
    
def quadrante():
    valor_x = int(input('Digite o valor de x: '))
    valor_y = int(input('Digite o valor de y: '))

    if valor_x > 0 and valor_y > 0:
        print(f'O ponto ({valor_x},{valor_y}) fica no primeiro quadrante')
    elif valor_x < 0 and valor_y > 0:
        print(f'O ponto ({valor_x},{valor_y}) fica no segundo quadrante')
    elif valor_x < 0 and valor_y < 0:
        print(f'O ponto ({valor_x},{valor_y}) fica no terceiro quadrante')
    elif valor_x > 0 and valor_y < 0:
        print(f'O ponto ({valor_x},{valor_y}) fica no quarto quadrante')
    elif valor_x == 0 and valor_y == 0:
        print(f'O ponto ({valor_x},{valor_y}) esta na origem')
    else:
        print(f'O ponto ({valor_x},{valor_y}) esta no eixo')

def portifolio():
    for projeto in projetos:
        if projeto:
            print(f'Projeto: {projeto}')
        else:
            print('Projeto não disponível.')

def validacao_encomenda():
    encomendas = input("Digite os números das encomendas separados por vírgula: ").split(',')
    try:
        for encomenda in encomendas:
            print(int(encomenda))
    except ValueError:
        print('Uma das entradas não é um número válido')

def listas():
    numeros = list(range(1,11))    
    nomes = ['Pedro', 'Joao', 'Cassiano','Luis'] 
    print(nomes)   
    idade = [1994, 2025]
    print(idade)
    
    print(numeros)    
    soma_lista(numeros)
    lista_reversa(numeros)

def soma_lista(lista):
    soma = 0
    for numero in lista:
        if numero % 2 != 0:
            soma += numero
    print(f'A soma dos numeros impares da lista é: {soma}')

def lista_reversa(lista):
    print(sorted(lista, reverse=True))

def tabuada():
    # numero_lista = list(range(1,11))
    # numero_solicitado = int(input('Digite um numero: '))
    # for numero in numero_lista:
    #     numero *= numero_solicitado
    #     print(numero)
    # Minha resolução

    numero_solicitado = int(input('Digite um numero: '))
    lista_tabuada = []
    for i in range(1, 11):
        lista_tabuada.append(numero_solicitado * i)
    
    print(f'A tabuada do numero {numero_solicitado} é: {lista_tabuada}')
    
def soma_execpt():
    numeros = [1, 2, 3, 4, 'a', 5, 6, 7, None, 8, 'd', 10]
    soma = 0
    for numero in numeros:
        try:
            soma += int(numero)
        except(ValueError,TypeError):
            print(f'Numero invalido ignorado: {numero}')
    
    print(f'Soma total dos numero validos: {soma}')

def calcular_media():
    numeros = [10, 20, 30, 40, 50]
    # numeros = []
    try:
        media = (sum(numeros)/len(numeros))
        print(f'A média é: {media}')
    except ZeroDivisionError:
        print('Não é possivel calcular uma média com uma lista vazia')

def manipulando_dicionario():
    print('Mudando a idade')
    print(dados)
    dados['idade'] = 31
    print(dados)
    print('Adicionando Profissao')
    dados['profissao'] = 'Desenvolvedor'
    print(dados)
    del dados['cidade']
    print(dados)

def dicionario_quadrado():
    quadrado = {}
    for i in range(1,6):
        quadrado[i] = i ** 2
    print(quadrado)

def dicionario_verificar():
    pessoa = {'nome': 'Pedro',
              'idade': 30,
              'cidade': 'Porto Alegre'
    }
    if 'email' in pessoa:
        print("A chave 'email' existe no dicionario")
    else:
        print("A chave 'email' nao existe no dicionario")
        
def dicionario_frequencia():
    frase = 'O rato roeu a roupa do rei de roma e a rainha de raiva roeu o resto da roupa do rei'
    palavras = frase.split()
    frequencia = {}

    for palavra in palavras:
        if palavra in frequencia:
            frequencia[palavra] += 1
        else:
            frequencia[palavra] = 1
    
    print(frequencia)

def main():
    lista_exercicios()
    escolher_opcao()

if __name__ == '__main__':
    main()