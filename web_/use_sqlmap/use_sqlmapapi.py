# -*- coding:utf-8 -*-

import requests
import json
import time

class Use_SqlMapAPI(object):
    def __init__(self, server='', target='', data='', referer='', cookie=''):
        super(Use_SqlMapAPI, self).__init__()
        self.server = server
        self.target = target
        self.data = data
        self.referer = referer
        self.cookie = cookie
        self.taskid = ''
        self.time_start = time.time()

    # Create New task to scan
    def task_create(self):
        json_ = json.loads(requests.get(self.server + '/task/new').text)
        self.taskid = json_['taskid']
        success = json_['success']
        if success:
            print 'Created new task success: ' + self.taskid
            return True
        else:
            print 'Created new task Failed'
            return False

    #Delete task
    def task_delete(self):
        json_ = json.loads(requests.get(self.server + '/task/' + self.taskid + '/delete').text)
        print json_
        success = json_['success']
        if success:
            print 'Delete task success: %s' % self.taskid
            return True
        else:
            print 'Delete task Failed'

    #Set Options
    def options_set(self):
        headers = {'Content-Type': 'application/json'}
        options = {"options": {
            "smart": True
        }
        }
        url = self.server + '/option/' + self.taskid + '/set'
        result = json.loads(requests.post(url, data=json.dumps(options), headers=headers).text)
        print result

    #Start Scan
    def scan_start(self):
        headers = {'Content-Type': 'application/json'}
        payload = {'url': self.target}
        start = self.server+'/scan/'+self.taskid+'/start'
        json_ = json.loads(requests.post(start, data=json.dumps(payload), headers=headers).text)
        engineid = json_['engineid']
        success = json_['success']
        if len(str(engineid))>0 and success:
            print "Start Scan"
            return True
        return False

    #Stop Scan
    def scan_stop(self):
        json_ = json.loads(requests.get(self.server+'/scan/'+self.taskid+'/stop').text)
        success = json_['success']
        if success:
            print  'Stop scan Success'
            return True

    #Kill Scan
    def scan_kill(self):
        json_ = json.loads(requests.get(self.server+'/scan/'+self.taskid+'/kill').text)
        success = json_['success']
        if success:
            print 'Kill scan Success'

    #Status of Scan
    def scan_status(self):
        self.status = json.loads(requests.get(self.server + '/scan/' + self.taskid + '/status').text)['status']
        if self.status == "running":
            return "running"
        else:
            return "error"

    #Data of Scan
    def scan_data(self):
        self.data = json.loads(requests.get(self.server + '/scan/' + self.taskid + '/data').text)['data']
        if len(self.data) == 0:
            print 'not injection:\t'
        else:
            print 'injection:\t' + self.target

    # Run
    def run(self):
        if not self.task_create():
            return False
        self.options_set()
        if not self.scan_start():
            return False
        while True:
            if self.scan_status() == "running":
                time.sleep(10)
            else:
                break
            if time.time() - self.time_start > 3000:
                if self.scan_stop():
                    if self.scan_kill():
                        break
                    else:
                        print "Kill Failed!"
                else:
                    print "Stop Failed"
        self.scan_data()
        self.task_delete()

if __name__ == "__main__":
    SqlTask = Use_SqlMapAPI('http://127.0.0.1:8774', 'http://192.168.130.130:81/news/NewsDetails.aspx?Cat_ID=1&News_ID=1400')
    SqlTask.run()