from flask import Flask, render_template


application = Flask(__name__)

@application.route('/')
def index():
    return render_template('index.html')

@application.route('/characters')
def characters():
    return render_template('characters.html')

@application.route('/houses')
def houses():
    return render_template('houses.html')

@application.route('/episodes')
def episodes():
    return render_template('episodes.html')

if __name__ == '__main__':
    application.run()
