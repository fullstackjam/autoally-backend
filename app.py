# from predict_intent import get_intent_name
from dotenv import load_dotenv
from fastapi import FastAPI, Request
from slack_bolt import App
from slack_bolt.adapter.fastapi import SlackRequestHandler

load_dotenv()  # take environment variables from .env.
app = App()
app_handler = SlackRequestHandler(app)


replied_threads = set()


@app.event("app_mention")
def handle_app_mentions(body, say, logger):
    logger.info(body)
    message_text = body["event"]["text"]
    # return_message = get_intent_name(message_text)
    return_message = message_text
    logger.info(f"return message is {return_message}")
    thread_ts = body["event"].get("thread_ts") or body["event"].get("ts")

    # 在同一线程中回复并将 thread_ts 添加到 replied_threads set
    say(text=return_message, thread_ts=thread_ts)
    replied_threads.add(thread_ts)


@app.event("message")
def handle_message(body, say, logger):
    message_text = body["event"]["text"]
    return_message = message_text
    # return_message = get_intent_name(message_text)
    logger.info(f"return message is {return_message}")
    thread_ts = body["event"].get("thread_ts")

    # 检查消息是否是子消息（即线程中的消息）
    if (
        thread_ts
        and thread_ts != body["event"].get("ts")
        and thread_ts in replied_threads
    ):
        say(text=return_message, thread_ts=thread_ts)


@app.event("app_home_opened")
def handle_app_home_opened_events(body, logger):
    logger.info(body)


api = FastAPI()


@api.post("/slack/events")
async def endpoint(req: Request):
    return await app_handler.handle(req)


@api.get("/")
async def get():
    return {"application": "fastapi"}
