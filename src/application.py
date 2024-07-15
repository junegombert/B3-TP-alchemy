from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Créer l'extension
db = SQLAlchemy()

# Créer l'application
app = Flask(__name__)

# Configurer la BDD
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///project.db"

# Initialiser l'appli à partir de l'extension
db.init_app(app)