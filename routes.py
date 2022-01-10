from starlette.routing import Mount, Route
from starlette.staticfiles import StaticFiles

from views.main import *


routes=[
    Route('/', home),

    Mount('/static', StaticFiles(directory='static'), name='static'),
]
