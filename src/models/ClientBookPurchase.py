from typing import List
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from . import Base

class ClientBookPurchase(Base):
  __tablename__ = "clientbookpurchases"
  purchase_id: Mapped[int] = mapped_column(primary_key=True)
  client_id = Column(Integer, ForeignKey('clients.client_id'), primary_key=True),
  book_id = Column(Integer, ForeignKey('books.book_id'), primary_key=True
  ),

  client: Mapped["Client"] = relationship(back_populates="client_purchase")
  book: Mapped["Book"] = relationship(back_populates="book_purchase")
  def __repr__(self):
    return f"Client: {self.client_id} Book: {self.book_id}"