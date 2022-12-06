from .jinja_filters import discordify
from starlette.responses import JSONResponse, HTMLResponse
from starlette.templating import Jinja2Templates


templates = Jinja2Templates(directory='templates')
filters = {'discordify': discordify}
templates.env.globals.update(discordify=discordify)
templates.env.autoescape = False


cached_file = 'templates/.announcements.html'


async def announcements(request):
    if request.method == 'POST':
        body = await request.json()
        template = templates.get_template('announcements.html')
        print(body['channels'])
        rendered = template.render(announcements=body['messages'], channels=body['channels'])
        with open(cached_file, 'w') as file:
            file.write(rendered)
        return JSONResponse({'status': 200})
    else:
        try:
            with open(cached_file, 'r') as file:
                return HTMLResponse(file.read())
        except FileNotFoundError:
            params = {'request': request, 'announcements': [], "channels": []}
            return templates.TemplateResponse('announcements.html', params)



