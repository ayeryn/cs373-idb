from io import StringIO
from unittest import main, TestCase

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
        test_episode = {"name": "TestEpisode", "season": "3", "previous_episode": "TestPrevEp",
                        "next_episode": "TestNextEp", "characters": "Jon Snow, Benjen Stark, Eddard Stark"}
        
        ep = Episode(**test_episode)
        self.session.add(ep)
        result = self.session.query(Episode).filter(Episode.name == "TestEpisode").first()

        self.assertEqual(result.season, "3")
        self.assertEqual(result.next_episode, "TestNextEp")
		self.assertEqual(result.previous_episode, "TestPrevEp")
		self.assertEqual(result.characters, "Jon Snow, Benjen Stark, Eddard Stark")


	def test_episode_delete(self):
		test_episode = self.session.query(Episode).filter(Episode.name == "TestEpisode").first()
		self.session.delete(test_episode)

		test_episode = self.session.query(Episode).filter(Episode.name == "TestEpisode").first()
		self.assertEqual(test_episode, None)


    # -------
    # Houses
    # -------
	def test_house_insert(self):
        test_house = {"name": "TestHouse", "region": "Norf", "words": "DA KING OF DA NORF",
                        "current_lord": "TestLord", "heir": "TestHeir", "overlord" : "TestOverLord"}
        
        h = House(**test_house)
        self.session.add(h)
		result = self.session.query(House).filter(House.name == "TestHouse").first()

        self.assertEqual(result.region, "Norf")
        self.assertEqual(result.words, "DA KING OF DA NORF")
		self.assertEqual(result.current_lord, "TestLord")
		self.assertEqual(result.heir, "TestHeir")
		self.assertEqual(result.overlord, "TestOverLord")


	def test_house_delete(self):
		test_house = self.session.query(House).filter(House.name == "TestHouse").first()
		self.session.delete(test_house)

		test_house = self.session.query(House).filter(House.name == "TestHouse").first()
		self.assertEqual(test_house, None)

    # -----------
    # Characters
    # -----------

    def test_character_insert(self):
        test_character = {"name": "Kieran", "titles": "Lord of the Python Tests", "aliases": "-",
                        "father": "OOP", "mother": "JavaScript", "spouse" : "Madam Tests.py",
                        "allegiances" : "House Java, House HTMl, House CSS", "played_by" : "Himself"}
        
        c = Character(**test_character)
        self.session.add(c)
		result = self.session.query(Character).filter(Character.name == "Kieran").first()

        self.assertEqual(result.titles, "Lord of the Python Tests")
        self.assertEqual(result.aliases, "-")
		self.assertEqual(result.father, "OOP")
		self.assertEqual(result.mother, "JavaScript")
		self.assertEqual(result.spouse, "Madam Tests.py")
		self.assertEqual(result.allegiances, "House Java, House HTMl, House CSS")
		self.assertEqual(result.played_by, "Himself")


	def test_character_delete(self):
		test_character = self.session.query(Character).filter(Character.name == "Kieran").first()
		self.session.delete(test_character)

		test_character = self.session.query(Character).filter(Character.name == "Kieran").first()
		self.assertEqual(test_character, None)

# ----
# main
# ----

if __name__ == "__main__":
    main()
