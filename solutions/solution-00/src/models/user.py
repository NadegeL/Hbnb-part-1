"""
User related functionality
"""
from src.models import db
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)
    
    def set_password(self, password):
        self.password = generate_password_hash(password)
        
    def check_password(self, password):
        return check_password_hash(self.password, password)

    @staticmethod
    def create(data):
        if User.query.filter_by(email=data["email"]).first():
            raise ValueError("User already exists")

        new_user = User(**data)
        db.session.add(new_user)
        db.session.commit()

        return new_user

    @staticmethod
    def update(entity_id, data):
        user = User.query.get(entity_id)
        if not user:
            return None

        if "email" in data:
            user.email = data["email"]
        if "first_name" in data:
            user.first_name = data["first_name"]
        if "last_name" in data:
            user.last_name = data["last_name"]

        db.session.commit()
        return user
