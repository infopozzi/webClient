import os
from flask import Flask

app = Flask(__name__)

app.config['HOST'] = '0.0.0.0'
app.config['PORT'] = 5000
app.config['DEBUG'] = True

app.config['HOST_API'] = '0.0.0.0'
app.config['PORT_API'] = 8080
