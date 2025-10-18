from sqlalchemy import Column, Integer, String, Text
from src.db.base import Base

class Company(Base):
    __tablename__ = "companies"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    description = Column(Text)
    rep_name = Column(String(255))
    info = Column(Text)
    keywords = Column(String(500))
    other_info = Column(Text)
