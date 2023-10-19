from fastapi import FastAPI

app = FastAPI(openapi_prefix="/imadapter")


@app.get("/")
def read_root():
    return {"Hello": "IMAdapter"}
