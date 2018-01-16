# -*- coding:utf-8 -*-

from flask_wtf import FlaskForm, Form
from wtforms import StringField, SubmitField, PasswordField, BooleanField, SelectField, DateField
from wtforms.validators import DataRequired, Length, Email, Required, Regexp

class trainset_attendanceForm(FlaskForm):
    late_number = StringField(u'迟到次数', validators=[DataRequired()])
    leave_number = StringField(u'请假次数', validators=[DataRequired()])
    sickleave_number = StringField(u'病假次数', validators=[DataRequired()])
    absenteeism_number = StringField(u'旷工次数', validators=[DataRequired()])
    score = SelectField(u'最终分数',choices=[('', ''), ('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')])
    submit = SubmitField('OK', render_kw={"class": "btn btn-default btn-block btn-success"})

class trainset_contributionForm(FlaskForm):
    is_tool = SelectField(u'是否工具', choices=[(u'否', u'否'), (u'是', u'是')])
    profit = StringField(u'收益金额', validators=[DataRequired()])
    satistied_level = SelectField(u'满意程度', choices=[(u'一般', u'一般'), (u'满意', u'满意'), (u'非常满意', u'非常满意')])
    score = SelectField(u'最终分数', choices=[('', ''), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')])
    submit = SubmitField('OK', render_kw={"class": "btn btn-default btn-block btn-success"})

class employeeForm(FlaskForm):
    name = StringField(u"姓名", validators=[DataRequired()])
    sex = StringField(u"性别", validators=[DataRequired()])
    telephone = StringField(u"联系电话", validators=[DataRequired()])
    email = StringField(u"邮箱", validators=[DataRequired(), Length(4, 64), Email()])
    submit = SubmitField('OK', render_kw={"class": "btn btn-default btn-block btn-success"})

class contributionForm(FlaskForm):
    year_date = StringField(u'年份', validators=[DataRequired()])
    num = StringField(u'编号', validators=[DataRequired()])
    is_tool = SelectField(u'是否工具', choices=[(u'否', u'否'), (u'是', u'是')])
    profit = StringField(u'收益金额', validators=[DataRequired()])
    satistied_level = SelectField(u'满意程度', choices=[(u'一般', u'一般'), (u'满意', u'满意'), (u'非常满意', u'非常满意')])
    score = SelectField(u'最终分数', choices=[('', ''), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')])
    submit = SubmitField('OK', render_kw={"class": "btn btn-default btn-block btn-success"})

class attendanceForm(FlaskForm):
    year_date = StringField(u'年份', validators=[DataRequired()])
    month_date = StringField(u'月份', validators=[DataRequired()])
    late_number = StringField(u'迟到次数', validators=[DataRequired()])
    leave_number = StringField(u'请假次数', validators=[DataRequired()])
    sickleave_number = StringField(u'病假次数', validators=[DataRequired()])
    absenteeism_number = StringField(u'旷工次数', validators=[DataRequired()])
    score = SelectField(u'最终分数', choices=[('', ''), ('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5') ])
    submit = SubmitField('OK', render_kw={"class": "btn btn-default btn-block btn-success"})