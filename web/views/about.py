import yaml
from .jinja_filters import to_date
from starlette.templating import Jinja2Templates


templates = Jinja2Templates(directory='templates')
filters = {'to_date': to_date}
templates.env.filters.update(filters)


async def about(request):
    elements = {
        'request': request, 
        'software': await get_yaml('data/about.yml', 'software'), 
        'admins': await get_yaml('data/about.yml', 'admins')
    }
    return templates.TemplateResponse('about.html', elements)


async def get_yaml(yaml_file, attr):
    with open(f'{yaml_file}', 'r') as file:
        return yaml.safe_load(file)[attr]

