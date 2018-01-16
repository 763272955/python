__author__ = 'AZONE'
from urls_to_sqlmapapi import creat_task,run_server,viewtask,viewdata,task_start,get_status
from save_to_mysql import addtask
'''newtask = task()
newtask.__int__('http://61.158.99.152/zzcx/search_sgxkz.jsp?xid=200705240303575851&workAction=Init')
newtask.task_start()
newtask.get_log()
newtask.get_status()'''
#print viewtask('dbbaf3c9dae3a970')
#print viewdata('dbbaf3c9dae3a970')
#get_status('dbbaf3c9dae3a970')
def start(siteid,url):
    taskid = creat_task()
    task_start(taskid,url)
    addtask(siteid,taskid,url)
#start('http://61.158.99.152/zzcx/search_sgxkz.jsp?xid=200705240303575851&workAction=Init')