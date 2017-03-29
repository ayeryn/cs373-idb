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
                                    house=values['house'], actor=values['actor'])

		db.session.add(c)
		db.session.commit()
