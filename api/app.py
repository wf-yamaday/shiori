from flask import Flask, request, jsonify
from infrastructure.database import init_db
from infrastructure.models import Bookmark, BookmarkSchema
from flask_cors import CORS


def create_app():
    app = Flask(__name__)
    CORS(app)
    app.config.from_object('config.Config')
    init_db(app)

    return app


app = create_app()


@app.route('/bookmarks', methods=['GET'])
def index():
    bookmark = Bookmark()
    bookmarks = bookmark.find_all()
    print(bookmarks)
    bookmarks_schema = BookmarkSchema(many=True)
    return jsonify(bookmarks_schema.dump(bookmarks))


@app.route('/bookmarks', methods=['POST'])
def save():
    req = request.get_json()
    bookmark = Bookmark()
    bookmark.url = req['url']
    bookmark.memo = req['memo']
    bookmark.ogp = req['ogp']
    bookmark.save(bookmark)
    return jsonify(req)
