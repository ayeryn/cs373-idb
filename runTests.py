from app import tests
from app import db, models
import anapioficeandfire
import time

def test():
    start=time.time()
    tests.test_episode_insert(db)
    tests.test_episode_delete(db)
    #tests.test_next_episode(db)
    tests.test_house_insert(db)
    tests.test_house_delete(db)
    tests.test_house_unique(db)
    tests.test_character_insert(db)
    tests.test_character_delete(db)
    tests.test_character_unique(db)
    end = time.time()
    print start, end
    return (end-start)

if __name__ == "__main__":
    test()
