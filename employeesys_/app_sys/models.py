# -*- coding:utf-8 -*-

from . import db
from flask_login import UserMixin
from . import login_manager


class admin(UserMixin, db.Model):
    __tablename__ = 'user_admin'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password = db.Column(db.String(64), unique=True, index=True)
    def __repr__(self):
        return '<User %r>' % self.username

class trainset(UserMixin, db.Model):
    __tablename__ = 'user_trainset'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password = db.Column(db.String(64), unique=True, index=True)
    def __repr__(self):
        return '<User %r>' % self.username

class test(UserMixin, db.Model):
    __tablename__ = 'user_test'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password = db.Column(db.String(64), unique=True, index=True)
    def __repr__(self):
        return '<User %r>' % self.username

@login_manager.user_loader
def load_user(user_id):
    if admin.query.get(int(user_id)):
        return admin.query.get(int(user_id))
    if test.query.get(int(user_id)):
        return test.query.get(int(user_id))
    if trainset.query.get(int(user_id)):
        return trainset.query.get(int(user_id))

class trainset_Contribution(db.Model):
    __tablename__ = 'trainset_contribution'
    id = db.Column(db.Integer, primary_key=True)
    is_tool = db.Column(db.String(64), unique=True, index=True)
    profit = db.Column(db.String(64), unique=True, index=True)
    profit_level = db.Column(db.String(64), unique=True, index=True)
    satistied_level = db.Column(db.String(64), unique=True, index=True)
    result = db.Column(db.Integer, unique=True, index=True)
    def __repr__(self):
        return '<Contribution %r>' % self.id

class trainset_Contribution_train(db.Model):
    __tablename__ = 'trainset_contribution_train'
    id = db.Column(db.Integer, primary_key=True)
    is_tool = db.Column(db.String(64), unique=True, index=True)
    profit = db.Column(db.String(64), unique=True, index=True)
    profit_level = db.Column(db.String(64), unique=True, index=True)
    satistied_level = db.Column(db.String(64), unique=True, index=True)
    result = db.Column(db.Integer, unique=True, index=True)
    def __repr__(self):
        return '<Contribution %r>' % self.id


class Contribution(db.Model):
    __tablename__ = 'contribution'
    id = db.Column(db.Integer, primary_key=True)
    employee_id = db.Column(db.Integer)
    year_date = db.Column(db.String(64), unique=True, index=True)
    num = db.Column(db.String(64), unique=True, index=True)
    is_tool = db.Column(db.String(64), unique=True, index=True)
    profit = db.Column(db.String(64), unique=True, index=True)
    profit_level = db.Column(db.String(64), unique=True, index=True)
    satistied_level = db.Column(db.String(64), unique=True, index=True)
    score = db.Column(db.String(64), unique=True, index=True)
    def __repr__(self):
        return '<Contribution %r>' % self.id

class trainset_Attendance(db.Model):
    __tablename__ = 'trainset_attendance'
    id = db.Column(db.Integer, primary_key=True)
    late_number = db.Column(db.String(64), unique=True, index=True)
    leave_number = db.Column(db.String(64), unique=True, index=True)
    sickleave_number = db.Column(db.String(64), unique=True, index=True)
    absenteeism_number = db.Column(db.String(64), unique=True, index=True)
    late_level = db.Column(db.String(64),unique=True, index=True)
    leave_level = db.Column(db.String(64), unique=True, index=True)
    absenteeism_level = db.Column(db.String(64), unique=True, index=True)
    result = db.Column(db.Integer, unique=True, index=True)
    def __repr__(self):
        return '<Attendence %r>' % self.result

class trainset_Attendance_train(db.Model):
    __tablename__ = 'trainset_attendance_train'
    id = db.Column(db.Integer, primary_key=True)
    late_number = db.Column(db.String(64), unique=True, index=True)
    leave_number = db.Column(db.String(64), unique=True, index=True)
    sickleave_number = db.Column(db.String(64), unique=True, index=True)
    absenteeism_number = db.Column(db.String(64), unique=True, index=True)
    late_level = db.Column(db.String(64), unique=True, index=True)
    leave_level = db.Column(db.String(64), unique=True, index=True)
    absenteeism_level = db.Column(db.String(64), unique=True, index=True)
    result = db.Column(db.Integer, unique=True, index=True)
    def __repr__(self):
        return '<Attendence %r>' % self.result

class Attendance(db.Model):
    __tablename__ = 'attendance'
    id = db.Column(db.Integer, primary_key=True)
    employee_id = db.Column(db.Integer)
    year_date = db.Column(db.String(64),unique=True, index=True)
    month_date = db.Column(db.String(64), unique=True, index=True)
    late_number = db.Column(db.String(64), unique=True, index=True)
    late_level = db.Column(db.String(64), unique=True, index=True)
    leave_number = db.Column(db.String(64), unique=True, index=True)
    leave_level = db.Column(db.String(64), unique=True, index=True)
    sickleave_number = db.Column(db.String(64), unique=True, index=True)
    absenteeism_number = db.Column(db.String(64), unique=True, index=True)
    absenteeism_level = db.Column(db.String(64), unique=True, index=True)
    score = db.Column(db.String(64), unique=True, index=True)
    def __repr__(self):
        return '<Attendence %r>' % self.result

class Trainset(db.Model):
    __tablename__ = 'trainset'
    trainset_name = db.Column(db.String(64), primary_key=True)
    trainset = db.Column(db.String(64),unique=True, index=True)
    correct_rate = db.Column(db.String(64), unique=True, index=True)

class Employee(db.Model):
    __tablename__ = 'employee'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, index=True)
    sex = db.Column(db.String(64), unique=True, index=True)
    telephone = db.Column(db.String(64), unique=True, index=True)
    email = db.Column(db.Integer, unique=True, index=True)
    def __repr__(self):
        return '<Employee %r>' % self.id

class Tmp(db.Model):
    __tablename__ = 'tmp'
    employee_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, index=True)
    year = db.Column(db.String(64), unique=True, index=True, primary_key=True)
    attendance = db.Column(db.String(64), unique=True, index=True)
    contribution = db.Column(db.Integer, unique=True, index=True)
    result = db.Column(db.Integer, unique=True, index=True)