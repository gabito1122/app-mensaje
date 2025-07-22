from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Text
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import Base  # Importamos la base declarativa del archivo database.py

# Modelo para usuarios
class User(Base):
    __tablename__ = "users"  # Nombre de la tabla en la base de datos

    id = Column(Integer, primary_key=True, index=True)  # ID único y clave primaria
    email = Column(String, unique=True, index=True, nullable=False)  # Email único y obligatorio
    hashed_password = Column(String, nullable=False)  # Contraseña encriptada
    full_name = Column(String, nullable=True)  # Nombre completo (opcional)
    created_at = Column(DateTime, default=datetime.utcnow)  # Fecha de creación, por defecto la actual

    # Relación uno a muchos con mensajes enviados
    messages_sent = relationship("Message", back_populates="sender", foreign_keys='Message.sender_id')
    # Relación uno a muchos con mensajes recibidos
    messages_received = relationship("Message", back_populates="receiver", foreign_keys='Message.receiver_id')


# Modelo para mensajes
class Message(Base):
    __tablename__ = "messages"  # Nombre de la tabla en la base de datos

    id = Column(Integer, primary_key=True, index=True)  # ID único y clave primaria
    content = Column(Text, nullable=False)  # Contenido del mensaje
    timestamp = Column(DateTime, default=datetime.utcnow)  # Fecha y hora del mensaje

    # ForeignKey para relacionar con usuario remitente
    sender_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    # ForeignKey para relacionar con usuario receptor
    receiver_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    # Relaciones para poder acceder a los datos del remitente y receptor desde el mensaje
    sender = relationship("User", back_populates="messages_sent", foreign_keys=[sender_id])
    receiver = relationship("User", back_populates="messages_received", foreign_keys=[receiver_id])
