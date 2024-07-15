from typing import List
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import Mapped, relationship

from . import Base

class Publisher(Base):
  __tablename__ = "publishers"
  publisher_id = Column(Integer, primary_key=True)
  publisher_name = Column(String)
  publisher_books: Mapped[List["Book"]] = relationship()