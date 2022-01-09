# makeopensource.org rework
The HUB for all things MakeOpenSource, rewritten in starlette, a light python web 
framework with great asynchronous programming support.


## structure

* `server.py` – the main server component
* `routes.py` – definition of routes (aka urls) for requests
* `views/` – holds request/response code (for apps, seperated by file)
* `db/` – stores db access functions (for apps, seperated by file)
* `.gitignore` – all files ignored by git


## run server
1. install starlette and uvicorn – `pip3 install -r requirements.txt`

2. run server – `uvicorn server:app`
