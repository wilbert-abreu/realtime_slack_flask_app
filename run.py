import os
from flask_script import Manager
from slack_clone import app, Base
from flask_migrate import Migrate, MigrateCommand

manager = Manager(app)


def run():
    port = int(os.environ.get('PORT', 8080))
    ip = os.environ.get('IP', '0.0.0.0')
    app.run(host=ip, port=port)


class DB(object):
    def __init__(self, metadata):
        self.metadata = metadata

migrate = Migrate(app, DB(Base.metadata))
manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    run()

