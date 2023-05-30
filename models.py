from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from app import db, login 
    #PAULO: 'db' e 'login' são objetos tipo instância de classe criados em app.py
    #PAULO> 'login' será usado para criar método que carrega o usuário na memória em cada página vistada.
from flask_login import UserMixin

@login.user_loader
def load_user(id):
    return User.query.get(int(id))
    #PAULO: 'login' é a instância de classe criada em app.py. Nome aleatório. Essencial para navegar pelas páginas com um usuário logado.

class User(db.Model, UserMixin):
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(64), index=True, unique=True)
  email = db.Column(db.String(120), unique = True, index = True)
  password = db.Column(db.String(128))
  password_hash = db.Column(db.String(128))
  posts = db.relationship('Post', backref='author', lazy='dynamic')

  def set_password(self,password):
      self.password_hash = generate_password_hash(password)
      #PAULO: função geradora de senha hash a partir do password
  
  def check_password(self, password):
      return check_password_hash(self.password_hash, password)
      #PAULO: retorna Booleano True ou False
  
  def __repr__(self):
        return '<User {}>'.format(self.username)


class Post():
    id = db.Column(db.Integer, primary_key=True)
    city = db.Column(db.String(140))
    country = db.Column(db.String(140))
    description = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post {}>'.format(self.description)
