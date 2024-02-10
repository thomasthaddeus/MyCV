"""app.py

This module is the entry point for a Flask web application. It initializes the
Flask app and sets up key components like SQLAlchemy for database interactions
and Flask-Migrate for database migrations.

The module imports configurations from a separate `Config` class, sets up the
database connection, and includes routes, models, and forms from the 'src'
directory. It's designed to launch the web application and handle high-level
configurations and initializations.

The module also includes a conditional statement to run the application in
debug mode when executed directly, facilitating easier development and
debugging.

Extended Summary:
- Flask instance initialization: Sets up the Flask app with configurations
  defined in `Config`.
- SQLAlchemy setup: Initializes SQLAlchemy for database ORM (Object-Relational
  Mapping), allowing easy interaction between Python objects and the database.
- Flask-Migrate integration: Configures Flask-Migrate for handling database
  migrations, which is useful for updating the database schema without losing
  data.
- Routes, models, and forms integration: Imports and registers routes, models,
  and forms from the 'src' directory, organizing the application structure.
- Application execution: Contains a conditional block to run the application,
  primarily used during development for running the Flask development server.

Usage:
To run the application, execute this script directly. It will start a Flask
development server on the localhost.

    $ python app.py
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config
from src import LoginForm, RegistrationForm, Profile, User

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)


if __name__ == "__main__":
    app.run(debug=True)
