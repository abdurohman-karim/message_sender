from datetime import datetime
from sqlalchemy import Column, Integer, BigInteger, String, TIMESTAMP
from app.db.base import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    telegram_id = Column(BigInteger, unique=True, index=True, nullable=False)
    phone = Column(String(32), unique=True, index=True, nullable=True)
    first_name = Column(String(255), nullable=True)
    last_name = Column(String(255), nullable=True)
    username = Column(String(255), nullable=True)
    created_at = Column(TIMESTAMP, default=datetime.utcnow)
