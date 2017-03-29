
from app import app as application
from flask import render_template


@application.route('/')
def index():
    return render_template('index.html')

@application.route('/about')
def about():
    return render_template('about.html')

@application.route('/characters')
def characters():
    return render_template('characters.html')

@application.route('/jonsnow')
def jon_snow():
    return render_template('jon_snow.html')

@application.route('/cerseilannister')
def cersei_lannister():
    return render_template('cersei_lannister.html')

@application.route('/tommenbaratheon')
def tommen_baratheon():
    return render_template('tommen_baratheon.html')

@application.route('/houses')
def houses():
    return render_template('houses.html')

@application.route('/housestark')
def house_stark():
    return render_template('house_stark.html')

@application.route('/housebaratheon')
def house_baratheon():
    return render_template('house_baratheon.html')

@application.route('/houselannister')
def house_lannister():
    return render_template('house_lannister.html')

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

