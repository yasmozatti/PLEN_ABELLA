print("BEM VINDO À OUVIDORIA!")
print("PARA INICIAR SEU COMENTÁRIO, INFORME:")

red = '\033[1;31m'
yellow = '\033[1;33m'
cyan = '\033[1;36m'
green = '\033[1;32m'
clean = '\033[0;0m'
magenta = '\033[1;35m'
nome = input("NOME: ").upper()
manifestacoes = []

while True:
    print("-" * 100)
    print(" " * 47 + "OPÇÕES" + " " * 47)
    print("-" * 100)
    print(
        f'{red}[1]{clean} LISTAR MANIFESTAÇÕES'
        f'\n{cyan}[2]{clean} ADICIONAR MANIFESTAÇÃO'
        f'\n{red}[3]{clean} PROCURAR MANIFESTAÇÃO PELO ÍNDICE'
        f'\n{magenta}[4]{clean} REMOVER MANIFESTAÇÃO PELO ÍNDICE'
        f'\n{yellow}[5]{clean} EXIBIR QUANTIDADE DE MANIFESTAÇÕES'
        f'\n{green}[6]{clean} FINALIZAR E SAIR DO MENU')
    resposta = int(input(f"{nome} DIGITE SUA ESCOLHA: "))
    print("-" * 100)

    if resposta < 0 or resposta > 6:
        print(f'{red}VALOR INVÁLIDO, INSIRA APENAS OS VALORES LISTADOS NO MENU{clean}')

    elif resposta == 1:
        if len(manifestacoes) == 0:
            print(f"{red}A LISTA ESTÁ VAZIA{clean}")
        else:
            for item in range(len(manifestacoes)):
                print(f'{item + 1} - {manifestacoes[item]}')

    elif resposta == 2:
        manifestacao = input(f"{nome} INSIRA SUA MANIFESTAÇÃO: ")
        manifestacoes.append(manifestacao)
        print(f'{green}SUA MANIFESTAÇÃO: {clean}({manifestacao}){green}  FOI ADICIONADA COM SUCESSO!!!{clean}')

    elif resposta == 3:
        if len(manifestacoes) == 0:
            print(f'{red}A LISTA ESTÁ VAZIA{clean}!!!!!')
        else:
            indice = int(input(f"{nome} INSIRA O INDICE DA MANIFESTAÇÃO: "))
            if indice-1 > len(manifestacoes) or indice < 0:
                print(f'A LISTA NÃO POSSUI ESSA MANIFESTAÇÃO')
            else:
                print(f'A MANIFESTAÇÃO DE ÍNDICE{indice} É {magenta}{manifestacoes[indice - 1]}{magenta}')

    elif resposta == 4:
        if len(manifestacoes) == 0:
            print(f'{red}A LISTA ESTÁ VAZIA{clean}!!!')

        else:
            eliminar = int(input('Insira o indice da manifestação que deseja eliminar: '))
            if eliminar > len(manifestacoes) or eliminar < 0:
                print('ESSE ÍNDICE NÃO EXISTE NA LISTA')
            else:
                print(f'A MANIFESTAÇÃO DE ÍNDICE {eliminar} É{manifestacoes[eliminar - 1]}')
                confirma = input('DESEJA CONTINUAR? [S/N]').lower()
                if confirma in 's':
                    manifestacoes.pop(eliminar - 1)
                else:
                    print(f"{green}OPERAÇÃO CANCELADA COM SUCESSO!!!{clean}")

    elif resposta == 5:
        print(f'A QUANTIDADE DE MANIFESTAÇÕES É {magenta}{len(manifestacoes)}{clean}')

    elif resposta == 6:
        print('PROGRAMA FINALIZADO')
        break
