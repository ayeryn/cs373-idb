from app import app as application
from io import StringIO
from unittest import main, TestCase
import models
from models import db

#
# Do Function/File imports here once they exist
#

TESTOR = TestCase('__init__')
# ---------
# Episodes
# ---------

def test_episode_insert(db):
    test_episode = {"name": "TestEpisode", "season": "3", "nr": "1002", "predecessor": "TestPrevEp",
                    "successor": "TestNextEp", "imageLink": "-"}
    
    ep = models.Episode(**test_episode)
    db.session.add(ep)
    result = db.session.query(models.Episode).filter(models.Episode.name == "TestEpisode").first()

    TESTOR.assertEqual(result.season, "3")
    TESTOR.assertEqual(result.nr, "1002")
    TESTOR.assertEqual(result.predecessor, "TestPrevEp")
    TESTOR.assertEqual(result.successor, "TestNextEp")


def test_episode_delete(db):
    test_episode = db.session.query(models.Episode).filter(models.Episode.name == "TestEpisode").first()
    db.session.delete(test_episode)

    test_episode = db.session.query(models.Episode).filter(models.Episode.name == "TestEpisode").first()
    TESTOR.assertEqual(test_episode, None)


def test_episode_unique(db):
    episodes = db.session.query(models.Episode).all()
    for x in range(0, len(episodes)):
        for y in range(x + 1, len(episodes)):
            TESTOR.assertNotEqual(episodes[x].name, episodes[y].name)


# -------
# Houses
# -------

def test_house_insert(db):
    test_house = {"name": "TestHouse", "region": "Norf", "words": "DA KING OF DA NORF", "current_lord": "TestLord", "title": "TestTitle", "overlord": "TestOverLord", "imageLink": "-"}

    h = models.House(**test_house)
    db.session.add(h)
    result = db.session.query(models.House).filter(models.House.name == "TestHouse").first()

    TESTOR.assertEqual(result.region, "Norf")
    TESTOR.assertEqual(result.words, "DA KING OF DA NORF")
    TESTOR.assertEqual(result.current_lord, "TestLord")
    TESTOR.assertEqual(result.title, "TestTitle")
    TESTOR.assertEqual(result.overlord, "TestOverLord")


def test_house_delete(db):
    test_house = db.session.query(models.House).filter(models.House.name == "TestHouse").first()
    db.session.delete(test_house)

    test_house = db.session.query(models.House).filter(models.House.name == "TestHouse").first()
    TESTOR.assertEqual(test_house, None)


def test_house_unique(db):
    houses = db.session.query(models.House).all()
    for x in range(0, len(houses)):
        for y in range(x + 1, len(houses)):
            TESTOR.assertNotEqual(houses[x].name, houses[y].name)


# -----------
# Characters
# -----------

def test_character_insert(db):
    test_character = {"name": "Kieran", "titles": "Lord of the Python Tests", "father": "OOP", 
                    "mother": "JavaScript", "spouse" : "Madam Tests.py", "house": "Slytherin", "actor" : "Himself", "imageLink": "-"}
    
    c = models.Character(**test_character)
    db.session.add(c)
    result = db.session.query(models.Character).filter(models.Character.name == "Kieran").first()

    TESTOR.assertEqual(result.titles, "Lord of the Python Tests")
    TESTOR.assertEqual(result.father, "OOP")
    TESTOR.assertEqual(result.mother, "JavaScript")
    TESTOR.assertEqual(result.spouse, "Madam Tests.py")
    TESTOR.assertEqual(result.house, "Slytherin")
    TESTOR.assertEqual(result.actor, "Himself")


def test_character_delete(db):
    test_character = db.session.query(models.Character).filter(models.Character.name == "Kieran").first()
    db.session.delete(test_character)

    test_character = db.session.query(models.Character).filter(models.Character.name == "Kieran").first()
    TESTOR.assertEqual(test_character, None)


def test_character_unique(db):
    characters = db.session.query(models.Character).all()
    for x in range(0, len(characters)):
        for y in range(x + 1, len(characters)):
            TESTOR.assertNotEqual(characters[x].name, characters[y].name)

# ---------
# run tests
# ---------

def test():
    start = time.time()
    test_episode_insert(db)
    test_episode_delete(db)
    test_episode_unique(db)
    test_house_insert(db)
    test_house_delete(db)
    test_house_unique(db)
    test_character_insert(db)
    test_character_delete(db)
    test_character_unique(db)
    end = time.time()
    return end-start

# ----
# main
# ----

if __name__ == "__main__":
    main()
