# APLICACAO OUVIDORIA
print("BEM VINDO À OUVIDORIA!")
print("PARA INICIAR SEU COMENTÁRIO, INFORME:")
nome = input("NOME: ")
while True:
    idade = input("IDADE: ")
    if idade.isdigit():
        idade = int(idade)
        break
    else:
        print("VOCÊ PODE INFORMAR APENAS UM NÚMERO INTEIRO. DIGITE NOVAMENTE.")
print("OPÇÕES: ")
print("1- AVALIAÇÃO")
print('2- SUGESTÃO')
print('3- RECLAMAÇÃO')
print('4- OUTROS')
resposta = input("DIGITE SUA ESCOLHA: ")

#DECLARANDO AS LISTAS DA OUVIDORIA
avaliacao = []
sugestao = []
reclamacao = []
outros = []

#ARMAZENANDO AS RESPOSTAS 
while True:
    if resposta == 1:
        estrelas = input("EM UMA ESCALA DE 1 A 5, COMO VOCÊ AVALIA O ATENDIMENTO? ")
        if estrelas.isdigit():
            avaliacao_opcional = input("GOSTARIA DE DEIXAR UMA AVALIAÇÃO ESCRITA? (1- S | 2- N) ").upper()
            if avaliacao_opcional == "N":
                avaliacao_escrita = input('DIGITE SUA AVALIAÇÃO: ')
                break
            else:
                avaliacao_escrita = '';
                break
        else:
            print('RESPOSTA INVÁLIDA, TENTE NOVAMENTE')
    elif resposta == 2:
        #DECIDI QUE QUANDO estrela FOR IGUAL A 0 É PORQUE NÃO HOUVE AVALIAÇÃO NUMÉRICA, ENTÃO DESCONSIDERAMOS NA MÉDIA FINAL DE ATENDIMENTO
        estrela = 0
        avaliacao_escrita = input('DIGITE SUA SUGESTÃO: ')
    elif resposta == 3:
        estrela = 1 #QUANDO O CLIENTE RECLAMA, O ATENDIMENTO É ENTENDIDO PELO SISTEMA COMO TOTALMENTE NEGATIVO
        avaliacao_escrita = input('DIGITE AQUI SUA RECLAMAÇÃO: ')
    elif resposta == 4:
        estrela = 0 #TAMBÉM ENTENDEMOS QUE NÃO HOUVE AVALIAÇÃO DO ATENDIMENTO E SIM OUTRAS TRATATIVAS DO SERVIÇO
        avaliacao_escrita = input('DIGITE SUA DÚVIDA: ')
        print('AVALIAREMOS SUA SOLICITAÇÃO E ENTRAREMOS EM CONTATO')



    
