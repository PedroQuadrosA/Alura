import os

def lista_exercicios():
    print('########################')
    print('Escolha o numero do exercicio que queira ver.')
    print('1. Criação simples de classe')
    print('20. Finalizar app')
    print('0. Sair')
    print('########################')

def escolher_opcao():
    opcao_escolhida = int(input('\nEscolha uma opção: '))
    match opcao_escolhida:
        case 1:
            classe_simples()
        case _:
            print('Opção inválida')

def classe_simples():
    class Musica:
        nome = ''
        artista = ''
        duracao = ''
    
    rock = Musica()
    rock.artista = 'Iron Maiden'
    rock.nome = 'Fear of the dark'
    rock.duracao = '7:19'

    print(f'Música: {rock.nome} - Banda: {rock.artista} - {rock.duracao} de duração')

def finalizar_app():
    os.system('cls')
    print('Finalizando Sistema')

def main():
    lista_exercicios()
    escolher_opcao()

if __name__ == '__main__':
    main()