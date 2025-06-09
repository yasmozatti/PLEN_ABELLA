import operacoesbd

#Apresentação do menu
def menu():
    while True:
        print("\n=== Ouvidoria ===")
        print("1. Registrar mensagem")
        print("2. Listar mensagens")
        print("3. Excluir mensagem")
        print("4. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            registrar_mensagem()
        elif opcao == "2":
            listar_mensagens()
        elif opcao == "3":
            excluir_mensagem()
        elif opcao == "4":
            break
        else:
            print("Opção inválida.")

#Criacao da tabela no SQL
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
        cursor.close()

criarTabelaOuvidoria()

#Criação da conexão do banco de dados 
#Durante todo o código estaremos utilizando a biblioteca disponibilizada
conn = db.criarConexao("localhost", "root", "sua_senha", "nome_do_banco")

#Função para registrar uma ouvidoria
def registrar_mensagem():
    nome = input("Seu nome: ")
    categoria = input("Categoria (reclamação/sugestão/elogio): ").lower()
    mensagem = input("Digite sua mensagem: ")

    sql = "INSERT INTO ouvidoria (nome, categoria, mensagem) VALUES (%s, %s, %s)"
    dados = (nome, categoria, mensagem)

    id = db.insertNoBancoDados(conn, sql, dados)
    if id:
        print("Mensagem registrada com sucesso.")

#Executando o programa
menu()