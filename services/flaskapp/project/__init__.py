from flask import Flask
from .extensions import db, migrate
from .routes.main import main


def create_app():
    app = Flask(__name__)
    app.config.from_object("project.config.Config")
    db.init_app(app)
    migrate.init_app(app, db)
    app.register_blueprint(main)
    return app
