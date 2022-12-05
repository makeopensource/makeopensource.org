from .jinja_filters import to_date, discordify
from starlette.responses import JSONResponse, HTMLResponse
from starlette.templating import Jinja2Templates


templates = Jinja2Templates(directory='templates')
filters = {'discordify': discordify}
templates.env.filters.update(filters)
templates.env.autoescape = False


async def announcements(request):
    if request.method == 'POST':
        body = await request.json()
        print(f"body: {body}")
        template = templates.get_template('announcements.html')
        rendered = template.render(announcements=body['messages'])
        with open('templates/.announcements.html', 'w') as file:
            file.write(rendered)
        return JSONResponse({'status': 200})
    else:
        try:
            with open('templates/.announcements.html', 'r') as file:
                return HTMLResponse(file.read())
        except FileNotFoundError:
            params = {'request': request, 'announcements': []}
            return templates.TemplateResponse('announcements.html', params)



