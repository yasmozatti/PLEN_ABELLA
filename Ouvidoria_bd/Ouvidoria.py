import operacoesbd as db

red = '\033[1;31m'
yellow = '\033[1;33m'
cyan = '\033[1;36m'
green = '\033[1;32m'
clean = '\033[0;0m'
magenta = '\033[1;35m'
# Criação da conexão do banco de dados 
conn = db.criarConexao("localhost", "root", "", "ouvidoria")

def criarTabelaOuvidoria():
    sql = """
    CREATE TABLE IF NOT EXISTS ouvidoria (
        id INT AUTO_INCREMENT PRIMARY KEY,
        nome VARCHAR(100),
        categoria ENUM('reclamação', 'sugestão', 'elogio'),
        manifestação TEXT
    );
    """
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()
    except Exception as e:
        print(f"Erro ao criar tabela: {e}")
    finally:
        if 'cursor' in locals():
            cursor.close()

criarTabelaOuvidoria()
#Apresentação do menu
print("BEM VINDO À OUVIDORIA!" 
"\nPARA INICIAR SEU COMENTÁRIO, INFORME:")

def menu():
   while True:
        print("-" * 100)
        print(" " * 47 + "OPÇÕES" + " " * 47)
        print("-" * 100)
        print(
            f'{red}[1]{clean} LISTAR MANIFESTAÇÕES'
            f'\n{cyan}[2]{clean} LISTAR MANIFESTAÇÕES POR CATEGORIA'
            f'\n{magenta}[3]{clean} ADICIONAR MANIFESTAÇÃO'
            f'\n{red}[4]{clean} EXIBIR QUANTIDADE DE MANIFESTAÇÕES'
            f'\n{magenta}[5]{clean} PROCURAR MANIFESTAÇÃO PELO CÓDIGO'
            f'\n{yellow}[6]{clean} REMOVER MANIFESTAÇÃO PELO CÓDIGO'
            f'\n{green}[7]{clean} FINALIZAR E SAIR DO MENU'
            )
        opcao = (input(f"DIGITE SUA ESCOLHA: "))
        print("-" * 100)

        if opcao not in "1234567":

            print(f'{red}ENTRADA INVÁLIDA. É PERMITIDO APENAS SELECIONAR ALGUMA OPÇÃO DO MENU!')

        elif opcao == "1":
            listar_todas_manifestacoes()

        elif opcao == "2":
            listar_manifestacoes_tipo()

        elif opcao == "3":
            adicionar_manifestacao()

        elif opcao == "4":
            exibir_quantidade_manifestacoes()

        elif opcao == "5":
            procurar_manifestacao()

        elif opcao == "6":
            remover_manifestacao()
            
        elif opcao == "7":
            print("Saindo do menu...")
            break



# Criacao da tabela no SQL


#Função para registrar uma ouvidoria
def adicionar_manifestacao():
    nome = input("Digite seu nome: ")
    categoria = input("Categoria (reclamação/sugestão/elogio): ").lower()
    mensagem = input("Digite sua manifestação: ")

    sql = "INSERT INTO ouvidoria (nome, categoria, manifestação) VALUES (%s, %s, %s)"
    dados = (nome, categoria, mensagem)

    id = db.insertNoBancoDados(conn, sql, dados)
    if id:
        print("Manifestação registrada com sucesso.")

# Função para listar as mensagens da ouvidoria
def listar_todas_manifestacoes():
    sql = "SELECT id, nome, categoria, manifestação FROM ouvidoria"
    resultados = db.listarBancoDados(conn, sql)
    for ouvidoria in resultados:
        print(f"ID: {ouvidoria[0]}, \nNOME: {ouvidoria[1]} \nCATEGORIA: {ouvidoria[2]}, \nMANIFESTAÇÃO: {ouvidoria[3]}")

#Função para listar as mensagens por categoria
def listar_manifestacoes_tipo():
    categoria_ouvidoria = input("Informa a categoria")
    sql = f"SELECT id, nome, categoria, manifestação FROM ouvidoria WHERE categoria = '{categoria_ouvidoria}'"
    resultados = db.listarBancoDados(conn, sql)
    for ouvidoria in resultados:
        print(f"ID: {ouvidoria[0]}, \nNOME: {ouvidoria[1]} \nCATEGORIA: {ouvidoria[2]}, \nMANIFESTAÇÃO: {ouvidoria[3]}")

#Função para excluir alguma ouvidoria
def remover_manifestacao():
    print("Implementar")

#Função para procurar uma manifestacao por códigona 
def procurar_manifestacao():
    print("Implementar")

#Executando o programa
menu()