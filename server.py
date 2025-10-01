#!/usr/bin/env python

import base64
from cryptography import fernet
from aiohttp_session import setup, get_session
from aiohttp_session.cookie_storage import EncryptedCookieStorage
from aiohttp import web
import aiohttp_jinja2
import jinja2

from captcha import some_random_operation


@aiohttp_jinja2.template("index.html")
async def handle_home(request: web.Request):
    session = await get_session(request)
    c, session["response"] = some_random_operation(20)
    return {"captcha": c}


@aiohttp_jinja2.template("submit.html")
async def handle_submit(request: web.Request):
    session = await get_session(request)
    resp = session.get("response")
    data = await request.post()
    cap = data["captcha"]
    return {"msg": "Yes" if str(resp) == cap else "No"}


async def handle_api_challenge(request: web.Request):
    c, response = some_random_operation(20)
    return web.json_response(
        {
            "challenge": c,
            "secret": request.app["fernet"].encrypt(str(response).encode()).decode(),
        }
    )


async def handle_api_response(request: web.Request):
    p = await request.json()
    secret = int(request.app["fernet"].decrypt(p["secret"]))
    return web.json_response(p["response"] == secret)


app = web.Application()
app.add_routes(
    [
        web.get("/", handle_home),
        web.post("/submit", handle_submit),
        web.static("/assets", "./assets"),
        web.get("/api/challenge", handle_api_challenge),
        web.post("/api/response", handle_api_response),
    ]
)

aiohttp_jinja2.setup(app, loader=jinja2.FileSystemLoader("./templates"))

fernet_key = fernet.Fernet.generate_key()
secret_key = base64.urlsafe_b64decode(fernet_key)
app["fernet"] = fernet.Fernet(fernet_key)
setup(app, EncryptedCookieStorage(secret_key))

if __name__ == "__main__":
    web.run_app(app)
