from app import tests
from app import db, models
import anapioficeandfire

def test():
    tests.test_episode_insert(db)
    tests.test_episode_delete(db)
    tests.test_episode_unique(db)
    tests.test_house_insert(db)
    tests.test_house_delete(db)
    tests.test_house_unique(db)
    tests.test_character_insert(db)
    tests.test_character_delete(db)
    tests.test_character_unique(db)

if __name__ == "__main__":
    test()
