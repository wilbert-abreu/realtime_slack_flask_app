from flask import Flask
from flask_heroku import Heroku
import pdb

app = Flask(__name__)
# config_path = os.environ.get("CONFIG_PATH",
#                               "slack_clone.config.DevelopmentConfig")
#  app.config.from_object(config_path)
heroku = Heroku(app)

pdb.set_trace()

from . import views
from . import login

from .database import Base, engine
Base.metadata.create_all(engine)
