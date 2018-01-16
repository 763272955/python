# -*- coding:utf-8 -*-

import os
import time
import shutil
import datetime
from _data_operat import Data_Operat
from _daily_operat import Daily_Operat
import _excel_creat

def dir_Create(time):
    try:
        if os.path.exists('outputFile/' + time):
            shutil.rmtree('outputFile/' + time)
        os.mkdir('outputFile/' + time)
        print time + u" 目录创建成功!"
        return
    except TypeError:
        print TypeError
        print time + u" 目录创建失败!"
        raise exit()

if __name__ == "__main__":
    strat_time = time.time()
    time_ = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime('%Y%m%d')
    dir_Create(time_)
    _excel_creat.Excel_Creat(time_).run()
    # Daily_Operat().run(time_)
    # end_time = time.time()
    # print end_time - strat_time