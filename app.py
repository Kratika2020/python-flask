from flask import Flask, request

app = Flask(__name__)

users = [{ 'Username' : 'kratika.saxena'}]

# ----- GET REQUESTS --------

# request type = GET
# endpoint = /users
@app.get('/users')
def get_user() :
    return users
# -------------------------

# ------ POST REQUESTS ------
# POSTMAN : select 'Body' tab then click 'raw' 
#           change type from "Text" to "JSON"

# request type = POST
# endpoint = /users
@app.post('/newuser')
def post_user():
    request_data = request.get_json()
    new_user = {'Username' : request_data['Username']}
    users.append(new_user)
    return new_user, 201
# -----------------------------------


# inorder to execute this enter -->
# python -m flask run