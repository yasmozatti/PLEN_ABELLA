import operacoesbd as db

#Apresentação do menu
def menu():
    while True:
        print("\n=== Ouvidoria ===")
        print("1. Registrar mensagem")
        print("2. Listar mensagens")
        print("3. Listar mensagens por categoria")
        print("4. Excluir mensagem")
        print("5. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            registrar_mensagem()
        elif opcao == "2":
            listar_mensagens()
        elif opcao == "3":
            listar_mensagens_categoria()
        elif opcao == "4":
            excluir_mensagem()
        elif opcao == "5":
            break
        else:
            print("Opção inválida.")

# Criação da conexão do banco de dados 
conn = db.criarConexao("localhost", "root", "", "ouvidoria")

# Criacao da tabela no SQL
def criarTabelaOuvidoria():
    sql = """
    CREATE TABLE IF NOT EXISTS ouvidoria (
        id INT AUTO_INCREMENT PRIMARY KEY,
        nome VARCHAR(100),
        categoria ENUM('reclamação', 'sugestão', 'elogio'),
        mensagem TEXT
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

#Função para registrar uma ouvidoria
def registrar_mensagem():
    nome = input("Digite seu nome: ")
    categoria = input("Categoria (reclamação/sugestão/elogio): ").lower()
    mensagem = input("Digite sua mensagem: ")

    sql = "INSERT INTO ouvidoria (nome, categoria, mensagem) VALUES (%s, %s, %s)"
    dados = (nome, categoria, mensagem)

    id = db.insertNoBancoDados(conn, sql, dados)
    if id:
        print("Mensagem registrada com sucesso.")

# Função para listar as mensagens da ouvidoria
def listar_mensagens():
    sql = "SELECT id, nome, categoria, mensagem FROM ouvidoria"
    resultados = db.listarBancoDados(conn, sql)
    for ouvidoria in resultados:
        print(f"ID: {ouvidoria[0]}, \nNOME: {ouvidoria[1]} \nCATEGORIA: {ouvidoria[2]}, \nMENSAGEM: {ouvidoria[3]}")

#Função para listar as mensagens por categoria
def listar_mensagens_categoria():
    categoria_ouvidoria = input("Informa a categoria")
    sql = f"SELECT id, nome, categoria, mensagem FROM ouvidoria WHERE categoria = '{categoria_ouvidoria}'"
    resultados = db.listarBancoDados(conn, sql)
    for ouvidoria in resultados:
        print(f"ID: {ouvidoria[0]}, \nNOME: {ouvidoria[1]} \nCATEGORIA: {ouvidoria[2]}, \nMENSAGEM: {ouvidoria[3]}")

#Função para excluir alguma ouvidoria
def excluir_mensagem():
    print("Implementar")

#Função para alterar a mensagem enviada na ouvidoria
def alterar_mensagem():
    print("Implementar")

#Executando o programa
menu()