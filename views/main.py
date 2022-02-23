import yaml

from starlette.templating import Jinja2Templates


templates = Jinja2Templates(directory='templates')


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


async def ledger(request):
    elements = {
        'request': request, 
        'payments': get_yaml('ledger.yml', 'payments')
    }
    return templates.TemplateResponse('ledger.html', elements)

