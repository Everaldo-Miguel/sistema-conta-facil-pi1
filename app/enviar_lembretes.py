from app import db, mail
from flask_mail import Message
from app.models import User, Conta
from twilio.rest import Client
from datetime import date, timedelta
import os

def enviar_lembretes(app):
    with app.app_context():
        
        datas_vencimento = [date.today(), date.today() + timedelta(days=1)]

        contas = Conta.query.filter(Conta.vencimento.in_(datas_vencimento),Conta.lembrete == True).all()


        for conta in contas:
            user = User.query.get(conta.user_id)
            if not user.receber_lembretes:
                continue

            # Enviar email
            msg = Message(
                subject='🔔 Lembrete de Conta',
                sender=os.getenv('MAIL_USERNAME'),
                recipients=[user.email]
            )
            msg.body = f"""
Olá {user.nome},

Lembrete: sua conta "{conta.descricao}" no valor de R$ {conta.valor:.2f}
vence em {conta.vencimento.strftime('%D/%m/%Y')}.

Atenciosamente,
Sistema Conta Fácil
"""
            mail.send(msg)

            # Enviar WhatsApp
            if user.whatsapp:
                twilio_sid = os.getenv('TWILIO_ACCOUNT_SID')
                twilio_token = os.getenv('TWILIO_AUTH_TOKEN')
                twilio_phone = os.getenv('TWILIO_PHONE')

                client = Client(twilio_sid, twilio_token)
                client.messages.create(
                    body=f'Lembrete: sua conta "{conta.descricao}" vence em {conta.vencimento.strftime("%D/%m/%Y")}.',
                    from_=f'whatsapp:{twilio_phone}',
                    to=f'whatsapp:{user.whatsapp}'
                )