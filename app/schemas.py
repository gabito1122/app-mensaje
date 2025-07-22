from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

# Esquema base para usuario (campos comunes)
class UserBase(BaseModel):
    email: EmailStr
    full_name: Optional[str] = None

# Esquema para crear usuario (registro)
class UserCreate(UserBase):
    password: str  # Contraseña que el usuario enviará (sin encriptar)

# Esquema para devolver datos de usuario (sin contraseña)
class UserOut(UserBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True  # Permite convertir modelos SQLAlchemy a dict para respuestas JSON

# Esquema base para mensaje
class MessageBase(BaseModel):
    content: str

# Esquema para crear mensaje (enviar)
class MessageCreate(MessageBase):
    receiver_id: int  # ID del usuario que recibe el mensaje

# Esquema para devolver mensaje
class MessageOut(MessageBase):
    id: int
    timestamp: datetime
    sender_id: int
    receiver_id: int

    class Config:
        orm_mode = True
