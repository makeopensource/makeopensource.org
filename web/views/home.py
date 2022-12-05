from starlette.templating import Jinja2Templates


templates = Jinja2Templates(directory='templates')


async def home(request):
    return templates.TemplateResponse('index.html', {'request': request})

