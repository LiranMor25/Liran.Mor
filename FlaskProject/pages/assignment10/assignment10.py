from flask import Flask, render_template, url_for, redirect, session, request, Blueprint, jsonify
import mysql.connector

assignment10 = Blueprint('assignment10', __name__, static_folder='static', static_url_path='/assignment10',
                         template_folder='templates')


#intataction with Data Base Function
def interact_db(query, query_type: str):
    return_value = False
    connection = mysql.connector.connect(host='localhost', user='root', passwd='root', database='web_dp', auth_plugin='mysql_native_password')
    cursor = connection.cursor(named_tuple=True)
    cursor.execute(query)

    if query_type == 'commit':
        # Use for INSERT, UPDATE, DELETE statement
        # returns: the number of rows affected by query
        connection.commit()
        return_value = True

    if query_type == 'fetch':
        # Use for SELECT statement
        # return: False if the query failed, or the result of the query if it succeeded
        query_result = cursor.fetchall()
        return_value = query_result

    connection.close()
    cursor.close()
    return return_value


# insert User to Data Base route and funcation
@assignment10.route('/insert_user', methods=['GET','POST'])
def insert_user():
    if request.method == 'POST':
        num_id = request.form['id']
        first_name = request.form['fname']
        last_name = request.form['lname']
        email = request.form['email']
        avatar = request.form['avatar']
        query = "INSERT into users (UserID, FirstName, LastName, UserEmail, avatar) VALUES ('%s', '%s', '%s', '%s','%s')" % (num_id, first_name, last_name, email, avatar)
        interact_db(query, 'commit')

    return redirect('/assignment10')


# Delete User to Data Base route and funcation
@assignment10.route('/delete_user', methods=['GET','POST'])
def delete_user():
    if request.method == 'POST':
        user_id = request.form['id']
        query = "DELETE FROM users WHERE UserID='%s';" % user_id
        interact_db(query, 'commit')

    return redirect('/assignment10')


# Update User Email by id route and function
@assignment10.route('/update_user')
def update_user():
    id_num = request.args['id']
    email = request.args['email']
    query = "UPDATE users SET UserEmail = '%s' WHERE UserID = '%s' " % (email, id_num)
    interact_db(query, query_type='commit')

    return redirect('/assignment10')


@assignment10.route('/assignment11')
@assignment10.route('/assignment11/users/')
def users():
    if request.method == 'GET':
        query = "select * from users;"
        query_result = interact_db(query, query_type='fetch')
        if len(query_result) == 0:
            return jsonify({'success': 'False', 'data':[]})
        else:
            return jsonify({'success': 'True', 'data':query_result})
    else:
        return render_template('assignment10.html')


@assignment10.route('/assignment11/users/selected/', defaults={'userId':3})
@assignment10.route('/assignment11/users/selected/<int:userId>')
def select_user(userId):
    query = "select * from users where UserID = '%s';" % userId
    query_result = interact_db(query, query_type='fetch')
    if len(query_result) == 0:
        return jsonify('Error User Not Exists!')
    else:
        return jsonify({'success': 'True', 'data':query_result[0]})