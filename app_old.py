from flask import Flask, request
from flask_smorest import abort
from db import users, uuid

app = Flask(__name__)


# ----- GET REQUESTS --------
# request type = GET

# To fetch all the users data
# endpoint = /users
@app.get('/users')
def get_users() :
    return users

# To fetch a particular user data
@app.get('/users/<id>')
def get_user_data(id):
    try:
        return users[id], 201
    except KeyError:
        abort(404, message = 'No such user id exists')     # using flask_smorest

# -------------------------

# ------ POST REQUESTS ------
# request type = POST
# POSTMAN : select 'Body' tab then click 'raw' 
#           change type from "Text" to "JSON"


# endpoint = /newuser
@app.post('/newuser')
def post_user():
    request_data = request.get_json()
    new_id = uuid.uuid4().hex
    new_user_data = {**request_data, 'id' : new_id}
    users[new_id] = new_user_data
    return users[new_id], 201

# --------- PUT REQUESTS ----------
# 
# endpoint = /changedata
@app.put('/changedata/<id>')
def change_data(id) :
    request_data = request.get_json()
    try :
        users[id] = {**request_data, 'id':id}
        return "data updated", 201
    except KeyError :
        abort(404, message = 'No such user exists')     # using flask_smorest
    except TypeError :
        abort(404, message = 'ERROR IN TYPE') 
# -----------------------------------

