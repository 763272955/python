#-*- coding: utf-8 -*-
import  pandas as pd

unames = ['user_id', 'gender', 'age', 'occupation', 'zip']
users = pd.read_table('C:\Users\cuipeng0207\Desktop\users.dat', sep='::', header=None, names=unames)
rnames = ['user_id', 'movie_id', 'rating', 'timestamp']
ratings = pd.read_table('C:\Users\cuipeng0207\Desktop\\ratings.dat', sep='::', header=None, names=rnames)
mnames = ['movie_id', 'title', 'genres']
movies = pd.read_table('C:\Users\cuipeng0207\Desktop\movies.dat', sep='::', header=None, names=mnames)
# print users[:5]
# print movies[:5]
# print ratings
data = pd.merge(pd.merge(ratings,users),movies)
data1 = pd.merge(pd.merge(ratings,movies),users)    #data1和data相同，关联list必须有相同title
print 'data is ',data
print 'data0 is', data.ix[0]
mean_ratings = data.pivot_table('rating', rows='title',cols='gender',aggfunc='mean')
print 'mean_rating5 is \n',mean_ratings[:5]
ratings_by_title = data.groupby('title').size()     #怎么额外加行标签？
print 'rating_by_title10 is \n', ratings_by_title[:10]
active_titles = ratings_by_title.index[ratings_by_title >= 250]
print 'active_titles is \n', active_titles
mean_ratings = mean_ratings.ix[active_titles]
print 'mean_ratings1 is \n', mean_ratings
top_female_ratings = mean_ratings.sort_index(by='F', ascending=False)       #降序排列
print 'top_female_ratings 10 is \n', top_female_ratings[:10]        #输出钱10的
mean_ratings['diff'] = mean_ratings['M'] - mean_ratings['F']
sorted_by_diff = mean_ratings.sort_index(by='diff')
print 'sorted_by_diff 10 is \n', sorted_by_diff[-15:]   #计算一部电影男女差别评分
rating_std_by_title =data.groupby('title')['rating'].std()
rating_std_by_title =rating_std_by_title.ix[active_titles]
print ' rating_std_by_title 10 is ', rating_std_by_title.order(ascending=False)[:10]


