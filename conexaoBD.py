import mysql.connector
from mysql.connector import errorcode

def conexao():
    try:
        db_connection = mysql.connector.connect(host='localhost', user='root', password='', database='cadastroFlask')
        return db_connection
    except mysql.connector.Error as error:
        if error.errno == errorcode.ER_BAD_DB_ERROR:
            print('Banco de dados não existe!')
        elif error.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print('Nome de usuário ou senha estão errados!')
        else:
            print(error)
    else:
        db_connection.close()

