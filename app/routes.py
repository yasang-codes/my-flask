from app import app

@app.route('/')
def login():
    return "<b>Login Page</b>"