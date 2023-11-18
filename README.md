# Flask CV and User Management Application

## Overview

This Flask application provides a platform to display a Curriculum Vitae (CV) and includes features such as user authentication, profile management, and testing. The application is built using Flask, along with extensions like Flask-WTF for form handling, Flask-SQLAlchemy for database interactions, and Flask-Migrate for database migrations.

## Features

- Display a CV
- User registration and login
- User profile management
- Responsive design using Bootstrap
- Unit testing for routes, models, and configurations

## Installation

### Prerequisites

- Python 3
- pip
- Virtual environment (recommended)

### Setup

1. **Clone the repository**

   ```bash
   git clone https://github.com/thomasthaddeus/my-cv.git
   cd your-repository
   ```

2. **Create and activate a virtual environment (optional but recommended)**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Environment Variables**
   - Copy `.env.example` to `.env` and fill in your environment variables.
   - Set `FLASK_APP=app.py` and `FLASK_ENV=development` in `.flaskenv` for development.

5. **Initialize the database**

   ```bash
   flask db upgrade
   ```

6. **Run the application**

   ```bash
   flask run
   ```

## Usage

Navigate to `http://localhost:5000` in your web browser to view the application.

## Testing

Run tests with the following command:

```bash
python -m unittest
```

## Structure

- `app/`: Application package.
  - `templates/`: Jinja2 templates.
  - `static/`: Static files like CSS, JavaScript, and images.
  - `models.py`: Database models.
  - `forms.py`: WTForms classes.
  - `routes.py`: Application routes.
- `tests/`: Unit and integration tests.
- `requirements.txt`: List of dependencies.
- `config.py`: Configuration settings.
- `.env`: Environment variables (not tracked by git).
- `.flaskenv`: Flask-specific environment variables.

## Contributing

Contributions are welcome! Please read `CONTRIBUTING.md` for guidelines on how to submit contributions to this project.

## License

Distributed under the MIT License. See [`LICENSE`](./LICENSE) for more information.
