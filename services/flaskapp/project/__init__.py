from flask import Flask
from .extensions import db, migrate
from .routes.poem import poem
from .routes.home import home
from .routes.add import add
from .routes.delete import delete
from .routes.edit import edit


def create_app():
    app = Flask(__name__)
    app.config.from_object("project.config.Config")
    db.init_app(app)
    migrate.init_app(app, db)
    app.register_blueprint(poem)
    app.register_blueprint(home)
    app.register_blueprint(add)
    app.register_blueprint(delete)
    app.register_blueprint(edit)
    return app
