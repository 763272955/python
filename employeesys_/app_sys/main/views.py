# -*- coding:utf-8 -*-

import uuid
from employeesys_.ID3_ import level,test,id3_main
from flask import render_template, session, redirect, url_for, flash, request
from . import main
from forms import trainset_contributionForm, trainset_attendanceForm, employeeForm, contributionForm, attendanceForm
from .. import db
from ..models import trainset_Attendance, trainset_Attendance_train, trainset_Contribution, trainset_Contribution_train, Attendance, Contribution, Employee, Trainset, Tmp

@main.route('/trainset_contribution', methods=['GET', 'POST'])
def trainset_contribution():
    contributions_ = Contribution.query.all()
    for contri in contributions_:
        exist_ = trainset_Contribution.query.filter_by(id=contri.id).first()
        exist__ = trainset_Contribution_train.query.filter_by(id=contri.id).first()
        if exist_ is None and exist__ is None:
            if contri.score is not None:
                contri_trainset = trainset_Contribution(
                    id=contri.id,
                    is_tool=contri.is_tool,
                    profit=contri.profit,
                    profit_level=contri.profit_level,
                    satistied_level=contri.satistied_level,
                    result=contri.score
                )
                db.session.add(contri_trainset)
                db.session.commit()
    contributions = trainset_Contribution.query.all()
    trainset = Trainset.query.filter_by(trainset_name='contribution').all()
    contributions_train = trainset_Contribution_train.query.all()
    return render_template('trainset_contribution.html', contributions=contributions, trainsets=trainset, contributions_train=contributions_train)
@main.route('/insert_train_contribution', methods=['GET', 'POST'])
def insert_train_contribution():
    form = trainset_contributionForm()
    if form.validate_on_submit():
        profit_level_ = level.contribution_profitlevel(form.profit.data)
        trainset_contribution = trainset_Contribution(
            id=uuid.uuid1(),
            is_tool=form.is_tool.data,
            profit=form.profit.data,
            profit_level=profit_level_,
            satistied_level=form.satistied_level.data,
            result=form.score.data)
        db.session.add(trainset_contribution)
        db.session.commit()
        return redirect(url_for('.trainset_contribution'))
    return render_template('insert_trainset_contribution.html', form=form)
@main.route('/insert_train_contribution_', methods=['GET', 'POST'])
def insert_train_contribution_():
    trainset_contribution_train = trainset_Contribution_train.query.filter_by(id=request.args.get('selectid')).first_or_404()
    trainset_contribution = trainset_Contribution(
        id=trainset_contribution_train.id,
        is_tool=trainset_contribution_train.is_tool,
        profit=trainset_contribution_train.profit,
        profit_level=trainset_contribution_train.profit_level,
        satistied_level=trainset_contribution_train.satistied_level,
        result=trainset_contribution_train.result)
    db.session.add(trainset_contribution)
    db.session.commit()
    db.session.delete(trainset_contribution_train)
    db.session.commit()
    return redirect(url_for('.trainset_contribution'))
@main.route('/insert_train_contribution_train', methods=['GET', 'POST'])
def insert_train_contribution_train():
    trainset_contribution = trainset_Contribution.query.filter_by(id=request.args.get('selectid')).first_or_404()
    trainset_contribution_train = trainset_Contribution_train(
        id=trainset_contribution.id,
        is_tool=trainset_contribution.is_tool,
        profit=trainset_contribution.profit,
        profit_level=trainset_contribution.profit_level,
        satistied_level=trainset_contribution.satistied_level,
        result=trainset_contribution.result)
    db.session.add(trainset_contribution_train)
    db.session.commit()
    db.session.delete(trainset_contribution)
    db.session.commit()
    return redirect(url_for('.trainset_contribution'))
@main.route('/delete_train_contribution', methods=['GET', 'POST'])
def delete_train_contribution():
    trainset_contribution = trainset_Contribution.query.filter_by(id=request.args.get('selectid')).first_or_404()
    db.session.delete(trainset_contribution)
    db.session.commit()
    return redirect(url_for('.trainset_contribution'))
@main.route('/delete_train_contribution_train', methods=['GET', 'POST'])
def delete_train_contribution_train():
    trainset_contribution = trainset_Contribution_train.query.filter_by(id=request.args.get('selectid')).first_or_404()
    db.session.delete(trainset_contribution)
    db.session.commit()
    return redirect(url_for('.trainset_contribution'))
@main.route('/train_contribution', methods=['GET', 'POST'])
def train_contribution():
    contributions = trainset_Contribution_train.query.all()
    datas = []
    for x in range(len(contributions)):
        data = []
        data.append(0 if contributions[x].is_tool == u'否' else 1)
        data.append(1 if contributions[x].profit_level == u'低' else (2 if contributions[x].profit_level == u'中'else 3))
        data.append(1 if contributions[x].satistied_level == u'一般' else (2 if contributions[x].satistied_level == u'满意' else 3))
        data.append(int(contributions[x].result))
        datas.append(data)
    labels = ["tool", "profit", "satistied"]
    labels_feat = {"tool": {0: "no", 1: "yes"},
                   "profit": {1: "low", 2: "high", 3: "veryHigh"},
                   "satistied": {1: "good", 2: "great", 3: "perfect"}}
    trainset_ = id3_main.train(datas, labels, labels_feat)
    train = Trainset.query.filter_by(trainset_name='contribution').first()
    if train is None:
        train = Trainset(
            trainset_name='contribution',
            trainset=trainset_
        )
        db.session.add(train)
        db.session.commit()
    else:
        train.trainset=trainset_
        db.session.add(train)
        db.session.commit()
    return redirect(url_for('.trainset_contribution'))



@main.route('/trainset_attendance', methods=['GET', 'POST'])
def trainset_attendance():
    attendances_ = Attendance.query.all()
    for atten in attendances_:
        exist_ = trainset_Attendance.query.filter_by(id=atten.id).first()
        exist__ = trainset_Attendance_train.query.filter_by(id=atten.id).first()
        if exist_ is None and exist__ is None:
            if atten.score is not None:
                atten_trainset = trainset_Attendance(
                    id=atten.id,
                    late_number=atten.late_number,
                    leave_number=atten.leave_number,
                    sickleave_number=atten.sickleave_number,
                    absenteeism_number=atten.absenteeism_number,
                    late_level=atten.late_level,
                    leave_level=atten.leave_level,
                    absenteeism_level=atten.absenteeism_level,
                    result=atten.score
                )
                db.session.add(atten_trainset)
                db.session.commit()
    attendances = trainset_Attendance.query.all()
    attendances_train = trainset_Attendance_train.query.all()
    trainset = Trainset.query.filter_by(trainset_name='attendance').all()
    return render_template('trainset_attendance.html', attendances=attendances, trainset=trainset, attendances_train=attendances_train)
@main.route('/insert_train_attendance', methods=['GET', 'POST'])
def insert_train_attendance():
    form = trainset_attendanceForm()
    if form.validate_on_submit():
        if int(form.leave_number.data) - int(form.sickleave_number.data) >= 0:
            absenteeism_level_ = level.attendance_absenteeismlevel(form.absenteeism_number.data)
            late_level_ = level.attendance_latelevel(form.late_number.data)
            leave_level_ = level.attendance_leavelevel(form.leave_number.data, form.sickleave_number.data)
            attendance = trainset_Attendance(
                id=uuid.uuid1(),
                leave_level=leave_level_,
                leave_number=form.leave_number.data,
                sickleave_number=form.sickleave_number.data,
                late_level=late_level_,
                late_number=form.late_number.data,
                absenteeism_level=absenteeism_level_,
                absenteeism_number=form.absenteeism_number.data,
                result=form.score.data)
            db.session.add(attendance)
            db.session.commit()
        else:
            flash(u'请确认病假天数!')
        return redirect(url_for('.trainset_attendance'))
    return render_template('insert_trainset_attendance.html', form=form)
@main.route('/insert_train_attendance_', methods=['GET', 'POST'])
def insert_train_attendance_():
    trainset_attendance_train = trainset_Attendance_train.query.filter_by(id=request.args.get('selectid')).first_or_404()
    trainset_attendance = trainset_Attendance(
        id=trainset_attendance_train.id,
        late_number=trainset_attendance_train.late_number,
        leave_number=trainset_attendance_train.leave_number,
        sickleave_number=trainset_attendance_train.sickleave_number,
        absenteeism_number=trainset_attendance_train.absenteeism_number,
        late_level=trainset_attendance_train.late_level,
        leave_level=trainset_attendance_train.leave_level,
        absenteeism_level=trainset_attendance_train.absenteeism_level,
        result=trainset_attendance_train.result)
    db.session.add(trainset_attendance)
    db.session.commit()
    db.session.delete(trainset_attendance_train)
    db.session.commit()
    return redirect(url_for('.trainset_attendance'))
@main.route('/insert_train_attendance_train', methods=['GET', 'POST'])
def insert_train_attendance_train():
    trainset_attendance = trainset_Attendance.query.filter_by(id=request.args.get('selectid')).first_or_404()
    trainset_attendance_train = trainset_Attendance_train(
        id=trainset_attendance.id,
        late_number=trainset_attendance.late_number,
        leave_number=trainset_attendance.leave_number,
        sickleave_number=trainset_attendance.sickleave_number,
        absenteeism_number=trainset_attendance.absenteeism_number,
        late_level=trainset_attendance.late_level,
        leave_level=trainset_attendance.leave_level,
        absenteeism_level=trainset_attendance.absenteeism_level,
        result=trainset_attendance.result)
    db.session.add(trainset_attendance_train)
    db.session.commit()
    db.session.delete(trainset_attendance)
    db.session.commit()
    return redirect(url_for('.trainset_attendance'))
@main.route('/delete_train_attendance', methods=['GET', 'POST'])
def delete_train_attendance():
    trainset_attendance = trainset_Attendance.query.filter_by(id=request.args.get('selectid')).first_or_404()
    db.session.delete(trainset_attendance)
    db.session.commit()
    return redirect(url_for('.trainset_attendance'))
@main.route('/delete_train_attendance_train', methods=['GET', 'POST'])
def delete_train_attendance_train():
    trainset_attendance = trainset_Attendance_train.query.filter_by(id=request.args.get('selectid')).first_or_404()
    db.session.delete(trainset_attendance)
    db.session.commit()
    return redirect(url_for('.trainset_attendance'))
@main.route('/train_attendance', methods=['GET', 'POST'])
def train_attendance():
    attendances = trainset_Attendance_train.query.all()
    datas = []
    for x in range(len(attendances)):
        data = []
        data.append(0 if attendances[x].absenteeism_level == u'差' else 1)
        data.append(0 if attendances[x].late_level == u'差' else (1 if attendances[x].late_level == u'良' else 2))
        data.append(0 if attendances[x].leave_level == u'差' else (1 if attendances[x].leave_level == u'中' else (2 if attendances[x].leave_level == u'良' else 3)))
        data.append(int(attendances[x].result))
        datas.append(data)
    labels = ['absenteeism', 'late', 'leave']
    labels_feat = {"late": {0: "miss", 1: "great", 2: 'perfect'},
                   "leave": {0: "miss", 1: "good", 2: 'great', 3: 'perfect'},
                   "absenteeism": {0: "miss", 1: 'perfect'}}
    trainset_ = id3_main.train(datas, labels, labels_feat)
    train = Trainset.query.filter_by(trainset_name='attendance').first()
    if train is None:
        train = Trainset(
            trainset_name='attendance',
            trainset=trainset_
        )
        db.session.add(train)
        db.session.commit()
    else:
        train.trainset = trainset_
        db.session.add(train)
        db.session.commit()
    return redirect(url_for('.trainset_attendance'))



@main.route('/delete_trainset', methods=['GET','POST'])
def delete_trainset():
    trainset = Trainset.query.filter_by(trainset_name=request.args.get('trainsetname')).first_or_404()
    db.session.delete(trainset)
    db.session.commit()
    if request.args.get('trainsetname') == 'attendance':
        return redirect(url_for('.trainset_attendance'))
    return redirect(url_for('.trainset_contribution'))



@main.route('/employee', methods=['GET', 'POST'])
def employee():
    name_ = request.form.get('name')
    if name_ is None or name_ == '':
        employee = Employee.query.all()
    else:
        employee = Employee.query.filter_by(name=name_).all()
    return render_template('employee.html', employees=employee)
@main.route('/insert_employee', methods=['GET', 'POST'])
def insert_employee():
    form = employeeForm()
    if form.validate_on_submit():
        myid = uuid.uuid1()
        employee = Employee(
            id=myid,
            name=form.name.data,
            sex=form.sex.data,
            telephone=form.telephone.data,
            email=form.email.data
        )
        db.session.add(employee)
        db.session.commit()
        return redirect(url_for('.employee'))
    return render_template('insert_employee.html', form=form)
@main.route('/change_employee', methods=['GET', 'POST'])
def change_employee():
    form = employeeForm()
    emp = Employee.query.filter_by(id=request.args.get('selectid')).first()
    if form.validate_on_submit():
        emp.name=form.name.data,
        emp.sex=form.sex.data,
        emp.telephone=form.telephone.data,
        emp.email=form.email.data
        db.session.add(emp)
        db.session.commit()
        return redirect(url_for('.employee'))
    form.name.data = emp.name
    form.sex.data = emp.sex
    form.telephone.data = emp.telephone
    form.email.data = emp.email
    return render_template('change_employee.html', form=form)
@main.route('/delete_employee', methods=['GET', 'POST'])
def delete_employee():
    employee = Employee.query.filter_by(id=request.args.get('selectid')).first_or_404()
    db.session.delete(employee)
    db.session.commit()
    contribution = Contribution.query.filter_by(employee_id=request.args.get('selectid')).all()
    if len(contribution) != 0:
        for x in contribution:
            db.session.delete(x)
            db.session.commit()
    attendance = Attendance.query.filter_by(employee_id=request.args.get('selectid')).all()
    if len(attendance) != 0:
        for x in attendance:
            db.session.delete(x)
            db.session.commit()
    tmp = Tmp.query.filter_by(employee_id=request.args.get('selectid')).all()
    if len(tmp) != 0:
        for x in tmp:
            db.session.delete(x)
            db.session.commit()




@main.route('/contribution', methods=['GET', 'POST'])
def contribution():
    id = request.args.get('selectid')
    contribution = Contribution.query.filter_by(employee_id=id).all()
    return render_template('contribution.html', contributions=contribution, employee_id=id)
@main.route('/insert_contribution', methods=['GET', 'POST'])
def insert_contribution():
    form = contributionForm()
    if form.validate_on_submit():
        exist_ = Contribution.query.filter_by(employee_id=request.args.get('employees_id'), year_date=form.year_date.data,num=form.num.data).first()
        if exist_ is None:
            if form.score.data == '':
                profit_level_ = level.contribution_profitlevel(form.profit.data)
                contribution = Contribution(
                    id = uuid.uuid1(),
                    employee_id=request.args.get('employees_id'),
                    is_tool=form.is_tool.data,
                    year_date=form.year_date.data,
                    num=form.num.data,
                    profit=form.profit.data,
                    profit_level=profit_level_,
                    satistied_level=form.satistied_level.data)
                db.session.add(contribution)
                db.session.commit()
            else:
                profit_level_ = level.contribution_profitlevel(form.profit.data)
                contribution = Contribution(
                    id=uuid.uuid1(),
                    employee_id=request.args.get('employees_id'),
                    is_tool=form.is_tool.data,
                    year_date=form.year_date.data,
                    num=form.num.data,
                    profit=form.profit.data,
                    profit_level=profit_level_,
                    satistied_level=form.satistied_level.data,
                    score=form.score.data)
                db.session.add(contribution)
                db.session.commit()
            return redirect(url_for('.contribution', selectid=request.args.get('employees_id')))
        flash(u'编号已存在!')
    return render_template('insert_contribution.html', form=form, employee_id=request.args.get('employees_id'))
@main.route('/change_contribution', methods=['GET', 'POST'])
def change_contribution():
    form = contributionForm()
    contri = Contribution.query.filter_by(id=request.args.get('selectid')).first()
    if form.validate_on_submit():
        if request.args.get('employees_id') != contri.employee_id and form.year_date.data!=contri.year_date and form.num.data!=contri.num:
            exist_ = Contribution.query.filter_by(employee_id=request.args.get('employees_id'), year_date=form.year_date.data,num=form.num.data).first()
        else:
            exist_ = None
        if exist_ is None:
            profit_level_ = level.contribution_profitlevel(form.profit.data)
            contri.is_tool = form.is_tool.data
            contri.year_date = form.year_date.data
            contri.num = form.num.data
            contri.profit = form.profit.data
            contri.profit_level = profit_level_
            contri.satistied_level = form.satistied_level.data
            if form.score.data != '':
                contri.score=form.score.data
            db.session.add(contri)
            db.session.commit()
            return redirect(url_for('.contribution', selectid=request.args.get('employees_id')))
        flash(u'编号已存在!')
    form.year_date.data = contri.year_date
    form.num.data = contri.num
    form.is_tool.data = contri.is_tool
    form.profit.data = contri.profit
    form.satistied_level.data = contri.satistied_level
    form.score.data = str(contri.score)
    return render_template('insert_contribution.html', form=form, employee_id=request.args.get('employees_id'))
@main.route('/delete_contribution', methods=['GET', 'POST'])
def delete_contribution():
    contribution = Contribution.query.filter_by(id=request.args.get('selectid')).first_or_404()
    tmp = Tmp.query.filter_by(employee_id=contribution.employee_id, year=contribution.year_date).first()
    if tmp is not None:
        tmp.attendance -= contribution.score
        tmp.result -= contribution.score
        db.session.add(tmp)
        db.session.commit()
    db.session.delete(contribution)
    db.session.commit()
    return redirect(url_for('.contribution', selectid=request.args.get('employees_id')))



@main.route('/attendance', methods=['GET', 'POST'])
def attendance():
    attendance = Attendance.query.filter_by(employee_id=request.args.get('selectid')).all()
    return render_template('attendance.html', attendances=attendance, employee_id=request.args.get('selectid'))
@main.route('/insert_attendance', methods=['GET', 'POST'])
def insert_attendance():
    form = attendanceForm()
    if form.validate_on_submit():
        exist_ = Attendance.query.filter_by(employee_id=request.args.get('employees_id'), year_date=form.year_date.data, month_date=form.month_date.data).first()
        if exist_ is None:
            if int(form.leave_number.data) - int(form.sickleave_number.data) >= 0:
                if form.score.data == '':
                    absenteeism_level_ = level.attendance_absenteeismlevel(form.absenteeism_number.data)
                    late_level_ = level.attendance_latelevel(form.late_number.data)
                    leave_level_ = level.attendance_leavelevel(form.leave_number.data, form.sickleave_number.data)
                    attendance = Attendance(
                        id = uuid.uuid1(),
                        employee_id=request.args.get('employees_id'),
                        year_date=form.year_date.data,
                        month_date=form.month_date.data,
                        leave_level=leave_level_,
                        leave_number=form.leave_number.data,
                        sickleave_number=form.sickleave_number.data,
                        late_level=late_level_,
                        late_number=form.late_number.data,
                        absenteeism_level=absenteeism_level_,
                        absenteeism_number=form.absenteeism_number.data)
                    db.session.add(attendance)
                    db.session.commit()
                else:
                    absenteeism_level_ = level.attendance_absenteeismlevel(form.absenteeism_number.data)
                    late_level_ = level.attendance_latelevel(form.late_number.data)
                    leave_level_ = level.attendance_leavelevel(form.leave_number.data, form.sickleave_number.data)
                    attendance = Attendance(
                        id=uuid.uuid1(),
                        employee_id=request.args.get('employees_id'),
                        year_date=form.year_date.data,
                        month_date=form.month_date.data,
                        leave_level=leave_level_,
                        leave_number=form.leave_number.data,
                        sickleave_number=form.sickleave_number.data,
                        late_level=late_level_,
                        late_number=form.late_number.data,
                        absenteeism_level=absenteeism_level_,
                        absenteeism_number=form.absenteeism_number.data,
                        score=form.score.data)
                    db.session.add(attendance)
                    db.session.commit()
                return redirect(url_for('.attendance', selectid=request.args.get('employees_id')))
            else:
                flash(u'请确认病假天数!')
        else:
            flash(u'请确认日期是否正确!')
    return render_template('insert_attendance.html', form=form, employee_id=request.args.get('employees_id'))
@main.route('/change_attendance', methods=['GET', 'POST'])
def change_attendance():
    form = attendanceForm()
    atten = Attendance.query.filter_by(id=request.args.get('selectid')).first()
    if form.validate_on_submit():
        if request.args.get('employees_id') != atten.employee_id and form.year_date.data!=atten.year_date and form.month_date.data!=atten.month_date:
            exist_ = Attendance.query.filter_by(employee_id=request.args.get('employees_id'), year_date=form.year_date.data, month_date=form.month_date.data).first()
        else:
            exist_ = None
        if exist_ is None:
            if int(form.leave_number.data) - int(form.sickleave_number.data) >= 0:
                absenteeism_level_ = level.attendance_absenteeismlevel(form.absenteeism_number.data)
                late_level_ = level.attendance_latelevel(form.late_number.data)
                leave_level_ = level.attendance_leavelevel(form.leave_number.data, form.sickleave_number.data)
                atten.year_date = form.year_date.data,
                atten.month_date = form.month_date.data,
                atten.leave_level = leave_level_,
                atten.leave_number = form.leave_number.data,
                atten.sickleave_number = form.sickleave_number.data,
                atten.late_level = late_level_,
                atten.late_number = form.late_number.data,
                atten.absenteeism_level = absenteeism_level_,
                atten.absenteeism_number = form.absenteeism_number.data,
                if form.score.data != '':
                    atten.score = form.score.data
                db.session.add(atten)
                db.session.commit()
                return redirect(url_for('.attendance', selectid=request.args.get('employees_id')))
            else:
                flash(u'请确认病假天数!')
        else:
            flash(u'请确认日期是否正确!')
    form.year_date.data = atten.year_date
    form.month_date.data = atten.month_date
    form.leave_number.data = atten.leave_number
    form.sickleave_number.data = atten.sickleave_number
    form.late_number.data = atten.late_number
    form.absenteeism_number.data = atten.absenteeism_number
    form.score.data = str(atten.score)
    return render_template('change_attendance.html', form=form, employee_id=request.args.get('employees_id'))
@main.route('/delete_attendance', methods=['GET', 'POST'])
def delete_attendance():
    attendance = Attendance.query.filter_by(id=request.args.get('selectid')).first_or_404()
    tmp = Tmp.query.filter_by(employee_id=attendance.employee_id, year=attendance.year_date).first()
    if tmp is not None:
        tmp.attendance -= attendance.score
        tmp.result -= attendance.score
        db.session.add(tmp)
        db.session.commit()
    db.session.delete(attendance)
    db.session.commit()
    return redirect(url_for('.attendance', selectid=request.args.get('employees_id')))



@main.route('/get_result', methods=['GET', 'POST'])
def get_result():
    attendances = Attendance.query.all()
    contributions = Contribution.query.all()
    tmp = Tmp.query.all()
    if len(tmp) != 0:
        for tmp_ in tmp:
            db.session.delete(tmp_)
            db.session.commit()
    trainset_atten = Trainset.query.filter_by(trainset_name='attendance').first()
    trainset_contri = Trainset.query.filter_by(trainset_name='attendance').first()
    if trainset_atten is not None and trainset_contri is not None:
        for atten in attendances:
            score_ = test.test_Attendance(atten.absenteeism_level, atten.late_level, atten.leave_level)
            tmp = Tmp.query.filter_by(employee_id=atten.employee_id, year=atten.year_date).first()
            if tmp is None:
                tmp_ = Tmp(
                    employee_id=atten.employee_id,
                    name=Employee.query.filter_by(id=atten.employee_id).first().name,
                    year=atten.year_date,
                    attendance=score_,
                    contribution=0,
                    result=score_
                )
                db.session.add(tmp_)
                db.session.commit()
                atten.score = score_
                db.session.add(atten)
                db.session.commit()
            else:
                tmp.attendance += score_
                tmp.result += score_
                db.session.add(tmp)
                db.session.commit()
                atten.score = score_
                db.session.add(atten)
                db.session.commit()
        for contri in contributions:
            score_ = test.test_Contribution(contri.is_tool, contri.profit_level, contri.satistied_level)
            tmp = Tmp.query.filter_by(employee_id=contri.employee_id, year=contri.year_date).first()
            if tmp is None:
                tmp_ = Tmp(
                    employee_id=contri.employee_id,
                    name=Employee.query.filter_by(id=contri.employee_id).first().name,
                    year=contri.year_date,
                    attendance=0,
                    contribution=score_,
                    result=score_
                )
                db.session.add(tmp_)
                db.session.commit()
                contri.score = score_
                db.session.add(contri)
                db.session.commit()
            else:
                tmp.contribution += score_
                tmp.result += score_
                db.session.add(tmp)
                db.session.commit()
                contri.score = score_
                db.session.add(contri)
                db.session.commit()
        return redirect(url_for('.result'))
    flash(u'请确定模型是否训练完成!')
    return redirect(url_for('.employee'))
@main.route('/get_oneresult', methods=['GET', 'POST'])
def get_oneresult():
    attendances = Attendance.query.filter_by(employee_id=request.args.get('selectid'), year_date=request.args.get('selectyear'))
    contributions = Contribution.query.filter_by(employee_id=request.args.get('selectid'), year_date=request.args.get('selectyear'))
    tmp = Tmp.query.filter_by(employee_id=request.args.get('selectid'), year=request.args.get('selectyear')).first()
    if tmp is not None:
        db.session.delete(tmp)
        db.session.commit()
    trainset_atten = Trainset.query.filter_by(trainset_name='attendance').first()
    trainset_contri = Trainset.query.filter_by(trainset_name='contribution').first()
    if trainset_atten is not None and trainset_contri is not None:
        for atten in attendances:
            score_ = test.test_Attendance(atten.absenteeism_level, atten.late_level, atten.leave_level)
            tmp = Tmp.query.filter_by(employee_id=atten.employee_id, year=atten.year_date).first()
            if tmp is None:
                tmp_ = Tmp(
                    employee_id=atten.employee_id,
                    name=Employee.query.filter_by(id=atten.employee_id).first().name,
                    year=atten.year_date,
                    attendance=score_,
                    contribution=0,
                    result=score_
                )
                db.session.add(tmp_)
                db.session.commit()
                atten.score = score_
                db.session.add(atten)
                db.session.commit()
            else:
                tmp.attendance += score_
                tmp.result += score_
                db.session.add(tmp)
                db.session.commit()
                atten.score = score_
                db.session.add(atten)
                db.session.commit()
        for contri in contributions:
            score_ = test.test_Contribution(contri.is_tool, contri.profit_level, contri.satistied_level)
            tmp = Tmp.query.filter_by(employee_id=contri.employee_id, year=contri.year_date).first()
            if tmp is None:
                tmp_ = Tmp(
                    employee_id=contri.employee_id,
                    name=Employee.query.filter_by(id=contri.employee_id).first().name,
                    year=contri.year_date,
                    attendance=0,
                    contribution=score_,
                    result=score_
                )
                db.session.add(tmp_)
                db.session.commit()
                contri.score = score_
                db.session.add(contri)
                db.session.commit()
            else:
                tmp.contribution += score_
                tmp.result += score_
                db.session.add(tmp)
                db.session.commit()
                contri.score = score_
                db.session.add(contri)
                db.session.commit()
        return redirect(url_for('.result'))
    flash(u'请确定模型是否训练完成!')
    return redirect(url_for('.employee'))
@main.route('/result', methods=['GET', 'POST'])
def result():
    emp = Employee.query.all()
    for emp_ in emp:
        atten = Attendance.query.filter_by(employee_id=emp_.id).all()
        for atten_ in atten:
            exists_ = Tmp.query.filter_by(employee_id=emp_.id, year=atten_.year_date).first()
            if exists_ is None:
                tmp = Tmp(
                    employee_id=emp_.id,
                    name=emp_.name,
                    year=atten_.year_date,
                    attendance=0,
                    contribution=0,
                    result=0)
                db.session.add(tmp)
                db.session.commit()
        contri = Contribution.query.filter_by(employee_id=emp_.id).all()
        for contri_ in contri:
            exists_ = Tmp.query.filter_by(employee_id=emp_.id, year=contri_.year_date).first()
            if exists_ is None:
                tmp = Tmp(
                    employee_id=emp_.id,
                    name=emp_.name,
                    year=atten_.year_date,
                    attendance=0,
                    contribution=0,
                    result=0)
                db.session.add(tmp)
                db.session.commit()
    year_ = request.form.get('year')
    name_ = request.form.get('name')
    if name_ is None and year_ is None:
        tmp_ = Tmp.query.all()
    if name_ != '' and name_ is not None and year_ != '' and year_ is not None:
        tmp_ = Tmp.query.filter_by(year=year_, name=name_).all()
    if  year_ != '' and name_ == '':
        tmp_ = Tmp.query.filter_by(year=year_).all()
    if name_ != '' and year_ == '':
        tmp_ = Tmp.query.filter_by(name=name_).all()
    return render_template('result.html', tmp=tmp_)
@main.route('/show_result', methods=['GET', 'POST'])
def show_result():
    trainset_atten = Trainset.query.filter_by(trainset_name='attendance').first()
    trainset_contri = Trainset.query.filter_by(trainset_name='contribution').first()
    attendance = Attendance.query.filter_by(employee_id=request.args.get('selectid'), year_date=request.args.get('selectyear')).all()
    contribution = Contribution.query.filter_by(employee_id=request.args.get('selectid'), year_date=request.args.get('selectyear')).all()
    return render_template('show_result.html', attendances=attendance, contributions=contribution, trainset_a=trainset_atten, trainset_c=trainset_contri)


@main.route('/pk_attendance', methods=['GET', 'POST'])
def pk_attendance():
    try:
        x = 0.0
        attendances = trainset_Attendance.query.all()
        for atten in attendances:
            score_ = test.test_Attendance(atten.absenteeism_level, atten.late_level, atten.leave_level)
            if atten.result == score_:
                x += 1
        result = (x/len(attendances)) * 100
        flash(u'正确率: %d' % result + '%')
        trainset = Trainset.query.filter_by(trainset_name='attendance').first()
        trainset.correct_rate = str(result) + '%'
        db.session.add(trainset)
        db.session.commit()
    except:
        flash(u"因缺少部分属性或属性特征,测试失败!")
    return redirect(url_for('.trainset_attendance'))
@main.route('/pk_contribution', methods=['GET', 'POST'])
def pk_contribution():
    try:
        x = 0.0
        contributions = trainset_Contribution.query.all()
        for contri in contributions:
            score_ = test.test_Contribution(contri.is_tool, contri.profit_level, contri.satistied_level)
            if contri.result == score_:
                x += 1
        result = (x / len(contributions)) * 100
        flash(u'正确率: %d' % result + '%')
        trainset = Trainset.query.filter_by(trainset_name='contribution').first()
        trainset.correct_rate = str(result) + '%'
        db.session.add(trainset)
        db.session.commit()
    except:
        flash(u"因缺少部分属性或属性特征,测试失败!")
    return redirect(url_for('.trainset_contribution'))