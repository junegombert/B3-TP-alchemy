from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

from . import Base, ClientBookPurchase

class Book(Base):
  __tablename__ = "books"
  book_id = Column(Integer, primary_key=True)
  book_name = Column(String(32))
  book_publisher = Column(ForeignKey("publishers.publisher_id"))
  clients: Mapped[List["Clients"]] = relationship(
    secondary="ClientBookPurchase",
    back_populates="books"  
  )

  client_purchase: Mapped[List["ClientBookPurchase"]] = relationship(
    back_populates="book"
  )

  def __repr__(self):
    return self.book_name

