from app import tests
from app import db, models
import anapioficeandfire

if __name__ == "__main__":
	tests.test_episode_insert(db)