from app import app as application
from io import StringIO
from unittest import main, TestCase
import models
from models import db

#
# Do Function/File imports here once they exist
#


# -----------
# TestNetflix
# -----------


# ---------
# Episodes
# ---------

def test_episode_insert(db):
    test_episode = {"name": "TestEpisode", "season": "3", "predecessor": "TestPrevEp",
                    "successor": "TestNextEp", "imageLink": "-"}
    
    ep = models.Episode(**test_episode)
    db.session.add(ep)
    result = db.session.query(Episode).filter(Episode.name == "TestEpisode").first()

    db.assertEqual(result.season, "3")
    db.assertEqual(result.predecessor, "TestNextEp")
    db.assertEqual(result.successor, "TestPrevEp")


def test_episode_delete(self):
    test_episode = db.session.query(Episode).filter(Episode.name == "TestEpisode").first()
    db.session.delete(test_episode)

    test_episode = self.session.query(Episode).filter(Episode.name == "TestEpisode").first()
    db.assertEqual(test_episode, None)


def test_next_episode(self):
    episodes = db.session.query(Episode).all()
    for x in range(0, len(episodes) - 1):
        db.assertEqual(episodes[x].next_episode, episodes[x].name)


# -------
# Houses
# -------

def test_house_insert(self):
    test_house = {"name": "TestHouse", "region": "Norf", "words": "DA KING OF DA NORF", "current_lord": "TestLord", "title": "TestTitle", "overlord": "TestOverLord", "imageLink": "-"}

    h = models.House(**test_house)
    db.session.add(h)
    result = db.session.query(House).filter(House.name == "TestHouse").first()

    db.assertEqual(result.region, "Norf")
    db.assertEqual(result.words, "DA KING OF DA NORF")
    db.assertEqual(result.current_lord, "TestLord")
    db.assertEqual(result.title, "TestTitle")
    db.assertEqual(result.overlord, "TestOverLord")


def test_house_delete(self):
    test_house = db.session.query(House).filter(House.name == "TestHouse").first()
    db.session.delete(test_house)

    test_house = db.session.query(House).filter(House.name == "TestHouse").first()
    db.assertEqual(test_house, None)


def test_house_unique(self):
    houses = db.session.query(House).all()
    for x in range(0, len(houses)):
        for y in range(0, len(houses)):
            db.assertNotEqual(houses[x].name, houses[y].name)


# -----------
# Characters
# -----------

def test_character_insert(self):
    test_character = {"name": "Kieran", "titles": "Lord of the Python Tests", "father": "OOP", 
                    "mother": "JavaScript", "spouse" : "Madam Tests.py", "house": "Slytherin", "actor" : "Himself", "imageLink": "-"}
    
    c = models.Character(**test_character)
    db.session.add(c)
    result = db.session.query(Character).filter(Character.name == "Kieran").first()

    db.assertEqual(result.titles, "Lord of the Python Tests")
    db.assertEqual(result.aliases, "-")
    db.assertEqual(result.father, "OOP")
    db.assertEqual(result.mother, "JavaScript")
    db.assertEqual(result.spouse, "Madam Tests.py")
    db.assertEqual(result.house, "Slytherin")
    db.assertEqual(result.actor, "Himself")


def test_character_delete(self):
    test_character = db.session.query(Character).filter(Character.name == "Kieran").first()
    db.session.delete(test_character)

    test_character = db.session.query(Character).filter(Character.name == "Kieran").first()
    db.assertEqual(test_character, None)


def test_character_unique(self):
    characters = db.session.query(Character).all()
    for x in range(0, len(characters)):
        for y in range(0, len(characters)):
            db.assertNotEqual(characters[x].name, characters[y].name)

# ----
# main
# ----

if __name__ == "__main__":
    main()
