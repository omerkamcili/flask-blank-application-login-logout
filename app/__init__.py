from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = '4r368wfw2ef7qi3'
app.config.from_object('config')

db = SQLAlchemy(app)

from app.controllers.default import module as default
from app.controllers.auth import module as auth

app.register_blueprint(default)
app.register_blueprint(auth)

if __name__ == '__main__':
    app.run()