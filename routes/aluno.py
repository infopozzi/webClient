from flask import Blueprint, render_template, jsonify, request, url_for, redirect, flash

alunos_blueprint = Blueprint("aluno", __name__)

import requests

#url = f'{ app.config["HOST_API"]}:{app.config["PORT_API"]}
url = 'http://127.0.0.1:8080'

@alunos_blueprint.route("/", methods=["GET"])
def index():
    retorno = requests.get(f'{url}/aluno/listar')
    return render_template("aluno/index.html", alunos = retorno.json())

@alunos_blueprint.route("/obter/<int:id>", methods=["GET"])
def obter(id):
    retorno = requests.get(f'{url}/aluno/obter/{id}')
    lista_turma = requests.get(f'{url}/turma/listar')
    return render_template("aluno/cadastrar.html", aluno = retorno.json(), turmas = lista_turma.json())


@alunos_blueprint.route("/cadastrar", methods=["GET"])
def cadastrar():
    lista_turma = requests.get(f'{url}/turma/listar')
    payload = {"id": 0, 
               "nome": "", 
               "idade": 0,
               "turma_id": 0,
               "data_nascimento": "",
               "nota_primeiro_semestre": "",
               "nota_segundo_semestre": ""
              } 
    
    return render_template("aluno/cadastrar.html", aluno = payload, turmas = lista_turma.json())

@alunos_blueprint.route("/salvar", methods=["POST"])
def salvar():
    payload = {"id": int(request.form["id"]), 
               "nome": request.form["nome"], 
               "turma_id": int(request.form["turma_id"]),
               "data_nascimento": request.form["data_nascimento"],
               "nota_primeiro_semestre": request.form["nota_primeiro_semestre"],
               "nota_segundo_semestre": request.form["nota_segundo_semestre"]
               }    
    retorno = requests.post(f"{url}/aluno/salvar", json = payload)

    if (retorno.status_code == 200):
        dados = retorno.json()
        flash(dados.get('message'), "success")
        return redirect("/aluno/")
    else:
        flash("Não foi possível salvar", "alert")

@alunos_blueprint.route("/excluir", methods=["POST"])
def excluir():
    id = int(request.form["id"])

    payload = {"id": id }
    retorno = requests.post(f"{url}/aluno/excluir", json = payload)

    if (retorno.status_code == 200):
        dados = retorno.json()
        flash(dados.get('message'), "success")
        return redirect("/aluno/")
    else:
        flash("Não foi possível excluir", "alert")