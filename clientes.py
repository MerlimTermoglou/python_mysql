# Importando a biblioteca de conexão com o banco de dados mysql
# Vamos adicionar um alias a biblioteca
import mysql.connector as mc
 
# Vamos estabelecer a conexão com o banco de dados e para tal, iremos passar os seguintes dados:
# servidor, porta, usuário, senha, banco

conexao = mc.connect(
    host = "127.0.0.1",
    port = "3784",
    user = "root",
    password = "senac@123",
    database = "banco"
)

print(conexao)

# para se movimentar dentro da estrutura de banco de dados e retornar dos dados necessários, iremos criar um cursor

cursor = conexao.cursor()

# Executar um comando usando o cursor
# cursor.execute("create database OLA")

cursor.execute("insert into clientes(nome_cliente,email,telefone)values('Amanda','mands@gmail.com','(54)99886-3425)")

# Vamos selecionar todos dados da tabela clietes
cursor.execute("Select * from banco.cliente")

print(cursor)

for c in cursor:
    print(f"Id do Cliente: {c[0]}")
    print(f"nome do Cliente: {c[1]}")
    print(f"E-mail: {c[2]}")