from app import db

"""
Episode model
Attributes: name, season, previous episode, next episode, characters
"""
class Episode(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True)
    season = db.Column(db.Integer)
    previous_epsiode = db.Column(db.String, unique=True)
    next_episode = db.Column(db.String, unique=True)
    characters = db.Column(db.String)

    def __init__(self, name, season, previous_episode, next_episode,
            characters):
        self.name = name
        self.season = season
        self.previous_episode = previous_episode
        self.next_episode = next_episode

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

    def __init__(self, name, region, words, current_lord, title, overlord):
        self.name = name
        self.region = region
        self.words = words
        self.current_lord = current_lord
        self.title = title
        self.overlord = overlord

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

    def __init__(self, name, titles, father, mother, spouse, house, actor):
        self.name = name
        self.titles = titles
        self.father = father
        self.mother = mother
        self.spouse = spouse
        self.house = house
        self.actor = actor

