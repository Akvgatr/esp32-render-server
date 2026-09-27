from fastapi import FastAPI, WebSocket, UploadFile, File

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


@app.post("/upload")
async def upload_image(file: UploadFile = File(...)):

    image_data = await file.read()

    print("Received image!")
    print("Filename:", file.filename)
    print("Size:", len(image_data), "bytes")
    print("Content type:", file.content_type)

    return {
        "status": "success",
        "message": "Image received",
        "size": len(image_data)
    }