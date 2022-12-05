from starlette.routing import Mount, Route
from starlette.staticfiles import StaticFiles

from views import home, about, github, matrix, discord, calendar, announcements


routes=[
    Route('/', home),
    Route('/about', about),
    Route('/github', github),
    Route('/discord', discord),
    Route('/matrix', matrix),
    Route('/calendar', calendar),
    # Route('/projects', projects),
    Route('/announcements', announcements, methods=["GET", "POST"]),
    
    Mount('/static', StaticFiles(directory='static'), name='static'),
    Mount('/data', StaticFiles(directory='data'), name='data'),
    Mount('/assets', StaticFiles(directory='static/assets'), name='assets'),
]

