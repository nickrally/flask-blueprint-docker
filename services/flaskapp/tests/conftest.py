import pytest
from ..project import create_app, db
from ..project.models import thing


@pytest.fixture()
def test_client():
    app = create_app()
    app.config.update({
        "TESTING": True,
    })
    # Create a test client using the Flask application configured for testing
    with app.test_client() as testing_client:
        # Establish an application context
        with app.app_context():
            yield testing_client  # this is where the testing happens!


@pytest.fixture(scope='module')
def init_database(test_client):
    # Create the database and the database table
    db.create_all()

    # Insert
    thing1 = thing.Thing(
        name='toves', description='something like badgers, something like lizards and something like corkscrews')
    thing2 = thing.Thing(name='slithy', description='lithe and slimy')
    db.session.add(thing1)
    db.session.add(thing2)

    # Commit the changes for the users
    db.session.commit()

    yield  # this is where the testing happens!

    db.drop_all()
