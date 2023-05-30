from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
app.secret_key = "my_secret_key"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///my_database.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    #Paulo: SQLite uses this as our connection to the Flask application
db = SQLAlchemy(app)
    #Paulo: binds your database to the application instance app

# ----- Gerenciando status de login ---------
login = LoginManager(app)
login.init_app(app)
    #PAULO: Instância de classe, gerencia acesso a páginas do site
login.login_view = 'login'
    #PAULO: redireciona não logados para a rota 'login' no routes.py.

import routes, models

