#coding:utf-8

import sys
import json
import time
import mysql.connector
from flask import Flask, render_template, Blueprint, g, request, send_from_directory
from site_info_collect import runscan
from playsqlmap import start
import hashlib
app = Blueprint("trace", __name__)
'''
@app.before_request
def before_request():
    g.conn=mysql.connector.connect(user='root',password='root',host='127.0.0.1',database='autopentest')
    g.cur=g.conn.cursor()


@app.teardown_request
def tear_down(response):
    g.conn.close()
    return response
'''
@app.route("/trace", methods = ['GET' ,'POST'])
def trace():
	try:
		result_infos = {}
		target = request.form["target"]
		target_urllist,iplist,collect_dirs,collect_ports,subdomain = runscan(target)

		id = hashlib.md5()
		id.update(target)
		siteid = id.hexdigest()
		for url in target_urllist[0:10:1]:
			start(siteid,url)
			time.sleep(0.3)
	except:
		pass
	reload(sys)
	sys.setdefaultencoding('utf-8')
	return render_template("trace.html", target = target,target_urllist=target_urllist,iplist=iplist,collect_dirs=collect_dirs,collect_ports=collect_ports,subdomain=subdomain)
	#return render_template("trace.html")






