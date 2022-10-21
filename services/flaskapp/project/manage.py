from flask.cli import FlaskGroup

from project import create_app, db
from project.models import Thing

app = create_app()
cli = FlaskGroup(app)


@cli.command("create_db")
def create_db():
    """create_all doesn't issue CREATEs for tables already present in the target database."""
    db.create_all()
    db.session.commit()


@cli.command("seed_db")
def seed_db():
    db.session.add(Thing(name="Brillig"))
    db.session.commit()


if __name__ == "__main__":
    cli()
