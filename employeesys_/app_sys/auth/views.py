# -*- coding:utf-8 -*-


from flask import render_template, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required
from forms import NameForm
from ..auth import auth
from ..models import admin, test, trainset


@auth.route('/', methods=['GET', 'POST'])
def login():
    form = NameForm()
    if form.validate_on_submit():
        if form.radio.data == 'admin':
            user = admin.query.filter_by(username=form.email.data, password=form.password.data).first()
            if user is not None:
                login_user(user)
                return redirect(url_for('main.employee'))
            flash(u'无效的邮箱或者密码')
        elif form.radio.data == 'trainset':
            user = trainset.query.filter_by(username=form.email.data, password=form.password.data).first()
            if user is not None:
                login_user(user)
                return redirect(url_for('main.trainset_attendance'))
            flash(u'无效的邮箱或者密码')
        elif form.radio.data == 'test':
            user = test.query.filter_by(username=form.email.data, password=form.password.data).first()
            if user is not None:
                login_user(user)
                return redirect(url_for('main.result'))
            flash(u'无效的邮箱或者密码')
        else:
            flash(u'请选择角色')
    return render_template('auth/auth.html', form=form)

@auth.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('.login'))