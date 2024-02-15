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