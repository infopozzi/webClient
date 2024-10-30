from flask import Blueprint, render_template, jsonify, request, url_for, redirect, flash

turmas_blueprint = Blueprint("turma", __name__)

import requests

#url = f'{ app.config["HOST_API"]}:{app.config["PORT_API"]}
url = 'http://127.0.0.1:8080'

@turmas_blueprint.route("/", methods=["GET"])
def index():
    retorno = requests.get(f'{url}/turma/listar')
    return render_template("turma/index.html", turmas = retorno.json())

@turmas_blueprint.route("/obter/<int:id>", methods=["GET"])
def obter(id):
    retorno = requests.get(f'{url}/turma/obter/{id}')
    lista_professor = requests.get(f'{url}/professor/listar')
    return render_template("turma/cadastrar.html", turma = retorno.json(), professores = lista_professor.json())

@turmas_blueprint.route("/cadastrar", methods=["GET"])
def cadastrar():
    lista_professor = requests.get(f'{url}/professor/listar')

    payload = {"id": 0,
               "descricao": "",
               "professor_id": 0, 
               "ativo": True
              }
    
    return render_template("turma/cadastrar.html", turma = payload, professores = lista_professor.json())

@turmas_blueprint.route("/salvar", methods=["POST"])
def salvar():

    payload = {"id": int(request.form["id"]),
                "descricao": request.form["descricao"],
                "professor_id": int(request.form["professor_id"]), 
                "ativo": "ativo" in request.form
              }
    
    retorno = requests.post(f"{url}/turma/salvar", json = payload)

    if (retorno.status_code == 200):
        dados = retorno.json()
        flash(dados.get('message'), "success")
        return redirect("/turma/")
    else:
        flash("Não foi possível salvar", "alert")

@turmas_blueprint.route("/excluir", methods=["POST"])
def excluir():
    id = int(request.form["id"])

    payload = {"id": id }
    retorno = requests.post(f"{url}/turma/excluir", json = payload)

    if (retorno.status_code == 200):
        dados = retorno.json()
        flash(dados.get('message'), "success")
        return redirect("/turma/")
    else:
        flash("Não foi possível excluir", "alert")