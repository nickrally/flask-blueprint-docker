from ..extensions import db


class Thing(db.Model):
    __tablename__ = 'thing'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    description = db.Column(db.String(255))

    def __init__(self, name: str, description: str):
        """Create a new Thing object using the name and description
        """
        self.name = name
        self.description = description
