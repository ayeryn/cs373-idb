from flask import Flask, render_template


application = Flask(__name__)

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
    return render_template('cersei_lannnister.html')

@application.route('/daenerystargaryen')
def daenerys_targaryen():
    return render_template('daenerys_targaryen.html')

@application.route('/houses')
def houses():
    return render_template('houses.html')

@application.route('/housestark')
def house_stark():
    return render_template('house_stark.html')

@application.route('/housetargaryen')
def house_targaryen():
    return render_template('house_targaryen.html')

@application.route('/houselannister')
def house_lannister():
    return render_template('house_lannister.html')

@application.route('/episodes')
def episodes():
    return render_template('episodes.html')

if __name__ == '__main__':
    application.run()
