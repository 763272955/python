# -*- coding:utf-8 -*-

from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from forms import NameForm


app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guss string'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost/employeesys'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

bootstrap = Bootstrap(app)
@app.route('/', methods=['get', 'post'])
def index():
    name = None
    form = NameForm()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
    return render_template('auth.html', form=form, name=name)

if __name__ == "__main__":
    app.run(debug=True )