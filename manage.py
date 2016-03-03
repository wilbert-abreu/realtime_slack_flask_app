from flask_script import Manager
from slack_clone import app, Base
from flask_migrate import Migrate, MigrateCommand

manager = Manager(app)

class DB(object):
    def __init__(self, metadata):
        self.metadata = metadata

migrate = Migrate(app, DB(Base.metadata))
manager.add_command('db', MigrateCommand)