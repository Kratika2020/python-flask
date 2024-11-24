# WEB-DEV with python (flask, rest-apis, docker)

---

## Python-Flask

- To install Flask --> pip install flask
- To run a python file --> python <file>.py
- To run flask app --> python -m flask run

- Topics introduced :
  [+] Blueprints and MethodViews
  code :
  from flask.views import MethodView
  from flask\*smorest import Blueprint, abort
  blp = Blueprint("stores", **name**, description="Operations on stores") //asteriks to be replaced with underscore
  //stores is the name of the file to be used
  @blp.route("/store/<string:store_id>")
  class Store(MethodView):
  def get(self, store_id):
  pass

---

## Docker

- To create a docker image --> docker build -t <name-of-image> .
  ----: The full stop reffers to same directory where work-directiory is declared

- To run the container of image --> docker run -d -p 3000:5000 <name-of-image>
  ----: -d stands for detached mode, -p stands for port exposing

- To kill a running image --> docker kill <id generated of the image>

- To get info of all the images --> docker ps -a
  ----: -a retreives all images

- docker-compose.yml is a file that has the services and allows multiple containers to run at the same time (network concept).
- to compose and start the container --> docker compose up
- to remove the container and newtork --> docker compose down

- Inorder to debug the flask app via docker, one can create docker-compose.debug.yml file. Then debug setup is required.

- for hot reloading while using docker
  --> docker run -dp 5000:5000 -w /app -v "/c/Users/Kratika/Desktop/python-flask:/app" <name-of-image>
  ----: -w --> working directory
  ----: -v --> mapping local directory to container's working directory via volumes
  \*\* also .flaskenv file is required
