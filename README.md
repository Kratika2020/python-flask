# WEB-DEV with python (flask, rest-apis, docker)

---

## Python-Flask

- To install Flask --> pip install flask
- To run a python file --> python <file>.py

---

## Docker

- To create a docker image --> docker build -t <name-of-image> .
  ----: The full stop reffers to same directory where work-directiory is declared

- To run the container of image --> docker run -d -p 3000:5000 <name-of-image>
  ----: -d stands for detached mode, -p stands for port exposing

- To kill a running image --> docker kill <id generated of the image>

- To get info of all the images --> docker ps -a
  ----: -a retreives all images
