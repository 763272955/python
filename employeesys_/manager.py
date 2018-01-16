# -*- coding:utf-8 -*-

from app_sys import create_app, db
from app_sys.models import admin, test, trainset
from flask_script import Manager, Shell

app = create_app('default')
manager = Manager(app)

def make_shell_context():
    return dict(app=app, db=db, admin=admin, test=test, trainset=trainset)
manager.add_command("shell", Shell(make_context=make_shell_context()))

if __name__ == '__main__':
    app.run()