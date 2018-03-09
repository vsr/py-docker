# A sample project for running a python process

## Creating docker image

`docker build -t py-docker .`

## Run the image

`docker run -it -e message="Hello World!" --rm --name py-docker-instance py-docker`