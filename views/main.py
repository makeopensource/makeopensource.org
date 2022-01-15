import json

from starlette.responses import JSONResponse, RedirectResponse
from starlette.templating import Jinja2Templates
from starlette.staticfiles import StaticFiles
import requests
from starlette.responses import FileResponse

from db.projects import get_project, create_project


templates = Jinja2Templates(directory='templates')

#flag variable for cache announcements
global updateAnnCache
updateAnnCache = False


async def home(request):
    return templates.TemplateResponse('index.html', {'request': request})


async def about(request):
    with open('static/json/about.json', 'r') as f:
        data = json.loads(f.read())
        elements = {
            'request': request, 
            'software': data['software'], 
            'admins': data['admins']
        }
        return templates.TemplateResponse('about.html', elements)


async def projects(request):
    org = requests.get('https://api.github.com/orgs/MakeOpenSource')
    assert org.status_code == 200

    repos_url = org.json()['repos_url']
    repos = requests.get(repos_url)
    assert repos.status_code == 200

    projects = []
    for project in repos.json():
        name = project['name']
        description = project['description']
        url = project['html_url']
        stars = project['stargazers_count']
        forks = project['forks_count']
        contributors = requests.get(project['contributors_url'])

        projects.append({
            'name': name,
            'description': description,
            'url': url,
            'stars': stars,
            'forks': forks,
            'collaborators': [c['login'] for c in contributors.json()]
        })

    return templates.TemplateResponse('projects.html', {'request': request, 'projects': projects})

    



async def announcements(request):
    if request.method == 'GET':
        if not updateAnnCache:
            response = FileResponse('static/annCache.html')
            return response
        else:
            sendAnn = []
            f = open("annCache.html", 'w')
            f.write(templates.TemplateResponse('announcements', {'request': request, 'announcements': sendAnn}))
            response = FileResponse('static/annCache.html')
            return response