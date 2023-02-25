
# builds the pre-requisite materials needed for running
# the application
build: web annbot

# Start the server
up: build
	docker compose up -d --build

# Shut the server down
down:
	docker compose down

# Restart the server
restart: all
	docker compose restart

web: web/Dockerfile

annbot: annbot/Dockerfile

annbot/Dockerfile: annbot/
	git submodule init annbot
	git submodule update --recursive

clean:
	git submodule deinit --all -f

.PHONY:
	build up down restart web annbot clean
