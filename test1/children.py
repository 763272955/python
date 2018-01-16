#-*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt
names1880 = pd.read_csv('D:\python\pydata-book-2nd-edition\datasets\\babynames\yob1880.txt',names=['name', 'sex',  'birth'])
print 'names1880 10 is ;\n',names1880[:10]
print 'names fen zu \n', names1880.groupby('sex').birth.sum()
years =range(1880,2011)
pieces = []
columns = ['name', 'sex', 'births']
for year in years:
    path = 'D:\python\pydata-book-2nd-edition\datasets\\babynames\yob%d.txt' % year
    frame = pd.read_csv(path,names=columns)
    frame['year'] = year
    pieces.append(frame)
names = pd.concat(pieces, ignore_index=True)
# print names[:10]
total_births = names.pivot_table('births', rows='year',cols='sex',aggfunc=sum)
print total_births.tail()
total_births[:10].plot(kind='barh',stacked=True)
# plt.show()
def add_prop(group):
    births = group.births.astype(float)
    group['prop'] = births / births.sum()
    return group
names = names.groupby(['year', 'sex']).apply(add_prop)
print 'names is \n',names