from io import StringIO
from unittest import main, TestCase
import models

#
# Do Function/File imports here once they exist
#


# -----------
# TestNetflix
# -----------


class TestModels(TestCase):

    # ---------
    # Episodes
    # ---------

    def test_episode_insert(self):
        test_episode = {"name": "TestEpisode", "season": "3", "predecessor": "TestPrevEp",
                        "successor": "TestNextEp", "characters": "Jon Snow, Benjen Stark, Eddard Stark"}
        
        ep = models.Episode(**test_episode)
        self.session.add(ep)
        result = self.session.query(Episode).filter(Episode.name == "TestEpisode").first()

        self.assertEqual(result.season, "3")
        self.assertEqual(result.predecessor, "TestNextEp")
        self.assertEqual(result.successor, "TestPrevEp")
        self.assertEqual(result.characters, "Jon Snow, Benjen Stark, Eddard Stark")


	def test_episode_delete(self):
		test_episode = self.session.query(Episode).filter(Episode.name == "TestEpisode").first()
		self.session.delete(test_episode)

		test_episode = self.session.query(Episode).filter(Episode.name == "TestEpisode").first()
		self.assertEqual(test_episode, None)


	def test_next_episode(self):
		episodes = self.session.query(Episode).all()
		for x in range(0, len(episodes) - 1):
			self.assertEqual(episodes[x].next_episode, episodes[x].name)


    # -------
    # Houses
    # -------

    def test_house_insert(self):
        test_house = {"name": "TestHouse", "region": "Norf", "words": "DA KING OF DA NORF", "current_lord": "TestLord",  "overlord": "TestOverLord"}

        h = models.House(**test_house)
        self.session.add(h)
        result = self.session.query(House).filter(House.name == "TestHouse").first()

        self.assertEqual(result.region, "Norf")
        self.assertEqual(result.words, "DA KING OF DA NORF")
        self.assertEqual(result.current_lord, "TestLord")
        self.assertEqual(result.overlord, "TestOverLord")


	def test_house_delete(self):
		test_house = self.session.query(House).filter(House.name == "TestHouse").first()
		self.session.delete(test_house)

		test_house = self.session.query(House).filter(House.name == "TestHouse").first()
		self.assertEqual(test_house, None)


	def test_house_unique(self):
		houses = self.session.query(House).all()
		for x in range(0, len(houses)):
			for y in range(0, len(houses)):
				self.assertNotEqual(houses[x].name, houses[y].name)


    # -----------
    # Characters
    # -----------

    def test_character_insert(self):
        test_character = {"name": "Kieran", "titles": "Lord of the Python Tests", "aliases": "-",
                        "father": "OOP", "mother": "JavaScript", "spouse" : "Madam Tests.py", "actor" : "Himself"}
        
        c = models.Character(**test_character)
        self.session.add(c)
        result = self.session.query(Character).filter(Character.name == "Kieran").first()

        self.assertEqual(result.titles, "Lord of the Python Tests")
        self.assertEqual(result.aliases, "-")
        self.assertEqual(result.father, "OOP")
        self.assertEqual(result.mother, "JavaScript")
        self.assertEqual(result.spouse, "Madam Tests.py")
        self.assertEqual(result.actor, "Himself")


	def test_character_delete(self):
		test_character = self.session.query(Character).filter(Character.name == "Kieran").first()
		self.session.delete(test_character)

		test_character = self.session.query(Character).filter(Character.name == "Kieran").first()
		self.assertEqual(test_character, None)


	def test_character_unique(self):
		characters = self.session.query(Character).all()
		for x in range(0, len(characters)):
			for y in range(0, len(characters)):
				self.assertNotEqual(characters[x].name, characters[y].name)

# ----
# main
# ----

if __name__ == "__main__":
    main()
