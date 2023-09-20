from typing import Union
from face_recognition import recog
import threading

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.counter = 0
app.rec = recog()


def thread_reco():
    app.rec.run()


x = threading.Thread(target=thread_reco)
x.start()


@app.get("/")
def read_root():
    return {"Welcome to conta pisca. Made by Alexandres e Daniels"}


@app.get("/blink_counter")
def read_blink_counter():
    app.counter += 1
    return {"blink_counter": f"{app.rec.contador}"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
