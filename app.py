import os

from fastapi import FastAPI

ROOT_PATH = os.environ.get("ROOT_PATH", "")

app = FastAPI(root_path=ROOT_PATH, openapi_url=f"{ROOT_PATH}/openapi.json")


@app.get("/")
def read_root():
    return {"Hello": "IMAdapter"}
