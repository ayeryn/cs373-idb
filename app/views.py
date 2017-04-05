
from app import app as application, models, db
from flask import render_template

@application.route('/')
def index():
    return render_template('index.html')

@application.route('/about')
def about():
    return render_template('about.html')

@application.route('/characters')
def characters(page=1):
    characters = models.Character.query.paginate(page, 20, False)
    return render_template('characters.html', characters=characters)

@application.route('/characters/<name>', methods=['GET', 'POST'])
def character(name):
    character = models.Character.query.filter_by(name=name).first()
    return render_template('character.html', character=character)

@application.route('/houses')
def houses():
    houses = models.House.query.all()
    return render_template('houses.html', houses=houses)

@application.route('/houses/<name>', methods=['GET', 'POST'])
def house(name):
    house = models.House.query.filter_by(name=name).first()
    return render_template('house.html', house=house)

@application.route('/episodes')
def episodes():
    episodes = models.Episode.query.all()
    return render_template('episodes.html', episodes=episodes)

@application.route('/episodes/<name>', methods=['GET', 'POST'])
def episode(name):
    episode = models.Episode.query.filter_by(name=name).first()
    return render_template('episode.html', episode=episode)



