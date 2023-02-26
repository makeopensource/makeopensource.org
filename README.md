# makeopensource.org

This repo contains all content and programs for makeopensource.org. 

Web content is stored in `web/data` and `web/templates`. The announcement
bot is in `annbot/`.

## Prerequisites

* Git
* Docker/Docker-Compose

## Setup/Configuration

1. To begin, run `$ make` to configure the submodules.

2. Open `annbot/.env`, and enter a discord bot token, and the id of the 
announcements channel in their respective places (in between the quotes).

3. Open `docker-compose.yml` to configure both the host and port for the
   applications.

## Run

Run `$ make up` to build the docker container and run it. See `Makefile` for
additional commands for controlling the composed container set.
