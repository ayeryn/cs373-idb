from flask import Flask, render_template


application = Flask(__name__)

@application.route('/', methods=['GET', 'POST'])
@application.route('/index', methods=['GET', 'POST'])
def index():
    return render_template('about.html')

if __name__ == '__main__':
    application.run()
