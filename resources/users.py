from flask import Flask, request
from flask.views import MethodView
from flask_smorest import Blueprint, abort 
import uuid
from db import users
from schemas import UserSchema, UserUpdateSchema

blp = Blueprint("users", __name__, description = "Operations on Users")

@blp.route("/user/<id>")
class User(MethodView) :
    def get(self,id) :
        try:
            return users[id], 201
        except KeyError:
            abort(404, message = 'No such user id exists')  
    
    @blp.arguments(UserUpdateSchema)
    def put(self,userdata,id) :
        try :
            users[id] = {**userdata, 'id':id}
            return "data updated - put", 201
        except KeyError :
            abort(404, message = 'No such user exists') 

    @blp.arguments(UserUpdateSchema)
    def patch(self,userdata,id) :
        try :
            data = {**userdata}
            if 'username' in data :
                users[id]['username'] = data['username']
            if 'password' in data :
                users[id]['password'] = data['password']
            return "data updated - patch", 201
        except KeyError :
            abort(404, message = 'No such user exists') 
    

    def delete(self,id) :
        try :
            del users[id]
            return "data deleted", 201
        except KeyError :
            abort(404, message = 'No such user id exists') 


@blp.route("/users")
class UsersList(MethodView) :
    def get(self) :
        return users

    @blp.arguments(UserSchema)
    def post(self,userdata) :
        new_id = uuid.uuid4().hex
        new_user_data = {**userdata, 'id' : new_id}
        users[new_id] = new_user_data
        return users[new_id], 201

    

