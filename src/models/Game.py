from sqlalchemy import Column, String, Integer
from models.Base import Base

class Game(Base):
    __tablename__ = 'games'

    game_id = Column(Integer, primary_key=True)
    title = Column(String)
    nb_min_joueurs = Column(Integer)
