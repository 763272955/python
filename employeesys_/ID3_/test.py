# -*- coding:utf-8 -*-

from employeesys_.app_sys.models import Trainset, Employee, Contribution, Attendance


def test_Attendance(absenteeism_level, late_level, leave_level):
    test = eval(Trainset.query.filter_by(trainset_name='attendance').first().trainset)
    while True:
        score = 0
        if 'absenteeism' in test.keys():
            node = 'perfect' if absenteeism_level == u'优' else 'miss'
            if type(test['absenteeism'][node]) == int:
                score = test['absenteeism'][node]
                break
            test = test['absenteeism'][node]
        if 'late' in test.keys():
            node = 'perfect' if late_level == u'优' else ('great' if late_level == u'良' else 'miss')
            if type(test['late'][node]) == int:
                score = test['late'][node]
                break
            test = test['late'][node]
        if 'leave' in test.keys():
            node = 'perfect' if leave_level == u'优' else ('great' if leave_level == u'良' else ('good' if leave_level == u'中' else 'miss'))
            if type(test['leave'][node]) == int:
                score = test['leave'][node]
                break
            test = test['leave'][node]
    return score

def test_Contribution(is_tool, profit_level, satistied_level):
    test = eval(Trainset.query.filter_by(trainset_name='contribution').first().trainset)
    while True:
        score = 0
        if 'tool' in test.keys():
            node = 'yes' if is_tool == u'是' else 'no'
            if type(test['tool'][node]) == int:
                score = test['tool'][node]
                break
            test = test['tool'][node]
        if 'profit' in test.keys():
            node = 'low' if profit_level == u'低' else ('high' if profit_level == u'中'else 'veryHigh')
            if type(test['profit'][node]) == int:
                score = test['profit'][node]
                break
            test = test['profit'][node]
        if 'satistied' in test.keys():
            node = 'good' if satistied_level == u'一般' else ('great' if satistied_level == u'满意' else 'perfect')
            if type(test['satistied'][node]) == int:
                score = test['satistied'][node]
                break
            test = test['satistied'][node]
    return score
# result_ = {}
# trainset_contribution = eval(Trainset.query.filter_by(trainset_name='contribution').first().trainset)
# trainset_attendance = eval(Trainset.query.filter_by(trainset_name='attendance').first().trainset)
# employee_ = Employee.query.all()
# if employee_ is not None:
#     for employee in employee_:
#         result_[employee.name]['contribution'] = {}
#         result_[employee.name]['attendance'] = {}
#         contribution = Contribution.query.filter_by(employee_id=employee.id).all()
#         attendance = Attendance.query.filter_by(employee_id=employee.id).all()
#         if contribution is not None:
#             for contri in contribution:
#                 if str(contri.year_date) not in result_[employee.name]['contribution'].keys():
#                     result_[employee.name]['contribution'][str(contri.year_date)] = {}
#             for contri in contribution:
#                 if str(contri.num) not in result_[employee.name]['contribution'][str(contri.year_date)].keys():
#                     test = trainset_contribution
#                     while True:
#                         grade = 0
#                         if 'tool' in test.keys():
#                             node = 'yes' if contri.is_tool == u'是' else 'no'
#                             if type(test['tool'][node]) == int:
#                                 grade = test['tool'][node]
#                                 break
#                             test = test['tool'][node]
#                         if 'profit' in test.keys():
#                             node = 'low' if contri.profit_level == u'低' else ('high' if contri.profit_level == u'中'else 'veryHigh')
#                             if type(test['profit'][node]) == int:
#                                 grade = test['profit'][node]
#                                 break
#                             test = test['profit'][node]
#                         if 'satistied' in test.keys():
#                             node = 'good' if contri.satistied_level == u'一般' else ('great' if contri.satistied_level == u'满意' else 'perfect')
#                             if type(test['satistied'][node]) == int:
#                                 grade = test['satistied'][node]
#                                 break
#                             test = test['satistied'][node]
#                     result_[employee.name]['contribution'][str(contri.year_date)][str(contri.num)] = grade
#         if attendance is not None:
#             for atten in attendance:
#                 if str(atten.year_date) not in result_[employee.name]['attendance'].keys():
#                     result_[employee.name][str(atten.year_date)] = {}
#             for atten in attendance:
#                 if str(atten.month_date) not in result_[employee.name]['attendance'][str(atten.year_date)].keys():
#                     test = trainset_attendance
#                     while True:
#                         grade = 0
#                         if 'absenteeism' in test.keys():
#                             node = 'yes' if atten.is_absenteeism == u'是' else 'no'
#                             if type(test['absenteeism'][node]) == int:
#                                 grade = test['absenteeism'][node]
#                                 break
#                             test = test['absenteeism'][node]
#                         if 'late' in test.keys():
#                             node = 'yes' if atten.is_late == u'是' else 'no'
#                             if type(test['late'][node]) == int:
#                                 grade = test['late'][node]
#                                 break
#                             test = test['late'][node]
#                         if 'leave' in test.keys():
#                             node = 'yes' if atten.is_leave == u'是' else 'no'
#                             if type(test['leave'][node]) == int:
#                                 grade = test['leave'][node]
#                                 break
#                             test = test['leave'][node]
#                         if 'sickleave' in test.keys():
#                             node = 'yes' if atten.is_sickleave == u'是' else 'no'
#                             if type(test['sickleave'][node]) == int:
#                                 grade = test['sickleave'][node]
#                                 break
#                             test = test['sickleave'][node]
#                         if 'over' in test.keys():
#                             node = 'yes' if atten.leave_day == u'是' else 'no'
#                             if type(test['over'][node]) == int:
#                                 grade = test['over'][node]
#                                 break
#                             test = test['over'][node]
#                     result_[employee.name]['attendance'][str(atten.year_date)][str(atten.month_date)] = grade