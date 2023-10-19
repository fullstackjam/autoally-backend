import os

from fastapi import FastAPI, Request
from slack_bolt import App
from slack_bolt.adapter.fastapi import SlackRequestHandler

app = App()
app_handler = SlackRequestHandler(app)


@app.event("app_mention")
def handle_app_mentions(body, say, logger):
    logger.info(body)
    say("What's up?")


@app.event("message")
def handle_message():
    pass


ROOT_PATH = os.environ.get("ROOT_PATH", "")

api = FastAPI(root_path=ROOT_PATH, openapi_url=f"{ROOT_PATH}/openapi.json")


@api.post("/slack/events")
async def endpoint(req: Request):
    # Transform the body to a dict
    body = await req.json()

    # Check if it's a URL verification challenge
    if body.get("type") == "url_verification":
        return {"challenge": body.get("challenge")}

    # Else, handle other events
    return await app_handler.handle(req)
