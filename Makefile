
# builds the pre-requisite materials needed for running
# the application
build: web annbot

# Start the server
up: all
	docker compose up -d --build

# Shut the server down
down:
	docker compose down

# Restart the server
restart: all
	docker compose restart

web: web/Dockerfile

annbot:
	git submodule update --recursive
	git submodule sync --recursive

.PHONY:
	build up down restart web annbot
