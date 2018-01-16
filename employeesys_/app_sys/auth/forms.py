# -*- coding:utf-8 -*-

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, RadioField
from wtforms.validators import DataRequired, Length, Email

class NameForm(FlaskForm):
    email = StringField('Email Address',validators=[DataRequired(), Length(4, 64), Email()],
                        render_kw={"placeholder": "E-mail: yourname@example.com"})
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login in', render_kw={"class": "btn btn-default btn-block btn-success"})
    radio = RadioField(
        'Choice?',
        validators=[DataRequired()],
        choices=[ ('admin', u'管理员'), ('trainset', u'模型训练员'), ('test', u'领导')])
