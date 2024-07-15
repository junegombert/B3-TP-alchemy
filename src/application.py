from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.User import User

postgresql_url = 'postgresql://postgres:mypassword@localhost:5432/mydatabase'
engine = create_engine(postgresql_url)
Session = sessionmaker(bind=engine)
session = Session()

new_user = User(name="Charlie", email="charlie@example.com")
session.add(new_user)
session.commit()

all_users = session.query(User).all()
for user in all_users:
    print(f"User: {user.id}, Name: {user.name}, Email: {user.email}")

session.close()