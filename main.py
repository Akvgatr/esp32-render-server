from fastapi import FastAPI, WebSocket

app = FastAPI()


@app.get("/")
def home():
    return {
        "status": "online",
        "message": "ESP32 camera server is running"
    }


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()

    print("ESP32 connected")

    await websocket.send_json({
        "type": "connected",
        "message": "Hello from Render"
    })

    try:
        while True:
            message = await websocket.receive_text()
            print("ESP32:", message)

    except Exception:
        print("ESP32 disconnected")