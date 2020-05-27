# web_app\__init__.py

from flask import Flask

from web_app.routes.home_routes import home_routes
from web_app.routes.suggestion_routes import suggestion_routes


def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    app.register_blueprint(home_routes)
    app.register_blueprint(suggestion_routes)

    return app


if __name__ == "__main__":
    spotify_app = create_app()
    spotify_app.run(debug=True)
