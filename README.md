# Sistema Conta Fácil

O **Sistema Conta Fácil** é uma aplicação web para o gerenciamento simples e eficiente de contas a pagar e a receber. Desenvolvido em **Python Flask**, com **SQLite** para armazenamento de dados, o sistema inclui funcionalidades como cadastro de usuários, lembretes por e-mail e WhatsApp, e status de pagamento de contas. O deploy é feito no **Render**.

---

## 🎯 **Principais Funcionalidades**

* Cadastro e login de usuários
* Cadastro de contas a pagar e a receber
* Controle de status (paga ou em aberto)
* Lembretes por e-mail e WhatsApp
* Interface intuitiva e responsiva

---

## 📦 **Tecnologias Utilizadas**

* **Backend:** Python Flask, SQLAlchemy
* **Frontend:** HTML, CSS (Bootstrap 5)
* **Banco de Dados:** SQLite
* **Autenticação:** Flask-Login, Werkzeug
* **Deploy:** Render

---

## 🚀 **Instalação e Configuração**

1. Baixe o projeto
   
Acesse o repositório no GitHub:
https://github.com/Everaldo-Miguel/sistema-conta-facil

Clique no botão verde "Code" e selecione "Download ZIP".

Extraia o arquivo .zip em uma pasta de sua preferência.

No terminal, navegue até a pasta extraída:
```No terminal, digite
cd sistema-conta-facil-pi1
```

2. Crie e ative um ambiente virtual:

```No terminal, digite
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate  # Windows
```

3. Instale as dependências:

```No terminal, digite
pip install -r requirements.txt
```

4. Configure as variáveis de ambiente (`.env`):

```Crie um arquivo .env na raiz do projeto com o seguinte conteúdo
FLASK_APP=app
FLASK_ENV=development
SECRET_KEY=sua_chave_secreta
MAIL_USERNAME=seu_email@gmail.com
MAIL_PASSWORD=sua_senha_de_app
MAIL_DEFAULT_SENDER=seu_email@gmail.com
MAIL_SERVER=smtp.gmail.com
MAIL_PORT=587
MAIL_USE_TLS=True
```

5. Crie o banco de dados:

```No terminal, digite
python
>>> from app import create_app, db
>>> app = create_app()
>>> app.app_context().push()
>>> db.create_all()
>>> exit()
```

6. Inicie o servidor:

```No terminal, digite
flask run
```

No terminal será exibida uma mensagem como essa:
 * Running on http://127.0.0.1:5000.

 Copie o endereço e cole no navegador para acessar a aplicação.

---


## 📞 **Contato**

Para sugestões, melhorias ou contribuições, entre em contato pelo e-mail ** 23203471@aluno.univesp.br **.
