from flask import Flask, jsonify, request
from random import randint

app = Flask(__name__)

livros = [
    {
        'id': 1,
        'titulo': 'O Senhor dos Anéis - A Sociedade do Anel',
        'autor': 'J.R.R Tolkien'
    },
    {
        'id': 2,
        'titulo': 'Harry Potter e a Pedra Filosofal',
        'autor': 'J.K Howling'
    },
    {
        'id': 3,
        'titulo': 'James Clear',
        'autor': 'Hábitos Atômicos'
    },
]

# A forma dicionario ja retorna em formato json


@app.route('/livros', methods=['GET'])
# Consultar
def obter_livros():
    return livros


@app.route('/livros/<int:id>', methods=['GET'])
# Consultar por id
def obter_livro_por_id(id):
    for livro in livros:
        if livro.get('id') == id:
            return livro

    result = {"error": "Livro nao encontrado"}
    return result, 400
# https://stackoverflow.com/a/54361534


@app.route('/livros/<int:id>', methods=['PUT'])
# Alterar
def editar_livro_por_id(id):
    livro_alterado = request.get_json()

    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            livros[indice].update(livro_alterado)
            return livros[indice]

    result = {"error": "Livro nao encontrado"}
    return result, 400


@app.route('/livros', methods=['POST'])
# Criar
def incluir_novo_livro():
    novo_livro = request.get_json()
    # livros.append({
    #     'id': randint(4, 10),
    #     'titulo': novo_livro['titulo'],
    #     'autor': novo_livro['autor']
    # })
    # ou
    novo_livro['id'] = randint(4, 10)
    livros.append(novo_livro)

    return {}, 201


@app.route('/livros/<int:id>', methods=['DELETE'])
# Deletar
def deletar_livro_por_id(id):

    for livro in livros:
        if livro.get('id') == id:
            livros.remove(livro)
            return {}, 204

    result = {"error": "Livro nao encontrado"}
    return result, 400


app.run(port=5000, host='localhost', debug=True)
