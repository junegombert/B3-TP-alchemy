from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, User, Game

postgresql_url = 'postgresql://postgres:mypassword@localhost:5432/mydatabase'
engine = create_engine(postgresql_url, client_encoding="utf-8")
Session = sessionmaker(bind=engine)
session = Session()
Base.metadata.create_all(engine)

# new_user = User(name="Charlie", email="charlie@example.com")
# session.add(new_user)
# session.commit()

# all_users = session.query(User).all()
# for user in all_users:
#     print(f"User: {user.id}, Name: {user.name}, Email: {user.email}")

new_game = Game(title="Minecraft", nb_min_joueurs=1)
session.add(new_game)
session.commit()

all_games = session.query(Game).all()
for game in all_games:
  print(f"Game: {game.game_id}, Title: {game.title}, Nombre min. Joueurs: {game.nb_min_joueurs}")

session.close()