from starlette.routing import Route
from views import *

routes=[
    Route('/', homepage),
]
