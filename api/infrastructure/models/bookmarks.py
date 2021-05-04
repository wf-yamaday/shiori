from infrastructure.database import db, ma
from datetime import datetime
from sqlalchemy import desc
from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field


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
        return Bookmark.query.order_by(desc(Bookmark.created_at)).all()

    def find_one(self, id):
        return Bookmark.query.filter_by(id=id).first()

    def find_by_ids(self, ids):
        return Bookmark.query.filter(Bookmark.id.in_(ids)).all()

    def save(self, bookmark):
        db.session.add(bookmark)
        db.session.commit()
        return bookmark


class BookmarkSchema(SQLAlchemySchema):
    class Meta:
        model = Bookmark
        load_instance = True

    id = auto_field()
    url = auto_field()
    memo = auto_field()
    ogp = auto_field()
    created_at = auto_field()
    updated_at = auto_field()
