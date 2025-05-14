from . import db
from flask_login import UserMixin
from datetime import datetime

# Modelagem do banco de dados dos usuários
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    whatsapp = db.Column(db.String(20))
    receber_lembretes = db.Column(db.Boolean, default=False)

# Modelagem do banco de dados das contas
class Conta(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tipo = db.Column(db.String(10)) 
    descricao = db.Column(db.String(150))
    valor = db.Column(db.Float)
    vencimento = db.Column(db.Date)
    lembrete = db.Column(db.Boolean, default=False)
    status = db.Column(db.String(10), default='Em aberto')
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    
