"""models.py

This module defines the data models used in a Flask web application,
specifically focusing on user management.

It uses SQLAlchemy for ORM (Object-Relational Mapping) to map Python classes to
database tables. The module includes the `User` and `Profile` classes, which
represent the users of the application and their profiles respectively.

The `User` class contains user-specific information like username, email, and
password hash. The `Profile` class allows for the extension of user information
through a one-to-one relationship with the `User` class.

Returns:
    Instances of SQLAlchemy Models: This module doesn't return values directly
    but defines classes that are used by SQLAlchemy to interact with a database.
"""

from datetime import datetime
from app import db  # Assuming you have already initialized SQLAlchemy as 'db' in your app package

class User(db.Model):
    """
    Represents a user in the application.

    This class maps to a database table `user` and includes fields for the
    user's id, username, email, and password hash. It also has a one-to-one
    relationship with the `Profile` class, allowing users to have an associated
    profile.

    Attributes:
        id (int): Unique identifier for the user.
        username (str): Username of the user, must be unique.
        email (str): Email address of the user, must be unique.
        password_hash (str): Hashed password for security purposes.
        profile (relationship): A SQLAlchemy relationship that links to the
          user's profile.

    Methods:
        __repr__: Returns a string representation of the user, typically used
          for debugging purposes.
    """
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    profile = db.relationship('Profile', backref='user', uselist=False)

    def __repr__(self):
        """
        Provide a human-readable representation of the User instance.

        This method is primarily used for debugging and logging purposes. It
        returns a string that is intended to be a clear and concise description
        of the user instance, typically including the username.

        Returns:
            str: A string representation of the user, including the username.
        """
        return f'<User {self.username}>'

class Profile(db.Model):
    """
    Represents a user's profile in the application.

    This class maps to a database table `profile` and includes fields for the
    profile's id, bio, and a foreign key linking to the `User` class. Each user
    has one associated profile, and this relationship is managed through the
    `user_id` field.

    Attributes:
        id (int): Unique identifier for the profile.
        bio (str): A short biography or description of the user.
        user_id (int): Foreign key that links to the associated user's id.

    Methods:
        __repr__: Returns a string representation of the profile, typically
          used for debugging purposes.
    """
    id = db.Column(db.Integer, primary_key=True)
    bio = db.Column(db.String(500))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        """
        Provide a human-readable representation of the Profile instance.

        This method is used for debugging and logging. It returns a string
        that gives a quick overview of the profile instance, usually including
        the associated user's ID.

        Returns:
            str: A string representation of the profile, indicating which user
                 it is associated with.
        """
        return f'<Profile for user {self.user_id}>'
