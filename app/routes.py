from flask import Blueprint, render_template, redirect, url_for, flash, request
from .forms import LoginForm, RegisterForm
from .models import User
from . import db, login_manager
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash

main = Blueprint('main', __name__)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@main.route('/')
def index():
    return redirect(url_for('main.login'))

@main.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            return redirect(url_for('main.dashboard'))
        else:
            flash('Email ou senha incorretos.', 'danger')
    return render_template('login.html', form=form)

@main.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        existing_user = User.query.filter_by(email=form.email.data).first()
        if existing_user:
            flash('Email já cadastrado.', 'warning')
            return redirect(url_for('main.register'))
        hashed_password = generate_password_hash(form.password.data, method='pbkdf2:sha256')

        new_user = User(email=form.email.data, password=hashed_password, whatsapp=form.whatsapp.data)
        db.session.add(new_user)
        db.session.commit()
        flash('Conta criada com sucesso! Faça login.', 'success')
        return redirect(url_for('main.login'))
    return render_template('register.html', form=form)

@main.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.login'))

@main.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html')

from .models import Conta
from datetime import date

@main.route('/contas/<tipo>')
@login_required
def contas(tipo):
    if tipo not in ['pagar', 'receber']:
        return redirect(url_for('main.dashboard'))
    contas = Conta.query.filter_by(user_id=current_user.id, tipo=tipo).order_by(Conta.vencimento).all()
    return render_template('contas.html', contas=contas, tipo=tipo, today=date.today())

from .forms import ContaForm

@main.route('/contas/<tipo>/nova', methods=['GET', 'POST'])
@login_required
def nova_conta(tipo):
    if tipo not in ['pagar', 'receber']:
        return redirect(url_for('main.dashboard'))
    form = ContaForm()
    if form.validate_on_submit():
        nova = Conta(
            tipo=tipo,
            descricao=form.descricao.data,
            valor=form.valor.data,
            vencimento=form.vencimento.data,
            lembrete= form.lembrete.data,
            status=form.status.data,
            user_id=current_user.id
        )
        db.session.add(nova)
        db.session.commit()
        flash(f'Conta a {tipo} cadastrada com sucesso!', 'success')
        return redirect(url_for('main.contas', tipo=tipo))
    return render_template('nova_conta.html', form=form, tipo=tipo)

@main.route('/contas/<tipo>/editar/<int:conta_id>', methods=['GET', 'POST'])
@login_required
def editar_conta(tipo, conta_id):
    conta = Conta.query.filter_by(id=conta_id, user_id=current_user.id, tipo=tipo).first_or_404()
    form = ContaForm(obj=conta)
    
    if form.validate_on_submit():
        conta.descricao = form.descricao.data
        conta.valor = form.valor.data
        conta.vencimento = form.vencimento.data
        conta.lembrete = form.lembrete.data
        conta.status = form.status.data

        db.session.commit()
        flash('Conta atualizada com sucesso.', 'success')
        return redirect(url_for('main.contas', tipo=tipo))

    return render_template('editar_conta.html', form=form, tipo=tipo, conta=conta)

from flask import jsonify
from datetime import date

@main.route('/contas/atualizar_status/<int:conta_id>', methods=['POST'])
@login_required
def atualizar_status(conta_id):
    conta = Conta.query.filter_by(id=conta_id, user_id=current_user.id).first_or_404()
    novo_status = request.json.get('status')
    
    if novo_status not in ['Em Aberto', 'Paga']:
        return jsonify({'error': 'Status inválido'}), 400

    conta.status = novo_status
    db.session.commit()

    vencida = conta.vencimento < date.today() and conta.status != 'Paga'

