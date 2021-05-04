from flask import Flask, request, jsonify
from infrastructure.database import init_db
from infrastructure.models import Bookmark, BookmarkSchema
from flask_cors import CORS
from service.bookmarks import save_bookmark

from infrastructure.milvus import init_milvus


def create_app():
    app = Flask(__name__)
    CORS(app)
    app.config.from_object('config.Config')
    init_db(app)

    return app


app = create_app()


@app.route('/bookmarks/<int:id>', methods=['GET'])
def get(id):
    bookmark = Bookmark().find_one(id)
    bookmark_schema = BookmarkSchema()
    return jsonify(bookmark_schema.dump(bookmark))


@app.route('/bookmarks', methods=['GET'])
def index():
    bookmark = Bookmark()
    bookmarks = bookmark.find_all()
    bookmarks_schema = BookmarkSchema(many=True)
    return jsonify(bookmarks_schema.dump(bookmarks))


@app.route('/bookmarks', methods=['POST'])
def save():
    req = request.get_json()
    if save_bookmark(req):
        return jsonify(req)
    else:
        return 'error'


@app.route('/init', methods=['POST'])
def init():
    if init_milvus('bookmarks'):
        return 'success'
    return 'error'
