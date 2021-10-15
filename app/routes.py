from app import app, db
from flask import render_template
from app.forms import UserInfoForm
from app.models import User


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=["GET", 'POST'])
def register():
    register_form = UserInfoForm()  
    if register_form.validate_on_submit():
        username = register_form.username.data
        email = register_form.email.data
        password = register_form.password.data
        print(username, email, password)

        new_user = User(username, email, password)
        db.session.add(new_user)
        db.session.commit()
    return render_template('register.html', form=register_form)
