# -*- coding:utf-8 -*-
import time
start = time.clock()
import sys
reload(sys)
sys.setdefaultencoding('gbk')
from mpl_toolkits.basemap import Basemap
from matplotlib.patches import Polygon
import matplotlib.pyplot as plt

fig = plt.figure()
ax1 = fig.add_axes([0.1,0.1,0.8,0.8])
map = Basemap(llcrnrlon=80.33,
              llcrnrlat=3.01,
              urcrnrlon=138.16,
              urcrnrlat=56.123,
             resolution='h', projection='cass', lat_0 = 42.5,lon_0=120,ax=ax1)

shp_info = map.readshapefile("CHN_adm1",'states',drawbounds=True) # CHN_adm1的数据是中国各省区域

for info, shp in zip(map.states_info, map.states):
    proid = info['NAME_1']  # 可以用notepad打开CHN_adm1.csv文件，可以知道'NAME_1'代表各省的名称
    if proid == 'Guangdong':
        poly = Polygon(shp,facecolor='g',edgecolor='c', lw=3) # 绘制广东省区域
        ax1.add_patch(poly)

map.shadedrelief() # 绘制阴暗的浮雕图

map.drawcoastlines()
end=time.clock()
print(end-start)
plt.show()