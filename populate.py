import json
import requests
from app import db, models

def theta_join(r, s, bp):
    return (dict(u, **v) for u in r for v in s if bp(u, v))

def get_characters():
	r = requests.get("https://api.got.show/api/characters/")
	data = json.loads(r.content)
    	attr = dict.fromkeys(dir(models.Character))
	for character in data:
                values = attr.copy()
                values.update(character)
                c = models.Character(name=values['name'],
                                    titles=', '.join(values['titles']), father=values['father'],
                                    mother=values['mother'], spouse=values['spouse'],
                                    house=values['house'], actor=values['actor'],
                                    imageLink=values['imageLink'])

		db.session.add(c)
		db.session.commit()

def get_houses():
    r = requests.get("https://api.got.show/api/houses/")
    data = json.loads(r.content)
    attr = dict.fromkeys(dir(models.House))
    for house in data:
                values = attr.copy()
                values.update(house)
                c = models.House(name=values['name'],
                                 region=values['region'], words=values['words'],
                                 current_lord=values['current_lord'], title=values['title'],
                                 overlord=values['overlord'], imageLink=values['imageLink'])

        	db.session.add(c)
        	db.session.commit()

def get_episodes():
    r = requests.get("https://api.got.show/api/episodes/")
    data = json.loads(r.content)
    attr = dict.fromkeys(dir(models.Episode))
    for episode in data:
                values = attr.copy()
                values.update(episode)
                c = models.Episode(name=values['name'],season=values['season'], predecessor=values['predecessor'],successor=values['successor'])
            	db.session.add(c)
            	db.session.commit()
