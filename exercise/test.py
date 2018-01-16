# -*- coding:utf-8 -*-

import datetime

print (datetime.datetime.now() - datetime.timedelta(minutes=20)).strftime("%Y%m%d %H:%M")