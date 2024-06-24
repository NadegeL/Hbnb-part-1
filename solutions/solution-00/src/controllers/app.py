# config.py

# Import the necessary module
from flask_jwt_extended import JWTManager
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Initialize the Flask app
app = Flask(__name__)
env = os.environ.get('ENV', 'development')

if env == 'development':
	app.config.from_object(DevelopmentConfig)

else:
    app.config.from_object(ProductionConfig)

db = SQLAlchemy(app)

# Ensure that the SQLite database is created if it does not exist
if env == 'development':
    with app.app_context():
        db.create_all()

@app.route('/')
def index():
    return "Hello, World!"

if __name__ == '__main__':
    app.run()

app.config['JWT_SECRET_KEY'] = 'super-secret'
jwt = JWTManager(app)