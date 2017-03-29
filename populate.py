import json
import requests
from app import db, models

def get_characters():
	r = requests.get("https://api.got.show/api/characters/")
	data = json.loads(r.content)
	for character in data:
		c = models.Character(name=character['name'], 
							 house=character['house'], 
							 titles=character['titles'],
							 father=character['father'],
							 mother=character['mother'],
							 spouse=character['spouse'],
							 played_by=character['actor'])
		db.session.add(c)
		db.session.commit()
