# APLICACAO OUVIDORIA
# A ouvidoria seguirá um modelo onde o seu índice será o id
ouvidoria = []

red = '\033[1;31m'
yellow = '\033[1;33m'
cyan = '\033[1;36m'
clean = '\033[0;0m'

while True:
    # INICAREMOS COM A VISUALIZACAO DO MENU
    print("\n")
    print("-" * 100)
    print(" " * 47 + "OPÇÕES" + " " * 47)
    print("-" * 100)
    print(
        f'{red}[1]{clean} Listar manifestações'
        f'\n{cyan}[2]{clean} Adicionar manifestão'
        f'\n{red}[3]{clean} Procurar manifestação pelo indice'
        f'\n{cyan}[4]{clean}Remover manifestação pelo indice'
        f'\n{yellow}[5]{clean}Exibir quantidade de manifestações'
        f'\n{yellow}[6]{clean}Sair e finalizar menu').upper()

    pergunta = input('ESCOLHA: ')
    resposta = int(pergunta)

    if resposta == 1:
        if len(ouvidoria) == 0:
            print("NÃO HÁ MANIFESTAÇÕES FEITAS")
        else:
            print("MANIFESTAÇÕES FEITAS:")
            for i in range(len(ouvidoria)):
                print((i+1) , ' - ' , ouvidoria[i])
    elif resposta == 2:
        texto_ouvidoria = input("ESCREVA SUA MANIFESTAÇÃO: ").upper()
        ouvidoria.append(texto_ouvidoria)
        print("MANIFESTAÇÃO ADICIONADA COM SUCESSO")
    elif resposta == 3:
        quantidade = 0
        for i in ouvidoria:
            quantidade +=1
        print('QUANTIDADE DE MANIFESTAÇÕES: ' , quantidade)
    elif resposta == 4:
        while True:
            codigo_str = input('DIGITE O CÓDIGO (DÍGITO) DA MANIFESTAÇÃO: ')
            if codigo_str.isdigit():
                codigo = int(codigo_str)
                if 1 <= codigo <= len(ouvidoria):
                    print(ouvidoria[codigo - 1])
                    break
                else: 
                    print('CÓDIGO INVÁLIDO, TENTE NOVAMENTE')
            else:
                print("ENTRADA INVÁLIDA, TENTE NOVAMENTE!")
    elif resposta == 5:
        eliminar = int(input("INSIRA O ÍNDICE DA MANIFESTAÇÃO QUE DESEJA ELIMINAR: "))
        if eliminar > len(ouvidoria) or eliminar <= 0:
            print('INDICE INVÁLIDO, TENTE NOVAMENTE!')
        else:
            print('A MANIFESTAÇÃO DO ÍNDICE É: ' , ouvidoria[eliminar-1])
            confirma = (input("DESEJA CONTINUAR? [SIM/NÃO]: ")).lower()
            if confirma == "sim":
                ouvidoria.pop(eliminar-1)
                print("MANIFESTAÇÃO ELIMINADA COM SUCESSO!")
            else:
                print("OPERAÇÃO CANCELADA COM SUCESSO!!!")

    elif resposta == 6:
        print('PROGRAMA FINALIZADO')
        print('AGRADECEMOS A PREFERÊNCIA')
        break
    else: 
        print("RESPOSTA INVALIDA, TENTE NOVAMENTE!")






