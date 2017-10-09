#!/usr/bin/env python

import os
from app import create_app, db
from app.models import User, Article, Category
from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

from flask_login import LoginManager, current_user

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)
migrate = Migrate(app, db)



# flask_login
app.secret_key = '5Yas55Oc'
login_manager = LoginManager()
login_manager.init_app(app)

# flask_admin
class AdminModelView(ModelView):
    def is_accessible(self):
        if current_user.is_authenticated and current_user.nickname == 'gua':
            return True
        return False

admin = Admin(app)
admin.add_view(AdminModelView(User, db.session))
admin.add_view(AdminModelView(Article, db.session))
admin.add_view(AdminModelView(Category, db.session))

@login_manager.user_loader
def user_loader(id):
    from app.models import User
    user = User.query.filter_by(id = id).first()
    return user

def make_shell_context():
    return dict(app = app, db = db, User = User, Article = Article, Category = Category)

manager.add_command("shell", Shell(make_context = make_shell_context))
manager.add_command("db", MigrateCommand)

if __name__ == '__main__':
    manager.run()

