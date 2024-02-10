"""config.py

This module defines the configuration settings for a Flask web application. It
uses environment variables to set key configuration parameters, providing a
flexible and secure way to manage the application's configuration depending on
the environment it is running in (development, testing, production, etc.).

The `Config` class includes settings for the secret key, database connection,
mail server, and other Flask extensions or application-specific settings. If
environment variables are not set, default values are provided.

_extended_summary_:
- Secret Key: Used for securely signing the session cookie and can be used for
  other security-related needs in the application. It's important to set a
  strong, unpredictable key in production.
- Database Configuration: Specifies the URI for the database connection.
  Supports various database systems, with a default to SQLite for ease of
  development.
- SQLAlchemy Track Modifications: Disables the modification tracking system of
  SQLAlchemy to save system resources.
- Mail Server Configuration: Includes settings like the mail server, port, and
  credentials, useful for email functionalities in the application (e.g.,
  sending password reset emails).
- Environment Variables: The class emphasizes the use of environment variables,
  allowing sensitive information to be kept out of the source code.

Usage:
The configuration class is typically imported and used to configure a Flask
application instance.

    from config import Config
    app.config.from_object(Config)
"""

import os

class Config:
    """
    Configuration class for Flask application.

    This class provides configuration variables for the Flask application. It
    uses environment variables to set these configurations, with default values
    for development. It includes configurations for database connections, mail
    server settings, and other Flask-related settings.

    Attributes:
        SECRET_KEY (str): Secret key for the application, crucial for security.
        SQLALCHEMY_DATABASE_URI (str): Database URI for SQLAlchemy.
        SQLALCHEMY_TRACK_MODIFICATIONS (bool): Flag for SQLAlchemy modification
          tracking.
        MAIL_SERVER (str): Address of the mail server.
        MAIL_PORT (int): Port number of the mail server.
        MAIL_USE_TLS (bool): Boolean to enable/disable TLS for the mail server.
        MAIL_USERNAME (str): Username for the mail server.
        MAIL_PASSWORD (str): Password for the mail server.
        [Other configuration variables]: More configurations can be added as needed.
    """
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///mydatabase.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    # Other configuration variables can be added here
