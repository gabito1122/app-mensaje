from fastapi import FastAPI, WebSocket
from app.routers import users, messages
from app.websocket import websocket_endpoint
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Configura CORS para permitir peticiones desde tu frontend (ajusta dominios)
origins = [
    "http://localhost",
    "http://localhost:3000",  # Si usas React o similar en local
    # Agrega dominios de producción aquí
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Incluye routers de usuarios y mensajes
app.include_router(users.router)
app.include_router(messages.router)

# Ruta WebSocket para chat en tiempo real
@app.websocket("/ws/{user_id}")
async def websocket_route(websocket: WebSocket, user_id: int):
    await websocket_endpoint(websocket, user_id)

# Ruta raíz para probar que el backend está corriendo
@app.get("/")
def root():
    return {"message": "Backend FastAPI para chat funcionando"}
