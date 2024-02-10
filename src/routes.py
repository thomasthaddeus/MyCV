"""routes.py

This module defines the routes for a web application using Flask. It includes
routes for home, about, login, registration, and user-related API endpoints.

The routes are responsible for handling web requests and returning appropriate
responses or web pages. The module uses forms for user interaction and
leverages the User model for database interactions.

Returns:
    HTML templates or JSON responses: Depending on the route, this module
      returns rendered HTML templates for web pages or JSON responses for API
      requests.
"""

from flask import render_template, flash, redirect, url_for, jsonify, request
from werkzeug.security import generate_password_hash, check_password_hash
from app import app
from app import LoginForm, RegistrationForm, User, Profile


@app.route('/')
@app.route('/home')
def home():
    """
    Render the home page of the web application.

    This route serves the main page of the site and is typically the first page users interact with.

    Returns:
        render_template: Renders and returns the 'home.html' template with 'Home' as the title.
    """
    return render_template('home.html', title='Home')

@app.route('/about')
def about():
    """
    Render the about page of the web application.

    Provides information about the web application, its purpose, and other relevant details.

    Returns:
        render_template: Renders and returns the 'about.html' template with 'About' as the title.
    """
    return render_template('about.html', title='About')

@app.route('/login', methods=['GET', 'POST'])
def login():
    """
    Handle user login.

    This route manages both displaying the login form (GET request) and
    processing the login data (POST request). It authenticates users based on their credentials.

    Returns:
        render_template or redirect: Renders the login form or redirects to the
        home page upon successful login.
    """
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and check_password_hash(user.password_hash, form.password.data):
            flash('Logged in successfully!')
            return redirect(url_for('home'))
        else:
            flash('Invalid username or password')
    return render_template('login.html', title='Sign In', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    """
    Handle user registration.

    This route manages both displaying the registration form (GET request) and
    processing the registration data (POST request). It creates a new user
    account and stores it in the database.

    Returns:
        render_template or redirect: Renders the registration form or redirects
        to the login page upon successful registration.
    """
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data)
        user = User(username=form.username.data, email=form.email.data, password_hash=hashed_password)
        # Add user to database here
        flash(f'Registration successful for user {form.username.data}')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route('/api/user/<username>', methods=['GET'])
def get_user(username):
    """
    Retrieve a user's details based on their username.

    This API endpoint fetches user details for a given username and returns them in JSON format.

    Args:
        username (str): The username of the user to be retrieved.

    Returns:
        jsonify: Returns a JSON object containing user details or an error
        message if the user is not found.
    """
    user = User.query.filter_by(username=username).first()
    if user is None:
        return jsonify({'error': 'User not found'}), 404
    return jsonify({
        'username': user.username,
        'email': user.email
        # Include other fields you want to expose
    })

@app.route('/api/users', methods=['GET'])
def get_users():
    """
    Retrieve details of all users.

    This API endpoint fetches details of all registered users and returns them
    in a list format in JSON.

    Returns:
        jsonify: Returns a JSON list containing details of all users.
    """
    users = User.query.all()
    return jsonify([{'username': user.username, 'email': user.email} for user in users])

@app.route('/api/user', methods=['POST'])
def create_user():
    """
    Create a new user via the API.

    This API endpoint allows for the creation of a new user with provided
    username, email, and password. It handles validation and uniqueness checks.

    Returns:
        jsonify: Returns a JSON object containing the newly created user's
        details or an error message.
    """
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')
    if username is None or email is None or password is None:
        return jsonify({'error': 'Missing data'}), 400
    if User.query.filter_by(username=username).first() is not None:
        return jsonify({'error': 'User already exists'}), 400
    hashed_password = generate_password_hash(password)
    user = User(username=username, email=email, password_hash=hashed_password)
    # Add user to database here
    return jsonify({'username': user.username, 'email': user.email}), 201
