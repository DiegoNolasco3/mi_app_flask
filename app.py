from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:password@localhost/mi_flask_app'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

#from app import app, db
from models import conectar_db
conectar_db(db)

with app.app_context():
    db.create_all()

from flask import render_template, redirect, url_for

@app.route('/add_user/<nombre>/<email>')
def add_user(nombre, email):
    #usuario = Usuario(nombre=nombre, email=email)
    #db.session.add(usuario)
    #db.session.commit()
    return redirect(url_for('usuarios'))

@app.route('/usuarios')
def usuarios():
    #usuarios = Usuario.query.all()
    return render_template('usuarios.html', usuarios=usuarios)

app.run(port=5050 , debug=True)

