from flask import Blueprint, render_template, jsonify, request, url_for, redirect, flash

professores_blueprint = Blueprint("professor", __name__)

import requests

#url = f'{ app.config["HOST_API"]}:{app.config["PORT_API"]}
url = 'http://127.0.0.1:8080'

@professores_blueprint.route("/", methods=["GET"])
def index():
    retorno = requests.get(f'{url}/professor/listar')
    return render_template("professor/index.html", professores = retorno.json())

@professores_blueprint.route("/obter/<int:id>", methods=["GET"])
def obter(id):
    retorno = requests.get(f'{url}/professor/obter/{id}')
    return render_template("professor/cadastrar.html", professor = retorno.json())


@professores_blueprint.route("/cadastrar", methods=["GET"])
def cadastrar():
    return render_template("professor/cadastrar.html", professor = { "id": 0, "nome": "", "endereco": ""})

@professores_blueprint.route("/salvar", methods=["POST"])
def salvar():
  
    payload = {"id": int(request.form["id"]), 
               "nome": request.form["nome"], 
               "idade":  int(request.form["idade"]),
               "materia": request.form["materia"],
               "observacao":request.form["observacao"]
              }
    
    retorno = requests.post(f"{url}/professor/salvar", json = payload)

    if (retorno.status_code == 200):
        dados = retorno.json()
        flash(dados.get('message'), "success")
        return redirect("/professor/")
    else:
        flash("Não foi possível salvar", "alert")

@professores_blueprint.route("/excluir", methods=["POST"])
def excluir():
    payload = {"id": int(request.form["id"]) }
    retorno = requests.post(f"{url}/professor/excluir", json = payload)

    if (retorno.status_code == 200):
        dados = retorno.json()
        flash(dados.get('message'), "success")
        return redirect("/professor/")
    else:
        flash("Não foi possível excluir", "alert")