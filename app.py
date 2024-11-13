from flask import Flask, request

app = Flask(__name__)

users = [
            {'user': 'kratika',
             'data':{
                     'username' : 'kratika.saxena',
                     'password' : '123456'
                    }
            }
        ]

# ----- GET REQUESTS --------
# request type = GET

# To fetch all the users data
# endpoint = /users
@app.get('/users')
def get_users() :
    return users

# To fetch a particular user data
@app.get('/users/<string:name>')
def get_user_data(name):
    name = name.lower()
    for i in users :
        if i['user'] == name :
            return i, 201
    return "No such user exists", 404

# -------------------------

# ------ POST REQUESTS ------
# request type = POST
# POSTMAN : select 'Body' tab then click 'raw' 
#           change type from "Text" to "JSON"


# endpoint = /newuser
@app.post('/newuser')
def post_user():
    request_data = request.get_json()
    new_user = {'user' : request_data['user'],
                'data' : request_data['data']}
    users.append(new_user)
    return new_user, 201

# endpoint = /changepswd
@app.post('/changepswd/<string:name>')
def change_password(name) :
    request_data = request.get_json()
    for i in users :
        if i['user'] == name :
            i['data']['password'] = request_data['data']['password']
            return i, 201
    return "No such user exsits", 404
# -----------------------------------


# inorder to execute this enter -->
# python -m flask run