from fastapi import FastAPI
from app.router.routes import initRoutes
from app.cors.cors import initCors

app = FastAPI(debug=True,title="Recipe API")
initCors(app)
initRoutes(app)
