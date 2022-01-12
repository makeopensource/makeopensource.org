from starlette.applications import Starlette
from routes import routes


app = Starlette(debug=True, routes=routes)

