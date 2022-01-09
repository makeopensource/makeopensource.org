# makeopensource.org rework
The HUB for all things MakeOpenSource, rewritten in starlette, a light python web 
framework with great asynchronous programming support.


## structure

* `server.py` – the main server component
* `routes.py` – definition of routes (aka urls) for requests
* `views/` – directory holding code apps (seperated by .py files)
* `.gitignore` – all files ignored by git


## run server
1. install starlette and uvicorn – `pip3 install -r requirements.txt`

2. run server – `uvicorn server:app`
