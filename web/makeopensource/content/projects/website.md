---
name: MakeOpenSource.org
slug: website
description: You're looking at it right now! The official website for MakeOpenSource.org, the University at Buffalo's 
  open-source software development student club. Built with Flask and Docker, it serves as a hub for club information 
  and project showcases.
github_url: https://github.com/makeopensource/makeopensource.org
---

## Project Structure

The `proxy` directory contains the Nginx configuration.

The main web application is in the `web/makeopensource` directory.

The application is segmented into Flask blueprints for organization, such as "general" and "projects". Each blueprint
should have its own directory.

HTML templates go into subdirectories of the `templates` directory. Most pages should extend `layouts/main_layout.html`,
and you should specify the `title` and `description` blocks for SEO.

Static assets, such as CSS, JavaScript, and images, go into the relevent subdirectory in the `static` directory. During
development, the Flask development server will automatically serve these. In production, Nginx will serve these.

The application starts running in `app.py`. This file registers the blueprints for routing.

## Local Development

### Initial Setup

You'll only need to follow these steps once.

* Install Python 3.14 or newer (older versions may work too)
* Create a Python virtual environment in the project's top-level directory. Your IDE can probably do this for you.
    * To manually do this, run `python3 -m venv .venv`, and activate it with `source .venv/bin/activate` (on
      macOS/Linux)
      or `.venv\Scripts\activate.bat` (on Windows).
* Install the dependencies within the virtual environment with `python3 -m pip install -r web/requirements.txt`. You
  should see the "(.venv)" prefix in your terminal to verify the virtual environment is active before running this.

### Running the Development Server

The development server provides a convenient preview of the application. It automatically reloads as changes are made to
the code, so you don't have to restart it. It also runs in debug mode, which provides detailed error details in your
browser.

* Run `web/makeopensource/app.py`
* Connect to the Flask development web server in your browser at http://localhost:5877

(Fun fact: port 5877 isn't random; it's the first four digits of the SHA-256 hash of "makeopensource" expressed in
base-10.)

## Docker Development

Docker is a containerization platform that allows you to run software in an identical environment across different
computers. If you can run the application in Docker on your computer, we should be able to run it on the production
server too.

Our Docker configuration runs the web application with a production-grade [Gunicorn](https://gunicorn.org/) server
sitting behind an [Nginx](https://nginx.org/) reverse proxy. Nginx serves static assets much more efficiently than
Python can.

If you're updating application infrastructure/dependencies, you **must** test your changes in Docker!

* Prerequisite: [Install Docker Engine](https://docs.docker.com/engine/install/)
* Run `docker compose up --build -d` anywhere within the project directory
    * Re-run this command every time you want to see your changes
* Connect to the Nginx proxy container in your browser at http://localhost:5878
    * This is one port higher than the development server port so you can run both simultaneously. Ensure you're
      connected to the one you expect&mdash;live changes will not apply to the Docker one.

### Useful Commands and Troubleshooting

* `docker compose up --build -d` is the recommended startup command
    * `up` starts all services (you can append service names start specific ones)
    * `--build` rebuilds images if their configurations (Dockerfiles) were updated
    * `-d` runs in detached mode, so it'll run in the background instead of locking your terminal
    * You can also use `--force-recreate` if an update isn't applying; this rebuilds the container even if Docker thinks
      its configuration hasn't changed
* `docker compose ps` will show the status of currently running containers for the project
* `docker compose logs` will show logs from all project containers; add `-f` to "follow" the logs in real-time; append a
  service name to filter to a particular service
* `docker compose restart` will restart all the containers; append a service name to restart a specific one
* `docker compose down` will shut down all the containers; append a service name to stop a specific one
* Nginx logs are stored in the `data/proxy-logs` directory