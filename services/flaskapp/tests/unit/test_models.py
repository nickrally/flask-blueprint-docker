from ...project.models import thing


def test_new_thing():
    """
    GIVEN a Thing model
    WHEN a new Thing is created
    THEN check name and description are correct
    """
    name = "brillig"
    description = "four o'clock in the afternoon — the time when you begin broiling things for dinner"
    new_thing = thing.Thing(name, description)
    assert new_thing.name == name
    assert new_thing.description == description
