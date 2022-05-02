from starlette.routing import Mount, Route
from starlette.staticfiles import StaticFiles

from views import main


routes=[
    Route('/', main.home),
    Route('/about', main.about),
    Route('/github', main.github),
    Route('/discord', main.discord),
    Route('/calendar', main.calendar),
    # Route('/projects', main.projects),
    Route('/announcements', main.announcements, methods=["GET", "POST"]),
    
    Mount('/static', StaticFiles(directory='static'), name='static'),
]

