from typing import List
from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

from . import Base

class Publisher(Base):
  __tablename__ = "publishers"
  publisher_id: Mapped[int] = mapped_column(primary_key=True)
  publisher_name: Mapped[str] = mapped_column(String(32))
  publisher_books: Mapped[List["Book"]] = relationship()