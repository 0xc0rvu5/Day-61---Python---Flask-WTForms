import os
from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, validators
from wtforms.validators import DataRequired, Email
from flask_bootstrap import Bootstrap


#initialize global variables
SECRET_KEY = os.urandom(32)
APP = Flask(__name__, template_folder='templates', static_folder='static')


#initialize relevant flask variables
APP.config['SECRET_KEY'] = SECRET_KEY
Bootstrap(APP)


class MyForm(FlaskForm):
    '''Password form used to validate correct login credentials.'''
    name = StringField('Email', validators=[validators.Length(min=6, max=35), validators.Email()])
    password = PasswordField('Password', validators=[validators.Length(min=10, max=60)])
    login = SubmitField('Log In', validators=[DataRequired()])


@APP.route("/")
def home():
    return render_template('index.html')


@APP.route("/login", methods=['GET', 'POST'])
def login():
    form = MyForm()
    #if user inputs the specified user credentials then send them to sucess.html else return them to login.html
    if form.validate_on_submit():
        if form.name.data == 'awesome@awesome.com' and form.password.data == 'supersecretpassword':
            return render_template('/success.html')
        else:
            return render_template('denied.html')

    return render_template('login.html', form=form)


if __name__ == '__main__':
    APP.run(debug=True)


#to start run
#export FLASK_APP=name_of_flask_file
#flask run