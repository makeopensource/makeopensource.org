import yaml
from .jinja_filters import to_date, discordify

from starlette.responses import JSONResponse, RedirectResponse, HTMLResponse
from starlette.templating import Jinja2Templates


templates = Jinja2Templates(directory='templates')
filters = {'to_date': to_date, 'discordify': discordify}
templates.env.filters.update(filters)
templates.env.autoescape = False

def get_yaml(yaml_file, attr):
    yaml_path = 'static/yaml'
    try:
        with open(f'{yaml_path}/{yaml_file}', 'r') as file:
            return yaml.safe_load(file)[attr]
    except FileNotFoundError:
        return {}


async def home(request):
    return templates.TemplateResponse('index.html', {'request': request})


async def about(request):
    print(get_yaml('about.yml', 'software'))
    elements = {
        'request': request, 
        'software': get_yaml('about.yml', 'software'), 
        'admins': get_yaml('about.yml', 'admins')
    }
    return templates.TemplateResponse('about.html', elements)


async def announcements(request):
    if request.method == 'POST':

        # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        # !!! make sure that the host and port !!!
        # !!! are verified before accepting    !!!
        # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

        body = await request.json()
        template = templates.get_template('announcements.html')
        rendered = template.render(announcements=body['messages'])
        with open('announcements.html', 'w') as file:
            file.write(rendered)
        return JSONResponse({'status': 200})
    else:
        with open('announcements.html', 'r') as file:
            return HTMLResponse(file.read())


async def ledger(request):
    elements = {
        'request': request, 
        'payments': get_yaml('ledger.yml', 'payments')
    }
    return templates.TemplateResponse('ledger.html', elements)


async def github(request):
    return RedirectResponse(url='https://github.com/makeopensource')


async def discord(request):
    return RedirectResponse(url='https://discord.com/invite/xbBPqdqr6n')

