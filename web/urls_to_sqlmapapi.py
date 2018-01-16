__author__ = 'AZONE'
import urllib
import urllib2
import json
import time
import os
def run_server():
    pass
    #os.system("python H:\zoomeye_spider\auto-pentest\sqlmap\sqlmapapi.py -s -p 8080")
def creat_task():
    try:
        url = 'http://127.0.0.1:8080/task/new'
        response = urllib2.urlopen(url)
        jdata = json.loads(response.read())
        taskid = str(jdata['taskid'])
    except:
        pass
    return taskid
'''
class task():
    def __int__(self,target_url):
        self.taskid = creat_task()
        self.url = target_url
    def get_status(self):
        url='http://127.0.0.1:8080/scan/'+self.taskid+'/status'
        response = urllib2.urlopen(url)
        print response.read()
    def get_log(self):
        url='http://127.0.0.1:8080/scan/'+self.taskid+'/log'
        response = urllib2.urlopen(url)
        print response.read()
    def get_data(self):
        url='http://127.0.0.1:8080/scan/'+self.taskid+'/data'
        response = urllib2.urlopen(url)
        print response.read()
    def task_start(self):
        url='http://127.0.0.1:8080/scan/'+self.taskid+'/start'
        value ={'url':self.url}
        i_headers = {'Content-Type':'application/json'}
        jdata = json.dumps(value)
        req = urllib2.Request(url, jdata,headers=i_headers)
        response = urllib2.urlopen(req)
        print response.read()
ret = #creat_task()
'''
def viewtask(taskid):
        url='http://127.0.0.1:8080/scan/'+taskid+'/log'
        response = urllib2.urlopen(url)
        return response.read()
def viewdata(taskid):
        url='http://127.0.0.1:8080/scan/'+taskid+'/data'
        response = urllib2.urlopen(url)
        return response.read()
def task_start(taskid,url):
    try:
        url='http://127.0.0.1:8080/scan/'+taskid+'/start'
        value ={'url':url}
        i_headers = {'Content-Type':'application/json'}
        jdata = json.dumps(value)
        req = urllib2.Request(url, jdata,headers=i_headers)
        response = urllib2.urlopen(req)
    except:
        pass
        return response.read()
def get_status(taskid):
        url='http://127.0.0.1:8080/scan/'+taskid+'/status'
        response = urllib2.urlopen(url)
        return response.read()
#print task_start(taskid,'http://www.hrbgtj.gov.cn//vote_result.jspx?voteId=20')




