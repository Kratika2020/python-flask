# WEB-DEV with python (flask, rest-apis, docker)

---

## Python-Flask

- To install Flask --> pip install flask
- To run a python file --> python <file>.py
- To run flask app --> python -m flask run

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
