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
        episode_dict = {"name": "TestEpisode", "season": "3", "previous_episode": "TestPrevEp",
                        "next_episode": "TestNextEp", "characters": "Jon Snow, Benjen Stark, Eddard Stark"}
        
        ep = Episode(**episode_dict)
        self.session.add(ep)

        result = self.session.query(Episode).filter(Episode.name == "TestEpisode").first()
        self.assertEqual(result.season, "3")
        self.assertEqual(result.next_episode, "TestNextEp")
		self.assertEqual(result.previous_episode, "TestPrevEp")
		self.assertEqual(result.characters, "Jon Snow, Benjen Stark, Eddard Stark")


    # -------
    # Houses
    # -------
	def test_house_insert(self):
        house_dict = {"name": "TestHouse", "region": "Norf", "words": "DA KING OF DA NORF",
                        "current_lord": "TestLord", "heir": "TestHeir", "overlord" : "TestOverLord"}
        
        h = House(**house_dict)
        self.session.add(h)

        result = self.session.query(House).filter(House.name == "TestHouse").first()
        self.assertEqual(result.region, "Norf")
        self.assertEqual(result.words, "DA KING OF DA NORF")
		self.assertEqual(result.current_lord, "TestLord")
		self.assertEqual(result.heir, "TestHeir")
		self.assertEqual(result.overlord, "TestOverLord")


    # -----------
    # Characters
    # -----------

    def test_character_insert(self):
        character_dict = {"name": "Kieran", "titles": "Lord of the Python Tests", "aliases": "-",
                        "father": "OOP", "mother": "JavaScript", "spouse" : "Madam Tests.py",
                        "allegiances" : "House Java, House HTMl, House CSS", "played_by" : "Himself"}
        
        c = Character(**character_dict)
        self.session.add(c)

        result = self.session.query(Character).filter(Character.name == "Kieran").first()
        self.assertEqual(result.titles, "Lord of the Python Tests")
        self.assertEqual(result.aliases, "-")
		self.assertEqual(result.father, "OOP")
		self.assertEqual(result.mother, "JavaScript")
		self.assertEqual(result.spouse, "Madam Tests.py")
		self.assertEqual(result.allegiances, "House Java, House HTMl, House CSS")
		self.assertEqual(result.played_by, "Himself")


# ----
# main
# ----

if __name__ == "__main__":
    main()
