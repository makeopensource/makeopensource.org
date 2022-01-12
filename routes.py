from starlette.routing import Mount, Route
from starlette.staticfiles import StaticFiles

from views import main


routes=[
    Route('/', main.home),
    Route('/about', main.about),
    Route('/projects', main.projects),
    Route('/announcements', main.announcements),

    Mount('/static', StaticFiles(directory='static'), name='static'),
]

