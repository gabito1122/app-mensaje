from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app import crud, schemas, auth
from app.database import get_db

router = APIRouter(
    prefix="/messages",
    tags=["messages"]
)

# Ruta para enviar un mensaje
@router.post("/", response_model=schemas.MessageOut)
def send_message(message: schemas.MessageCreate, 
                 current_user=Depends(auth.get_current_user), 
                 db: Session = Depends(get_db)):
    return crud.create_message(db, message, sender_id=current_user.id)

# Ruta para obtener mensajes entre el usuario autenticado y otro usuario
@router.get("/{user_id}", response_model=List[schemas.MessageOut])
def get_messages(user_id: int, 
                 current_user=Depends(auth.get_current_user), 
                 db: Session = Depends(get_db)):
    messages = crud.get_messages_between_users(db, current_user.id, user_id)
    return messages
