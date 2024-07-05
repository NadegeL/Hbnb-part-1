# src/models/review.py

from src.app import db
from src.models.base import Base
from src.models.place import Place
from src.models.user import User

class Review(Base):
    __tablename__ = 'reviews'

    place_id = db.Column(db.String(36), db.ForeignKey('places.id'), nullable=False)
    user_id = db.Column(db.String(36), db.ForeignKey('users.id'), nullable=False)
    comment = db.Column(db.Text, nullable=False)
    rating = db.Column(db.Float, nullable=False)

    def __repr__(self):
        """String representation of the Review"""
        return f"<Review {self.id} - '{self.comment[:25]}...'>"

    def to_dict(self):
        """Dictionary representation of the object"""
        return {
            "id": self.id,
            "place_id": self.place_id,
            "user_id": self.user_id,
            "comment": self.comment,
            "rating": self.rating,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
        }

    @staticmethod
    def create(data: dict) -> "Review":
        """Create a new review"""
        user = User.get(data["user_id"])
        if not user:
            raise ValueError(f"User with ID {data['user_id']} not found")

        place = Place.get(data["place_id"])
        if not place:
            raise ValueError(f"Place with ID {data['place_id']} not found")

        new_review = Review(**data)
        db.session.add(new_review)
        db.session.commit()
        return new_review

    @staticmethod
    def update(review_id: str, data: dict) -> "Review | None":
        """Update an existing review"""
        review = Review.get(review_id)
        if not review:
            raise ValueError("Review not found")

        for key, value in data.items():
            setattr(review, key, value)

        db.session.commit()
        return review

    @staticmethod
    def get_all() -> list["Review"]:
        """Get all reviews"""
        return Review.query.all()

    @staticmethod
    def delete(review_id: str) -> bool:
        """Delete a review by ID"""
        review = Review.get(review_id)
        if review:
            db.session.delete(review)
            db.session.commit()
            return True
        return False
