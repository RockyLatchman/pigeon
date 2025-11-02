from flask import Flask, render_template, session, request
from dotenv import load_dotenv
from flask_wtf import CSRFProtect
from sqlmodel import Session, create_engine
import os

load_dotenv('.env')

app = Flask(__name__)
app.config['DATABASE_URL'] = os.environ.get('DATABASE_URL')
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
db_engine = create_engine(app.config['DATABASE_URL'], echo=True)
csrf_token = CSRFProtect(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    return render_template('register.html')

@app.route('/signout')
def signout():
    return render_template('signout.html')

@app.route('/inbox')
def inbox():
    return render_template('inbox.html')

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

@app.route('/tags/<color>')
def tag(color):
    pass

if __name__ == '__main__':
    app.run(debug=True)
