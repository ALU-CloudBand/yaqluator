# yaqluator
YAQLuator - an online YAQL evaluator

A free online evaluator for YAQL - A query language for querying YAML / JSON

The website is available online at [http://yaqluator.com/](http://yaqluator.com/).

![YAQLuator screenshot](https://github.com/ALU-CloudBand/yaqluator/blob/master/public_html/yaqluator_screenshot.jpg)

Created by Alcatel-Lucent Cloudband during a 24 hours Hackathon session

# Usage with Docker
To run YAQLuator locally using [Docker](https://www.docker.com/):
1. Ensure that you have Docker **and** [Docker Compose](https://docs.docker.com/compose/) installed. Follow the standard installation instructions for your platform. The Docker configuration has been tested on Linux (Ubuntu and CentOS), Mac OS X, and Windows 10.
2. Clone this repository to your machine.
```console
$ git clone https://github.com/ALU-CloudBand/yaqluator.git
```
3. Make the launch script, `docker_yaqluator.sh`, executable. On Windows, the preferred option is to use Git Bash which comes with [Git for Windows](https://gitforwindows.org/).
```console
$ chmod +x docker_yaqluator.sh
```
4. Run the launch script, `docker_yaqluator.sh`, to download Docker image files, configure the environment, and run YAQLuator. Downloading the [Docker image](https://phoenixnap.com/kb/docker-image-vs-container) files may take several minutes the first time that you run the script; please be patient. On subsequent runs, Docker will use the cached images, so startup time will be much shorter.
```console
$ ./docker_yaqluator.sh
```
5. Open your web brower to [`http://localhost/`](http://localhost/). If everything goes smoothly, the YAQLuator main page will be displayed.

If the standard HTTP port (port **80**) is already in use on your system, you can specify a different [port](http://www.steves-internet-guide.com/tcpip-ports-sockets/) to use by setting the `YAQLUATOR_HTTP_PORT` environment variable to the desired port, such as 8080, in the provided `.env` environment configuration file. Remember to indicate this port in the web browser URL, for example [`http://localhost:8080/`](http://localhost:8080/).
