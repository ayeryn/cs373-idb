from app import tests
from app import db, models
import anapioficeandfire

if __name__ == "__main__":
	tests.test_episode_insert(db)
	tests.test_episode_delete(db)
	#tests.test_next_episode(db)
	tests.test_house_insert(db)
	tests.test_house_delete(db)
	tests.test_house_unique(db)
	tests.test_character_insert(db)
	tests.test_character_delete(db)
	tests.test_character_unique(db)