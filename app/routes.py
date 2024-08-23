from app import app
import secrets
from flask import render_template, request, redirect, flash
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from app.classes.user import USERS, Anonymous, USER_NAMES

app.secret_key = secrets.token_hex(16)

login_manager = LoginManager()

login_manager.anonymous_user = Anonymous

@login_manager.user_loader
def load_user(id):
    return USERS.get(int(id))

login_manager.setup_app(app)

@app.route('/')
def index():    
    if current_user.is_authenticated:
        return render_template('index.html')
    else:
        return redirect('/login')
        

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/login/submit', methods=['POST'])
def login_submit():
    username = request.form['username']
    password = request.form['password']
    remember = request.form.get('remember')
    
    if (username in USER_NAMES and password == 'Password123'):
        if(login_user(USER_NAMES[username], remember == 'on')):            
            flash(username)
            return redirect('/')
        else:
            flash('Login failed. Please contact the administrator.')
            return redirect('/login')
    elif (username in USER_NAMES and password != 'Password123'):
        flash('Username and password do not match. Please try again.')
        return redirect('/login')
    else:
        flash('Username does not exist. Please sign up and try again.')
        return redirect('/login')
    
@app.route('/logout', methods=['POST'])
@login_required
def logout():
    logout_user()
    flash('You have been logged out.')
    return redirect('/')    

        
    