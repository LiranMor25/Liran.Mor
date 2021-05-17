from flask import Flask, url_for, redirect
from flask import render_template

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST', 'DELETE', 'PUT'])
def hello_world():
    return render_template('cv.html')


@app.route('/contactList', methods=['GET', 'POST', 'DELETE', 'PUT'])
def hello_contact():
    return render_template('contactList.html')


@app.route('/assignment8', methods=['GET', 'POST', 'DELETE', 'PUT'])
def hello_assignment8():
    return render_template('assignment8.html',
                           user={'name': "Liran Mor"},
                           hobbies=['Football', 'Surfing', 'Snowboarding'])


if __name__ == '__main__':
    app.run(debug=True)
