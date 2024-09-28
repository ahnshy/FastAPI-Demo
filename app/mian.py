from dataclasses import asdict

import uvicorn
from fastapi import FastAPI

from app.database.connect import db
from app.src.config import conf
from app.router import index

def create_app():
    c = conf()
    app = FastAPI()
    conf_dict = asdict(c)
    db.init_app(app, **conf_dict)

    # to do initialize database
    # to do redis
    # to do define middle-ware, router ...etc

    app.include_router(index.router)
    return app

app = create_app()

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=conf().PROJ_RELOAD)