# APLICACAO OUVIDORIA
# A ouvidoria seguirá um modelo onde o seu índice será o id
# As manifestações são guardadas numa lista 'ouvidoria'
manifestacoes = []

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
        f'\n{green}[6]{clean} FINALIZAR E SAIR DO MENU'
        )
    pergunta = (input(f"{nome} DIGITE SUA ESCOLHA: "))
    print("-" * 100)
    
    if pergunta not in "123456":

        print(f'{red}ENTRADA INVÁLIDA. É PERMITIDO APENAS SELECIONAR ALGUMA OPÇÃO DO MENU!')
        
    elif pergunta == "1":
        
        if len(manifestacoes) == 0:
            print(f"{red}NÃO HÁ MANIFESTAÇÕES FEITAS{clean}")
        
        else:
            print(f"{red}MANIFESTAÇÕES FEITAS: {clean}")
            for i in range(len(manifestacoes)):
                print((i+1) , ' - ' , manifestacoes[i])
    
    elif pergunta == "2":
        
        texto_manifestacao = input(f"{nome}, ESCREVA SUA MANIFESTAÇÃO: ").upper()
        manifestacoes.append(texto_manifestacao)
        print(f"{green}MANIFESTAÇÃO ADICIONADA COM SUCESSO{clean}")

    
    elif pergunta == "3":

        if len(manifestacoes) == 0:
            print(f'{red}NÃO HÁ MANIFESTAÇÕES FEITAS{clean}!!!!!')
        else:
            print(f'QUANTIDADE DE MANIFESTAÇÕES: {magenta}{len(manifestacoes)}{clean}')
    
    elif pergunta == "4":
        
        while True:
            codigo_str = input('DIGITE O CÓDIGO (DÍGITO) DA MANIFESTAÇÃO: ')
            
            if codigo_str.isdigit():
                codigo = int(codigo_str)
                
                if 1 <= codigo <= len(manifestacoes):
                    print(manifestacoes[codigo - 1])
                    break

                elif len(manifestacoes) == 0:
                    print(f'{red}CÓDIGO INVÁLIDO! NÃO HÁ MANIFESTAÇÕES FEITAS. {clean}')
                    break
                
                else: 
                    print(f'{red}CÓDIGO INVÁLIDO, TENTE NOVAMENTE{clean}')
            
            else:
                print(f"{red}ENTRADA INVÁLIDA, INSIRA APENAS NÚMEROS INTEIROS POSITIVOS!{clean}")
    
    elif pergunta == "5":
        
        while True:
            eliminar = int(input("INSIRA O CÓDIGO DA MANIFESTAÇÃO QUE DESEJA ELIMINAR: "))
            
            if eliminar > len(manifestacoes) or eliminar <= 0:
                print(f'{red}CÓDIGO INVÁLIDO, TENTE NOVAMENTE!{clean}\nA LISTA POSSUI {len(manifestacoes)} MANIFESTAÇÕES.')

            else:
                print(f'A MANIFESTAÇÃO DE CÓDIGO {eliminar} É {magenta}{manifestacoes[eliminar - 1]}{magenta}')
                confirma = (input("DESEJA CONTINUAR? [SIM/NÃO](Se outra opção for inserida, a operação será cancelada): ")).lower()
                
                if confirma == "sim":
                    manifestacoes.pop(eliminar-1)
                    print(f"{green}MANIFESTAÇÃO ELIMINADA COM SUCESSO!{clean}")
                    break
                
                else:
                    print("OPERAÇÃO CANCELADA COM SUCESSO!!!")
                    break

    elif pergunta == "6":
        
        print('PROGRAMA FINALIZADO')
        print('AGRADECEMOS A PREFERÊNCIA')
        break
    
        






