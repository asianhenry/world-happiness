from .app import db


class Happy(db.Model):
    __tablename__ = "happiness" # required field  
    index = db.Column(Integer, primary_key=True, nullable=False)
    country = db.Column(db.String(100))
    rank = db.Column(db.Integer)
    score = db.Column(db.Float)
    economy = db.Column(db.Float)
    family = db.Column(db.Float)
    health = db.Column(db.Float)
    freedom = db.Column(db.Float)
    generosity = db.Column(db.Float)
    trust = db.Column(db.Float)
    year = db.Column(db.Integer)
    lat = db.Column(db.Float)
    long = db.Column(db.Float)

    def __repr__(self):
        return '<Happy %r>' % (self.name)
