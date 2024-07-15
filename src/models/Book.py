from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from . import Base

class Book(Base):
  __tablename__ = "books"
  book_id: Mapped[int] = mapped_column(primary_key=True)
  book_name: Mapped[str] = mapped_column(String(32))
  book_publisher: Mapped[int] = mapped_column(ForeignKey("publishers.publisher_id"))

  def __repr__(self):
    return self.book_name