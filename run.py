from app import create_app
from app.enviar_lembretes import enviar_lembretes

app = create_app()
enviar_lembretes(app)

if __name__ == '__main__':
    app.run(debug=True)

