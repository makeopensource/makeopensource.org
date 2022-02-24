from starlette.routing import Mount, Route
from starlette.staticfiles import StaticFiles

from views import main


routes=[
    Route('/', main.home),
    Route('/about', main.about),
    Route('/ledger', main.ledger),
    Route('/github', main.github),
    Route('/discord', main.discord),
    # Route('/projects', main.projects),
    Route('/announcements', main.announcements, methods=["GET", "POST"]),
    
    Mount('/static', StaticFiles(directory='static'), name='static'),
]

