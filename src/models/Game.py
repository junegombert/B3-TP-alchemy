from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped, mapped_column
from . import Base

class Game(Base):
    __tablename__ = 'games'

    game_id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(32))
    nb_min_joueurs: Mapped[int] = mapped_column()
