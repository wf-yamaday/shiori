from infrastructure.database import db
from datetime import datetime
from marshmallow_sqlalchemy import ModelSchema


class Bookmark(db.Model):
    __tablename__ = 'bookmarks'

    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.TEXT, nullable=False)
    memo = db.Column(db.String(255), nullable=True)
    ogp = db.Column(db.JSON, nullable=True)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
    updated_at = db.Column(db.DateTime, nullable=False,
                           default=datetime.now, onupdate=datetime.now)

    def find_all(self):
        return Bookmark.query.all()

    def save(self, bookmark):
        db.session.add(bookmark)
        db.session.commit()


class BookmarkSchema():
    class Meta:
        model = Bookmark
