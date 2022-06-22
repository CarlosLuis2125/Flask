import conexaoBD
import mysql.connector
import this
this.msg = ""
db_connection = conexaoBD.conexao()
con = db_connection.cursor()

def inserir(nome, telefone, endereco, dataDeNascimento):
    try:
        sql = "Insert into Pessoa(codigo , nome, telefone, endereco, dataDeNascimento) values('', '{}', '{}', '{}', '{}')".format(nome, telefone, endereco, dataDeNascimento)
        con.execute(sql)
        db_connection.commit()
        return con.rowcount,"Inserido"
    except Exception as erro:
        return erro

def consultar():
    try:
        sql = "select * from pessoa"
        con.execute(sql)

        this.msg = ""
        for (codigo, nome, telefone, endereco, dataDeNascimento) in con:
            this.msg = this.msg + "Código: {} Nome: {} Telefone: {} Endereço: {} Data de nasciento: {}".format(codigo, nome, telefone, endereco, dataDeNascimento)
        return this.msg
    except Exception as erro:
        return erro

def consultarPorCodigo(cod):
    try:
        sql = "select * from pessoa where codigo = '{}'".format(cod)
        con.execute(sql)

        this.msg = ""
        this.msg = "Nenhum dado encontrado!"
        for(codigo, nome, telefone, endereco, dataDeNascimento) in con:
            if int(codigo) == int(cod):
                this.msg = "Código: {} Nome: {} Telefone: {} Endereço: {} Data de nascimento: {}".format(codigo, nome, telefone, endereco, dataDeNascimento)
                return this.msg
        return this.msg
    except Exception as erro:
        return erro