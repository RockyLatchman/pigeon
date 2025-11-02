from flask import Flask, render_template, session
from dotenv import load_dotenv
from flask_wtf import CSRFProtect
from sqlmodel import Session, create_engine

load_dotenv('.env')

app = Flask(__name__)
app.config['DATABASE_URL'] = os.environ.get('DATABASE_URL')
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
db_engine = create_engine(app.config['DATABASE_URL'], echo=True)

@app.route('/')
def index():
    pass

@app.route('/register')
def register():
    pass

@app.route('/signout')
def signout():
    pass

@app.route('/inbox')
def inbox():
    pass

@app.route('/contacts')
def contacts():
    pass

@app.route('/calendar')
def calendar():
    pass

@app.route('/storage')
def storage():
    pass

@app.route('/settings')
def settings():
    pass

if __name__ == '__main__':
    app.run(debug=True)
