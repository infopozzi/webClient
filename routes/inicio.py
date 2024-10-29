from flask import Blueprint, render_template

inicio_blueprint = Blueprint("inicio", __name__)

@inicio_blueprint.route("/")
def index():
    return render_template("inicio.html")
