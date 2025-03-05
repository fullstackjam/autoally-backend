from dotenv import load_dotenv
from fastapi import FastAPI, Request
from slack_bolt import App
from slack_bolt.adapter.fastapi import SlackRequestHandler

load_dotenv()  # Load environment variables from .env.
app = App()
app_handler = SlackRequestHandler(app)

@app.event("message")
def handle_message(body, say, logger):
    logger.info(body)
    message_text = body["event"]["text"]
    return_message = message_text  # reply same message
    logger.info(f"Return message is: {return_message}")
    thread_ts = body["event"].get("thread_ts") or body["event"].get("ts")

    say(text=return_message, thread_ts=thread_ts)

@app.event("app_home_opened")
def handle_app_home_opened_events(body, logger):
    logger.info(body)

api = FastAPI()

@api.post("/slack/events")
async def endpoint(req: Request):
    return await app_handler.handle(req)

@api.get("/")
def get():
    return {"application": "fastapi"}
