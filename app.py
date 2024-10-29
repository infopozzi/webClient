from config import app
from flask import render_template
from routes.login import login_blueprint
from routes.inicio import inicio_blueprint
from routes.aluno import alunos_blueprint
from routes.turma import turmas_blueprint
from routes.professor import professores_blueprint

app.register_blueprint(login_blueprint, url_prefix="/login")
app.register_blueprint(inicio_blueprint, url_prefix="/inicio")
app.register_blueprint(alunos_blueprint, url_prefix="/aluno")
app.register_blueprint(turmas_blueprint, url_prefix="/turma")
app.register_blueprint(professores_blueprint, url_prefix="/professor")

app.secret_key = "@aula@api"

@app.route("/", methods=["GET",])
def index():
    return render_template("index.html")

if __name__ == '__main__':
  app.run(host=app.config["HOST"], port = app.config['PORT'],debug=app.config['DEBUG'] )