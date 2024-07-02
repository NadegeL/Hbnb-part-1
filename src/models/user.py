"""
User related functionality
"""
from src.models.base import Base, db_session
from src import db
from src.models.base import Base
from src import bcrypt


class User(Base):
    __tablename__ = 'users'

    email = db.Column(db.String(120), unique=True, nullable=False)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)

    def set_password(self, password):
        self.password_hash = bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password_hash, password)


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
