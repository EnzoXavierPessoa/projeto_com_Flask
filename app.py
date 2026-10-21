from flask import Flask, request
from markupsafe import escape

app = Flask(__name__)

@app.route("/")
def ola_mundo():
    return '<p>Olá, mundo!</p>'

@app.route("/pessoa")
def ola_pessoa():
    nome = request.args.get("nome", "Flask")
    return f'<h1>Olá, {escape(nome)}</h1>'

@app.route("/usuario/<username>")
def home_usuario(username):
    return f'<p>Usuário: {escape(username)}</p>'

# Corrigido: adicionada a função para tratar a rota de boas-vindas
@app.route("/ola/")
@app.route("/ola/<nome>")
def ola_nome(nome="Visitante"):
    return f'<h1>Olá, {escape(nome)}!</h1>'

# Corrigido: apenas um bloco de inicialização
if __name__ == "__main__":
    # Ativa o modo debug e define a porta padrão 5000
    app.run(debug=True, port=5000)
