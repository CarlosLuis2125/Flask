from flask import Flask, render_template, request
import this
import operacoes
this.codigo = ""
this.nome = ""
this.telefone = ""
this.endereco = ""
this.data = 0
this.dados = ""
this.mensagem = ""

pessoa = Flask(__name__) #representando uma váriavel do tipo flask

@pessoa.route('/', methods=['GET', 'POST']) #pode deixar o link só com a barra para o index
def cadastrar():
    if request.method == 'POST':
        this.nome     = request.form['tNovoNome']
        this.telefone = request.form['tNovoTelefone']
        this.endereco = request.form['tNovoEndereco']
        this.data     = request.form['tNovaData']
        this.dados    = operacoes.inserir(this.nome, this.telefone, this.endereco, this.data)
    return render_template('index.html', titulo='Página principal', resultado=this.dados) #se nao existe o templates nao da pra execultar o render_template

@pessoa.route('/consultar.html', methods=['GET', 'POST'])
def consul():
    if request.method == 'POST':
        this.mensagem = operacoes.consultar()
    return render_template('consultar.html', titulo='Consultar', resultado=this.mensagem)

@pessoa.route('/consultarCodigo.html', methods=['GET', 'POST'])
def consulCod():
    if request.method == 'POST':
        this.codigo = request.form['tCodigo']
        this.mensagem = operacoes.consultarPorCodigo(this.codigo)
    return render_template('consultarCodigo.html', titulo='Consultar por Código', consultar=this.mensagem)

if __name__ == '__main__':
    pessoa.run(debug=True, port=5000)