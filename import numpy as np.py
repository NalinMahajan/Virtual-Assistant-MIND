import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
pic = Image.open('F:\SnapTube Video\Pahad photos\documents\IMG_20201231_155358.jpg').show()
print(type(pic))
pic_arr=np.asarray(pic)
print(type(pic_arr))
print(pic_arr,end='')
print(pic_arr.shape)
x=plt.imshow(pic_arr)
