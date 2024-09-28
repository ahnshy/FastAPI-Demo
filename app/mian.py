import uvicorn
from fastapi import FastAPI

from app.src.config import conf

def create_app():
    app = FastAPI()
    return app

    # to do initialize database
    # to do redis
    # to do define middle-ware, router ...etc

app = create_app()

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=conf().PROJ_RELOAD)