from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Email, Length, EqualTo
from wtforms import FloatField, DateField, SelectField

# Criação do formulário de login
class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Senha', validators=[DataRequired()])
    remember = BooleanField('Lembrar de mim')
    submit = SubmitField('Entrar')

# Criação do formulário de cadastro
class RegisterForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Senha', validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField('Confirmar Senha', validators=[DataRequired(), EqualTo('password')])
    whatsapp = StringField('WhatsApp (com DDD)', validators=[DataRequired(), Length(min=10, max=20)])
    submit = SubmitField('Cadastrar')

# Criação do formulário de contas
class ContaForm(FlaskForm):
    descricao = StringField('Descrição', validators=[DataRequired()])
    valor = FloatField('Valor (R$)', validators=[DataRequired()])
    vencimento = DateField('Data de Vencimento', validators=[DataRequired()], format='%Y-%m-%d')
    lembrete = BooleanField('Desejo receber lembrete desta conta')
    status = SelectField('Status da conta', choices=[('Em Aberto', 'Em Aberto'), ('Paga', 'Paga')])
    submit = SubmitField('Salvar')