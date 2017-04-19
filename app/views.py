
from app import app as application, models, db
from flask import render_template, jsonify
from flask_cors import CORS, cross_origin
import os

CORS(application)

@application.route('/')
def index():
    return render_template('index.html')

@application.route('/about')
def about():
    return render_template('about.html')

@application.route('/test')
def test():
    os.system('python runTests.py')
    return render_template('test.html')

@application.route('/inebriate')
def inebriate():
    return render_template('inebriate.html')

@application.route('/characters', methods=['GET', 'POST'])
@application.route('/characters/<int:page>', methods=['GET', 'POST'])
def characters(page=1):
    characters = models.Character.query.paginate(page, 17, False)
    return render_template('characters.html', characters=characters)

@application.route('/characters/<name>', methods=['GET', 'POST'])
def character(name):
    character = models.Character.query.filter_by(name=name).first()
    return render_template('character.html', character=character)

@application.route('/houses', methods=['GET', 'POST'])
@application.route('/houses/<int:page>', methods=['GET', 'POST'])
def houses(page=1):
    houses = models.House.query.paginate(page, 17, False)
    return render_template('houses.html', houses=houses)

@application.route('/houses/<name>', methods=['GET', 'POST'])
def house(name):
    house = models.House.query.filter_by(name=name).first()
    return render_template('house.html', house=house)

@application.route('/episodes', methods=['GET', 'POST'])
@application.route('/episodes/<int:page>', methods=['GET', 'POST'])
def episodes(page=1):
    episodes = models.Episode.query.paginate(page, 17, False)
    return render_template('episodes.html', episodes=episodes)

@application.route('/episodes/<name>', methods=['GET', 'POST'])
def episode(name):
    episode = models.Episode.query.filter_by(name=name).first()
    return render_template('episode.html', episode=episode)

@application.route('/api',methods=['GET'])
def api():
    redirect = "Check out https://app.apiary.io/swegot1 for supported API requests!"
    return jsonify({'hello': redirect})

@application.route('/api/episodes', methods=['GET'])
def api_episodes():
    episods = models.Episode.query.all()
    return jsonify(episodes=[i.serialize for i in episods])

@application.route('/api/houses', methods=['GET'])
def api_houses():
    hos = models.House.query.all()
    return jsonify(houses=[i.serialize for i in hos])

@application.route('/api/characters', methods=['GET'])
def api_characters():
    chars = models.Character.query.all()
    return jsonify(characters=[i.serialize for i in chars])

@application.route('/api/episodes/<name>', methods=['GET', 'POST'])
def api_episode(name):
    ep = models.Episode.query.filter_by(name=name).first()
    return jsonify(episode=ep.serialize)

@application.route('/api/characters/<name>', methods=['GET', 'POST'])
def api_character(name):
    ep = models.Character.query.filter_by(name=name).first()
    return jsonify(character=ep.serialize)

@application.route('/api/houses/<name>', methods=['GET', 'POST'])
def api_house(name):
    ep = models.House.query.filter_by(name=name).first()
    return jsonify(house=ep.serialize)

