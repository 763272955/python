# -*- coding:utf-8 -*-

def attendance_latelevel(late):
    if int(late) <1:
        return u'优'
    if int(late) <3:
        return u'良'
    return u'差'
def attendance_leavelevel(leave, sickleave):
    if int(leave) < 2:
        return u'优'
    if int(leave) < 4:
        if int(leave) - int(sickleave) <= 1:
            return u'良'
        return u'中'
    return u'差'
def attendance_absenteeismlevel(absenteeism):
    if int(absenteeism) >0:
        return u'差'
    return u'优'

def contribution_profitlevel(profit):
    if int(profit) < 1000:
        return u'低'
    if int(profit) < 5000:
        return u'中'
    else:
        return u'高'