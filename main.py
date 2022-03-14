# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from app import create_app, db
from app.models import User
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

app = create_app("production")

manager = Manager(app)
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)

@manager.shell
def make_shell_ctx():
    return dict(app=app, db=db, User=User)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run()
    # manager.run()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
