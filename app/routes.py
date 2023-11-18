from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm, RegistrationForm

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title='Home')

@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # Here you would typically check if the user exists and the password is correct.
        # This is a simplified example.
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('home'))
    return render_template('login.html', title='Sign In', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        # Here you would typically add the user to the database.
        # This is a simplified example.
        flash('Registration successful for user {}'.format(form.username.data))
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)
