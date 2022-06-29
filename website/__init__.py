from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "f8ae4b6af41137f26af63cdbd05ceb58037aa598c2f74df719eaa72b38938199"

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")
    return app