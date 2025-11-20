from sqlalchemy import Column, Integer, String

from app.db import Base

class URL(Base):
    __tablename__ = "urls"

    id = Column(Integer, primary_key=True, index=True)
    slug = Column(String(16), unique=True, index=True)
    target_url = Column(String, nullable=False)