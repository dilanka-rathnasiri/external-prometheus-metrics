# Simple Web Server

* A simple web server written in Python Fast API
* This image is only for testing
* The server port can be passed as an environment variable
* If the server port isn't specified, 3000 will be used as the server port

#### Pull Docker Image

```shell
docker pull dilankarathnasiri/simple-web-server:latest
```

#### Run Docker Image

```shell
docker run -p {{server port}}:{{server port}} --name {{docker container name}} --env SERVER_PORT={{server port}} dilankarathnasiri/simple-web-server:latest
```

e.g.,

```shell
docker run -p 5000:5000 --name web-server-container --env SERVER_PORT=5000 dilankarathnasiri/simple-web-server:latest
```
