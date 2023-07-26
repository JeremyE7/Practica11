from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:root@db/mydatabase'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)

    def __init__(self, username):
        self.username = username


@app.route('/')
def index():
    users = User.query.all()
    return render_template('index.html', users=users)

@app.route('/crear/<username>')
def crear_usuario(username):
    user = User(username=username)
    db.session.add(user)
    db.session.commit()
    return f"Usuario {username} creado exitosamente."

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Crea la base de datos y las tablas
    app.run()

