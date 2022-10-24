import pytest
from ..project import create_app, db
from ..project.models import thing


@pytest.fixture(scope='module')
def test_client():
    app = create_app()
    app.config.update({
        "TESTING": True,
    })
    print(app.config['SQLALCHEMY_DATABASE_URI'])
    with app.test_client() as testing_client:
        with app.app_context():
            yield testing_client


""" @pytest.fixture(scope='module')
def init_database(test_client):
    db.create_all()
    thing1 = thing.Thing(
        name='toves', description='something like badgers, something like lizards and something like corkscrews')
    thing2 = thing.Thing(name='slithy', description='lithe and slimy')
    db.session.add(thing1)
    db.session.add(thing2)

    db.session.commit()

    yield  

    db.drop_all() """
