from sqlalchemy.orm import Session
from . import models, schemas
from passlib.context import CryptContext

# Contexto para encriptar contraseñas con bcrypt
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Función para hashear (encriptar) la contraseña
def hash_password(password: str):
    return pwd_context.hash(password)

# Función para verificar que la contraseña en texto plano coincide con la hasheada
def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)

# Crear un nuevo usuario en la base de datos
def create_user(db: Session, user: schemas.UserCreate):
    hashed_pw = hash_password(user.password)
    db_user = models.User(email=user.email, full_name=user.full_name, hashed_password=hashed_pw)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)  # Refresca el objeto con los datos guardados (como el id)
    return db_user

# Buscar usuario por email (para login o validación)
def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

# Crear y guardar un mensaje
def create_message(db: Session, message: schemas.MessageCreate, sender_id: int):
    db_message = models.Message(
        content=message.content,
        sender_id=sender_id,
        receiver_id=message.receiver_id
    )
    db.add(db_message)
    db.commit()
    db.refresh(db_message)
    return db_message

# Obtener mensajes entre dos usuarios ordenados por fecha
def get_messages_between_users(db: Session, user1_id: int, user2_id: int):
    return db.query(models.Message).filter(
        ((models.Message.sender_id == user1_id) & (models.Message.receiver_id == user2_id)) |
        ((models.Message.sender_id == user2_id) & (models.Message.receiver_id == user1_id))
    ).order_by(models.Message.timestamp).all()
