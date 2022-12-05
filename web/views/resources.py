from starlette.templating import Jinja2Templates
from starlette.responses import RedirectResponse


templates = Jinja2Templates(directory='templates')


# calendar of recent club events
async def calendar(request):
    return templates.TemplateResponse('calendar.html', {'request': request})


# github (or future remote git host) for projects
async def github(request):
    return RedirectResponse(url='https://github.com/makeopensource')


# chat application
async def matrix(request):
    return RedirectResponse(url="https://matrix.to/#/#tech-space:matrix.makeopensource.org")


# alternative chat application (may be deprecated soon)
async def discord(request):
    return RedirectResponse(url='https://discord.com/invite/xbBPqdqr6n')

