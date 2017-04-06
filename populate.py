import json
import requests
from app import db, models
import anapioficeandfire

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
    api = anapioficeandfire.API()
    apihouses = []
    for x in range(1,45):
        apihouses += api.get_houses(page=x)
    for house in data:
        values = attr.copy()
        values.update(house)
        c = models.House(name=values['name'],
                         region=values['region'], words=values['words'],
                         current_lord=values['current_lord'], title=values['title'],
                         overlord=values['overlord'], imageLink=values['imageLink'])
        db.session.add(c)
    apinames = []
    for a in apihouses:
        apinames += [a.name]
    names = []
    for h in data:
        names += [h['name']]
    snames = set(names)
    sapinames = set(apinames)
    intersection = snames.intersection(sapinames)
    house_data = models.House.query.all()
    for ho in house_data:
        if ho.name in intersection:
            apiHo = api.get_houses(name=ho.name)[0]
            if not ho.region and apiHo.region:
                ho.region = apiHo.region
            if not ho.current_lord and apiHo.currentLord:
                req = requests.get(apiHo.currentLord)
                dat = json.loads(req.content)
                ho.current_lord = dat['name']
            if not ho.title and apiHo.titles:
                ho.title = str(apiHo.titles)
            if not ho.overlord and apiHo.overlord:
                ho.overlord = str(apiHo.overlord)
    db.session.commit()

    
    

def get_episodes():
    r = requests.get("https://api.got.show/api/episodes/")
    data = json.loads(r.content)
    attr = dict.fromkeys(dir(models.Episode))
    for episode in data:
        values = attr.copy()
        values.update(episode)
        episode_number = episode['nr']
        url = "http://api.tvmaze.com/shows/82/episodebynumber?season=" + str(values['season']) + "&number=" + str(episode_number)
        episode_r = requests.get(url)
        episode_data = json.loads(episode_r.content)
        if not 'image' in episode_data:
            episode_data['image'] = {'medium': None}
        c = models.Episode(name=values['name'],season=values['season'], nr=values['nr'], 
                           predecessor=values['predecessor'],successor=values['successor'],
                           imageLink = episode_data['image']['medium'])
        db.session.add(c)
        db.session.commit()


