from flask import Blueprint,render_template,jsonify, request, redirect

login_blueprint = Blueprint("login", __name__)

@login_blueprint.route("/", methods=["GET",])
def login():
    return render_template("login.html")

@login_blueprint.route("/logar", methods=["POST",])
def logar():
    usuario = request.form["usuario"]
    senha = request.form["senha"]
    return redirect("/inicio/")

@login_blueprint.route("/sair", methods=["GET",])
def sair():
    return redirect("/")