# makeopensource.org rework
The HUB for all things MakeOpenSource, rewritten in starlette, a light python web 
framework with great asynchronous programming support.


## structure

* `server.py` – the main server component
* `routes.py` – definition of routes (aka urls) for requests
* `/views` – holds request/response code (for apps, seperated by file)
* `/db` – stores db access functions (for apps, seperated by file)
* `/templates` – stores all html templates
* `/static` – stores all static files
* `.gitignore` – all files ignored by git


## run server
*before you continue, [install docker](https://docs.docker.com/get-docker/) for
your local machine*
```
$ docker-compose up --build
```

## test environment
1. install requirements
```
$ pip install -r requirements.txt
```

2. run server
```
uvicorn server:app
```
