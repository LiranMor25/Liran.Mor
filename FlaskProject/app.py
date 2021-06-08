from flask import Flask, url_for, redirect
from flask import render_template, request, session, blueprints

app = Flask(__name__)
app.secret_key = '123'

from pages.assignment10.assignment10 import assignment10
app.register_blueprint(assignment10)


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


@app.route('/assignment9', methods=['GET', 'POST', 'DELETE', 'PUT'])
def hello_assignment9():
    search, username, = '', ''
    curr_user = ({"id": 1, "email": "george.bluth@reqres.in", "first_name": "George", "last_name": "Bluth",
                  "avatar": "https://reqres.in/img/faces/1-image.jpg"},
                 {"id": 2, "email": "janet.weaver@reqres.in", "first_name": "Janet", "last_name": "Weaver",
                  "avatar": "https://reqres.in/img/faces/2-image.jpg"},
                 {"id": 3, "email": "emma.wong@reqres.in", "first_name": "Emma", "last_name": "Wong",
                  "avatar": "https://reqres.in/img/faces/3-image.jpg"},
                 {"id": 4, "email": "eve.holt@reqres.in", "first_name": "Eve", "last_name": "Holt",
                  "avatar": "https://reqres.in/img/faces/4-image.jpg"},
                 {"id": 5, "email": "charles.morris@reqres.in", "first_name": "Charles", "last_name": "Morris",
                  "avatar": "https://reqres.in/img/faces/5-image.jpg"},
                 {"id": 6, "email": "tracey.ramos@reqres.in", "first_name": "Tracey", "last_name": "Ramos",
                  "avatar": "https://reqres.in/img/faces/6-image.jpg"})
    current_method = request.method
    if current_method == 'GET':
        if 'searchfield' in request.args:
            search = request.args['searchfield']
            return render_template('assignment9.html', search=search, users=curr_user)

    if current_method == 'POST':
        username = request.form['nickname']
        session['logged_in'] = True
        session['username'] = username

    return render_template('assignment9.html', request_method=request.method, username=username)


@app.route('/assignment10', methods=['GET', 'POST', 'DELETE', 'PUT'])
def hello_assignment10():
    return render_template('assignment10.html')


@app.route('/log_out')
def log_out():
        session['logged_in'] = False
        return redirect(url_for('hello_assignment9'))


if __name__ == '__main__':
    app.run(debug=True)
