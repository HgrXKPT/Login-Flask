from flask import Flask, request,render_template,redirect,url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user
from werkzeug.security import generate_password_hash, check_password_hash





app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///atividade1.sqlite3"
app.config['SECRET_KEY'] = 'secret'

login_manager = LoginManager(app)
db = SQLAlchemy(app)


@login_manager.user_loader
def get_user(user_id):
    return Curso.query.filter_by(id=user_id).first()

class Curso(db.Model,UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(70),unique=True)
    nome = db.Column(db.String(70))
    senha = db.Column(db.String(70))

    def __init__(self,email,nome,senha):
        self.email = email
        self.nome = nome
        self.senha = generate_password_hash(senha)

    def verify_password(self, senha):
        return check_password_hash(self.senha, senha)
    
class Problemas(db.Model,UserMixin):
    __tablename__ = 'registros'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(70))
    problema = db.Column(db.String(2000))

    def __init__(self,problema,nome):
        self.problema = problema
        self.nome = nome

    




@app.route('/', methods=["POST","GET"])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password= request.form['password']

        user = Curso.query.filter_by(email=email).first()

        if not user or not user.verify_password(password):
            return render_template('login.html')  

        login_user(user)
        return redirect(url_for('home'))

    return render_template('login.html')

@app.route('/registro', methods=["POST", "GET"])
def registro():
    if request.method == "POST":
        email = request.form['email']
        nome = request.form['nome']
        senha = request.form['password']
        usuario = Curso(email,nome,senha)
        with app.app_context():
            db.create_all()
            db.session.add(usuario)
            db.session.commit()
            return render_template('login.html')

    return render_template('register.html')


@app.route('/home', methods=["POST","GET"])
def home():
    if request.method == "POST":
        nome = request.form['nome']
        text = request.form.get('text')
        problema = Problemas(text,nome)
        with app.app_context():
            db.create_all()
            db.session.add(problema)
            db.session.commit()
    return render_template('home.html')

if __name__ == "__main__":
    app.run(debug=True)