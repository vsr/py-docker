# A sample proof of concept project for running a python process on a docker container

## Creating docker image

`docker build -t py-docker .`

## Run the image

`docker run -it -e message="Hello World!" --rm --name py-docker-instance py-docker`