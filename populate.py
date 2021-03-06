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
    r = requests.get("https://api.got.show/api/houses/", verify=False)
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
    updated_houses = models.House.query.all()
    for h in updated_houses:
        if not h.words:
            h.words = "-"
        if not h.current_lord:
            h.current_lord = "-"
        if not h.title:
            h.title = "-"
        if not h.overlord:
            h.overlord = "-"
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
        for char in values['characters']:
            c.characters.append(models.Character.query.filter(models.Character.name==char).first())
        db.session.add(c)
    db.session.commit()

def update_characters():
    updated_chars = models.Character.query.all()
    for c in updated_chars:
        if not c.titles:
            c.titles = "-"
        if not c.mother:
            c.mother = "-"
        if not c.father:
            c.father = "-"
        if not c.spouse:
            c.spouse = "-"
        if not c.house:
            c.house = "-"
        if not c.actor:
            c.actor = "-"
    db.session.commit()

# Making use of other team's API #

def get_ingredients():
    r = requests.get("http://inebri8.me/api/ingredients/all")
    data = json.loads(r.content)
    for i in data:
        n = models.Ingredient(name=i['name'])
        db.session.add(n)
    db.session.commit()

def get_recipes():
    r = requests.get("http://inebri8.me/api/recipes/all")
    data = json.loads(r.content)
    for c in data:
        p = models.Recipe(name=c['title'], link=c['link'], image=c['image'])
        for i in c['ingredients']:
            p.ingredients.append(models.Ingredient.query.filter(models.Ingredient.name==i['name']).first())
        db.session.add(p)
    db.session.commit()

def get_alc():
    r = requests.get("http://inebri8.me/api/alcohol/all")
    data = json.loads(r.content)
    for alc in data:
        a = models.Alcohol(name=alc['name'])
        for r in alc['recipes']:
            a.recipes.append(models.Recipe.query.filter(models.Recipe.name == r['title']).first())
        db.session.add(a)
    db.session.commit()

