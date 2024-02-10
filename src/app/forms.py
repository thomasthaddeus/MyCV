"""forms.py

This module defines the form classes for user authentication in a Flask web
application using Flask-WTF, an extension for Flask that integrates with
WTForms for form handling.

The module includes two classes, `LoginForm` and `RegistrationForm`, which are
used for user login and registration respectively. These forms utilize WTForms'
field types and validators to ensure that the data submitted by the user meets
certain criteria before being processed by the application.

The `LoginForm` class handles user authentication, while the `RegistrationForm`
class handles new user registration, including validations for email format and
password confirmation.

Returns:
    FlaskForm instances: Instances of FlaskForm classes, ready to be rendered
    in templates and handle user input for authentication and registration
    processes.
"""

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo


class LoginForm(FlaskForm):
    """
    LoginForm for user authentication in a Flask web application.

    This form class is used to create a login form for users. It includes
    fields for username, password, and a 'remember me' option. The form uses
    WTForms validators to ensure that the username and password fields are not
    empty.

    Attributes:
        username (StringField): Field for the user's username, required.
        password (PasswordField): Field for the user's password, required.
        remember_me (BooleanField): Checkbox to allow users to stay logged in.
        submit (SubmitField): Button to submit the form.

    Inherits:
        FlaskForm: Inherits from FlaskForm which provides form handling with Flask and WTForms.
    """

    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    remember_me = BooleanField("Remember Me")
    submit = SubmitField("Sign In")


class RegistrationForm(FlaskForm):
    """
    RegistrationForm for new user registration in a Flask web application.

    This form class is used to create a registration form for new users. It
    includes fields for username, email, password, and password confirmation.
    It uses WTForms validators to ensure that all fields are filled out
    correctly, the email is valid, and the passwords match.

    Attributes:
        username (StringField): Field for the new user's username, required.
        email (StringField): Field for the new user's email, required and
          validated for email format.
        password (PasswordField): Field for the new user's password, required.
        password2 (PasswordField): Field for confirming the password, must
          match the first password.
        submit (SubmitField): Button to submit the form.

    Inherits:
        FlaskForm: Inherits from FlaskForm which provides form handling with
        Flask and WTForms.
    """

    username = StringField("Username", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    password2 = PasswordField(
        "Repeat Password", validators=[DataRequired(), EqualTo("password")]
    )
    submit = SubmitField("Register")
