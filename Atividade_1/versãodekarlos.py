print("BEM VINDO À OUVIDORIA!")
print("PARA INICIAR SEU COMENTÁRIO, INFORME:")

red = '\033[1;31m'
yellow = '\033[1;33m'
cyan = '\033[1;36m'
clean = '\033[0;0m'
nome = input("NOME: ")
manifestacoes = []

#while True:
# idade = input("IDADE: ")
# if idade.isdigit():idade = int(idade
# break# else:print("VOCÊ PODE INFORMAR APENAS UM NÚMERO INTEIRO. DIGITE NOVAMENTE.")

while True:
    print("-" * 100)
    print(" " * 47 + "OPÇÕES" + " " * 47)
    print("-" * 100)
    print(
        f'{red}[1]{clean} Listar manifestações'
        f'\n{cyan}[2]{clean} Adicionar manifestão'
        f'\n{red}[3]{clean} Procurar manifestação pelo indice'
        f'\n{cyan}[4]{clean}Remover manifestação pelo indice'
        f'\n{yellow}[5]{clean}Exibir quantidade de manifestações'
        f'\n{yellow}[6]{clean}Sair e finalizar menu')
    resposta = int(input("DIGITE SUA ESCOLHA: "))
    print("-" * 100)

    if resposta < 0 or resposta > 6:
        print(f'{red}Valor inválido, insira apenas os valores listados no menu{clean}')

    elif resposta == 1:
        if len(manifestacoes) == 0:
            print(f"{red}A lista está vazia{clean}")
        else:
            for c in range(len(manifestacoes)):
                print(f'{c+1} - {manifestacoes[c]}')

    elif resposta == 2:
        manifestacao = input(f"{nome} Insira sua manifestação: ")
        manifestacoes.append(manifestacao)
        print(f'{cyan}Sua manifestação: ({manifestacao}) foi adicionada com sucesso!!!{clean}')

    elif resposta == 3:
        indice = int(input(f"{nome} Insira o indice da manifestação: "))
        print(f'A manifestação de {indice} é {manifestacoes[indice-1]}')

    elif resposta == 4:
            eliminar = int(input('Insira o indice da manifestação que deseja eliminar: '))
            print(f'A manifestação de indice {eliminar} é {manifestacoes[eliminar-1]}')
            confirma = (input('Deseja continuar? [S/N]')).lower()
            if confirma in 's':
                manifestacoes.pop(eliminar-1)
            else:
                print(f"Operação cancelada com sucesso!!!")

    elif resposta == 5:
        print(f'A quantidade de manifestações é {len(manifestacoes)}')

    elif resposta == 6:
        print('Programa finalizado')
        break
