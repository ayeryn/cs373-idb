
from app import app as application, models, db
from flask import render_template

@application.route('/')
def index():
    return render_template('index.html')

@application.route('/about')
def about():
    return render_template('about.html')

@application.route('/characters')
def characters():
    characters = models.Character.query.all()
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
    return render_template('episodes.html')

@application.route('/s1e1')
def s1e1():
    return render_template('episodes1e1.html')

@application.route('/s1e2')
def s1e2():
    return render_template('episodes1e2.html')

@application.route('/s1e3')
def s1e3():
    return render_template('episodes1e3.html')

