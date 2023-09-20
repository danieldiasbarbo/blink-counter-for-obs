from typing import Union
from face_recognition import recog
import threading

from fastapi import FastAPI, WebSocket
import asyncio
import json
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


websockets = set()


# Função para enviar atualizações para todos os clientes WebSocket conectados
async def send_updates():
    while True:
        if len(websockets) > 0:
            contador_atual = app.rec.contador
            update_message = json.dumps({"contador": contador_atual})
            await asyncio.gather(*[ws.send_text(update_message) for ws in websockets])
        await asyncio.sleep(0.1)


@app.websocket("/counter")
async def counter_websocket(websocket: WebSocket):
    # Aceitar a conexão WebSocket
    await websocket.accept()
    websockets.add(websocket)

    try:
        while True:
            # Esperar por mensagens do cliente (não é necessário neste exemplo)
            await websocket.receive_text()
    except:
        websockets.remove(websocket)
    finally:
        await websocket.close()


asyncio.create_task(send_updates())
