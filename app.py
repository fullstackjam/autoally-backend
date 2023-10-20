import os

from fastapi import FastAPI, Request
from slack_bolt import App
from slack_bolt.adapter.fastapi import SlackRequestHandler

app = App()
app_handler = SlackRequestHandler(app)


replied_threads = set()


@app.event("app_mention")
def handle_app_mentions(body, say, logger):
    logger.info(body)
    message_text = body["event"]["text"]
    thread_ts = body["event"].get("thread_ts") or body["event"].get("ts")

    # 在同一线程中回复并将 thread_ts 添加到 replied_threads set
    say(text=message_text, thread_ts=thread_ts)
    replied_threads.add(thread_ts)


@app.event("message")
def handle_message(body, say, logger):
    message_text = body["event"]["text"]
    thread_ts = body["event"].get("thread_ts")

    # 检查消息是否是子消息（即线程中的消息）
    if (
        thread_ts
        and thread_ts != body["event"].get("ts")
        and thread_ts in replied_threads
    ):
        say(text=message_text, thread_ts=thread_ts)


@app.event("app_home_opened")
def handle_app_home_opened_events(body, logger):
    logger.info(body)


ROOT_PATH = os.environ.get("ROOT_PATH", "")

api = FastAPI(root_path=ROOT_PATH, openapi_url=f"{ROOT_PATH}/openapi.json")


@api.post("/slack/events")
async def endpoint(req: Request):
    return await app_handler.handle(req)
