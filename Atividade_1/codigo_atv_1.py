# APLICACAO OUVIDORIA
# A ouvidoria seguirá um modelo onde o seu índice será o id
# As manifestações são guardadas numa lista 'ouvidoria'
ouvidoria = []

# Pegamos o nome do usuário, apesar de não ter uso nas opções do menu do sistema
print("BEM VINDO À OUVIDORIA!")
print("PARA INICIAR SEU COMENTÁRIO, INFORME:")

red = '\033[1;31m'
yellow = '\033[1;33m'
cyan = '\033[1;36m'
green = '\033[1;32m'
clean = '\033[0;0m'
magenta = '\033[1;35m'
nome = input("NOME: ").upper()

while True:
    print("-" * 100)
    print(" " * 47 + "OPÇÕES" + " " * 47)
    print("-" * 100)
    print(
        f'{red}[1]{clean} LISTAR MANIFESTAÇÕES'
        f'\n{cyan}[2]{clean} ADICIONAR MANIFESTAÇÃO'
        f'\n{red}[3]{clean} EXIBIR QUANTIDADE DE MANIFESTAÇÕES'
        f'\n{magenta}[4]{clean} PROCURAR MANIFESTAÇÃO PELO CÓDIGO'
        f'\n{yellow}[5]{clean} REMOVER MANIFESTAÇÃO PELO CÓDIGO'
        f'\n{green}[6]{clean} FINALIZAR E SAIR DO MENU')
    pergunta = (input(f"{nome} DIGITE SUA ESCOLHA: "))
    print("-" * 100)
    
    if pergunta.isdigit():
        resposta = int(pergunta)
    else:
        print(f'{red}ENTRADA INVÁLIDA. É PERMITIDO APENAS SELECIONAR ALGUMA OPÇÃO DO MENU!')
        print(f'EXECUTE O PROGRAMA {red} NOVAMENTE. {clean}')
        break

    if resposta == 1:
        if len(ouvidoria) == 0:
            print(f"{red}NÃO HÁ MANIFESTAÇÕES FEITAS{clean}")
        else:
            print(f"{red}MANIFESTAÇÕES FEITAS: {clean}")
            for i in range(len(ouvidoria)):
                print((i+1) , ' - ' , ouvidoria[i])
    elif resposta == 2:
        texto_ouvidoria = input(f"{nome}, ESCREVA SUA MANIFESTAÇÃO: ").upper()
        ouvidoria.append(texto_ouvidoria)
        print(f"{green}MANIFESTAÇÃO ADICIONADA COM SUCESSO{clean}")
    elif resposta == 3:
        quantidade = 0
        for i in ouvidoria:
            quantidade +=1
        if quantidade == 0:
            print(f'{red}NÃO HÁ MANIFESTAÇÕES FEITAS{clean}!!!!!')
        else:
            print(f'QUANTIDADE DE MANIFESTAÇÕES: {magenta}{len(ouvidoria)}{clean}')
    elif resposta == 4:
        codigo_str = input('DIGITE O CÓDIGO (DÍGITO) DA MANIFESTAÇÃO: ')
        if codigo_str.isdigit():
            codigo = int(codigo_str)
            if 1 <= codigo <= len(ouvidoria):
                print(ouvidoria[codigo - 1])
            elif len(ouvidoria) == 0:
                print(f'{red}CÓDIGO INVÁLIDO! NÃO HÁ MANIFESTAÇÕES FEITAS. {clean}')
            else: 
                print(f'{red}CÓDIGO INVÁLIDO, TENTE NOVAMENTE{clean}')
        else:
            print(f"{red}ENTRADA INVÁLIDA, TENTE NOVAMENTE!{clean}")
    elif resposta == 5:
        eliminar = int(input("INSIRA O ÍNDICE DA MANIFESTAÇÃO QUE DESEJA ELIMINAR: "))
        if eliminar > len(ouvidoria) or eliminar <= 0:
            print(f'{red}INDICE INVÁLIDO, TENTE NOVAMENTE!{clean}')
        else:
            print(f'A MANIFESTAÇÃO DE ÍNDICE{eliminar} É {magenta}{ouvidoria[eliminar - 1]}{magenta}')
            confirma = (input("DESEJA CONTINUAR? [SIM/NÃO]: ")).lower()
            if confirma == "sim":
                ouvidoria.pop(eliminar-1)
                print(f"{green}MANIFESTAÇÃO ELIMINADA COM SUCESSO!{clean}")
            else:
                print("OPERAÇÃO CANCELADA COM SUCESSO!!!")

    elif resposta == 6:
        print('PROGRAMA FINALIZADO')
        print('AGRADECEMOS A PREFERÊNCIA')
        break
    else: 
        print(f'{red}VALOR INVÁLIDO, INSIRA APENAS OS VALORES LISTADOS NO MENU{clean}')






