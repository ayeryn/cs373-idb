from app import db

"""
Episode model
Attributes: name, season, predecessor, next episode, characters
"""
class Episode(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True)
    season = db.Column(db.Integer)
    predecessor = db.Column(db.String, unique=True)
    successor = db.Column(db.String, unique=True)
    characters = db.Column(db.String)
    imageLink = db.Column(db.String, unique=True)

    def __init__(self, name, season, predecessor, successor, imageLink):
        self.name = name
        self.season = season
        self.predecessor = predecessor
        self.successor = successor
        self.imageLink = imageLink

"""
House model
Attributes: name, region, words, current_lord, title, overlord
"""
class House(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True)
    region = db.Column(db.String)
    words = db.Column(db.String)
    current_lord = db.Column(db.String)
    title = db.Column(db.String)
    overlord = db.Column(db.String)
    imageLink = db.Column(db.String, unique=True)

    def __init__(self, name, region, words, current_lord, title, overlord, imageLink):
        self.name = name
        self.region = region
        self.words = words
        self.current_lord = current_lord
        self.title = title
        self.overlord = overlord
        self.imageLink = imageLink

"""
Characters model
Attributes: name, titles, aliases, father, mother, spouse, allegiance, played_by
"""
class Character(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True)
    titles = db.Column(db.String, unique=True)
    father = db.Column(db.String)
    mother = db.Column(db.String)
    spouse = db.Column(db.String)
    house = db.Column(db.String)
    actor = db.Column(db.String, unique=True)
    imageLink = db.Column(db.String, unique=True)

    def __init__(self, name, titles, father, mother, spouse, house, actor, imageLink):
        self.name = name
        self.titles = titles
        self.father = father
        self.mother = mother
        self.spouse = spouse
        self.house = house
        self.actor = actor
        self.imageLink = imageLink
