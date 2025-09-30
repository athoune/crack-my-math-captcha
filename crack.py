import base64
from cryptography import fernet
from aiohttp_session import setup, get_session, session_middleware
from aiohttp_session.cookie_storage import EncryptedCookieStorage
from aiohttp import web
import aiohttp_jinja2
import jinja2

from captcha import some_random_operation


@aiohttp_jinja2.template("index.html")
async def handle_home(request):
    session = await get_session(request)
    c, session["response"] = some_random_operation(20)
    return {"captcha": c}


@aiohttp_jinja2.template("submit.html")
async def handle_submit(request):
    session = await get_session(request)
    resp = session.get("response")
    data = await request.post()
    cap = data["captcha"]
    return {"msg": "Yes" if str(resp) == cap else "No"}


app = web.Application()
app.add_routes([web.get("/", handle_home), web.post("/submit", handle_submit)])
aiohttp_jinja2.setup(app, loader=jinja2.FileSystemLoader("./templates"))
fernet_key = fernet.Fernet.generate_key()
secret_key = base64.urlsafe_b64decode(fernet_key)
setup(app, EncryptedCookieStorage(secret_key))

if __name__ == "__main__":
    web.run_app(app)
