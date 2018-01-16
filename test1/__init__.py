import numpy as  np
import matplotlib
arr3d = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print 'arr3d is \n', arr3d
print 'arr3d[0] is \n ',arr3d[0]
ola_value = arr3d[0].copy()
print 'old', ola_value
arr3d[0] =42
print 'arr 3d  is \n ',arr3d
arr3d[0] = ola_value
print 'arr3d is \n', arr3d
print arr3d[1][0]