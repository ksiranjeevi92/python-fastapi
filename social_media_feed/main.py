from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from typing import List

class Notification(BaseModel):
    author: str
    description: str

class User(BaseException):
    name: str
    username: str
    email: str
    birthday: str
    friends: str
    notifications: List[Notification]

class UserDB(User):
    hashed_password: str

app = FastAPI()

templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
def root(request: Request):
    return templates.TemplateResponse("index.html", {"request" : request, "title": "FriendsConnect - Home"})