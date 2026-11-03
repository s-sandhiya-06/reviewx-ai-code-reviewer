from sqlalchemy import Column, Integer, String, DateTime, Boolean
from sqlalchemy.sql import func

from app.db.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)

    github_id = Column(String, unique=True, nullable=False, index=True)

    username = Column(String, nullable=False)

    email = Column(String, unique=True, nullable=True)

    avatar_url = Column(String, nullable=True)

    is_active = Column(Boolean, default=True)

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )