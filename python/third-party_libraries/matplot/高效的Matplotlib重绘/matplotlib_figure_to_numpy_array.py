import numpy as np
import matplotlib.path as mpath
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt

Path = mpath.Path

fig, ax = plt.subplots()
pp1 = mpatches.PathPatch(
    Path([(0, 0), (1, 0), (1, 1), (0, 0)],
         [Path.MOVETO, Path.CURVE3, Path.CURVE3, Path.CLOSEPOLY]),
    fc="none", transform=ax.transData)

pp2 = mpatches.PathPatch(
    Path([(0, 0), (1, 0), (1, 1)],
         [Path.MOVETO, Path.CURVE3, Path.CURVE3]),
    fc="none", transform=ax.transData)

print (pp2, type(pp2))

# ax.add_patch(pp1)
ax_rst = ax.add_patch(pp2)
print (ax_rst.get_path(), type(ax_rst))
print (ax)
ax.plot([0.75], [0.25], "ro")
ax.set_title('The red point should be on the path')

plt.show()

import matplotlib.pyplot as plt
import pylab
import imageio
import skimage.io
import cv2
from io import StringIO
import PIL
#申请缓冲地址
buffer_ = StringIO()#using buffer,great way!
print ('buffer_', buffer_)
#保存在内存中，而不是在本地磁盘，注意这个默认认为你要保存的就是plt中的内容
plt.savefig('buffer_',format="png")
buffer_.seek(0)
#用PIL或CV2从内存中读取
dataPIL = PIL.Image.open(buffer_)
#转换为nparrary，PIL转换就非常快了,data即为所需
data = np.asarray(dataPIL)
cv2.imshow('image', data)
#释放缓存    
buffer_.close()



