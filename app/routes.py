from app import app
import secrets
from flask import render_template, request, redirect, session, flash

app.secret_key = secrets.token_hex(16)

@app.route('/')
def index():    
    if 'username' not in session:
        return redirect('/login')
    else:
        return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/login/submit', methods=['POST'])
def login_submit():
    username = request.form['username']
    password = request.form['password']

    if (username == 'admin' and password == 'Password123'):
        session['username'] = username
        return redirect('/')
    else:
        flash('Invalid username or password')
        return redirect('/login')
    
@app.route('/logout', methods=['POST'])
def logout():
    session.pop('username', None)
    return redirect('/')    

        
    