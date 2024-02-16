import mysql.connector as mc

# estabelecer a conexap com o banco
cx = mc.connect(
    host = "127.0.0.1",
    port = "3784",
    user = "root",
    password = "senac@123",
    database = "banco"
)

# verificar se a conexao foi estabelecida
print(cx)

# criação de variaveis para o usuario passar os dados do cliente para cadastrar

nome = input("digite o nome do cliente: ")
email = input("digite o email do cliente: ")
telefone = input("digite o telefone do cliente: ")

cursor = cx.cursor()
cursor.execute("insert into clientes(nome_cliente,email,telefone)values('"+nome+"','"+email+"','"+telefone+"')")

# confirmar a inserçao dos dados na tabela
print(cx.commit())