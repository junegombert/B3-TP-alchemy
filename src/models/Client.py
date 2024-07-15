from typing import List
from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

from . import Base, ClientBookPurchase

class Client(Base):
    __tablename__ = 'clients'

    client_id: Mapped[int] = mapped_column(primary_key=True)
    client_name: Mapped[str] = mapped_column(String(32))
    client_email: Mapped[str] = mapped_column(String(64))
    books = relationship("Book", secondary="ClientBookPurchase", back_populates="books")