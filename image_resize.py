import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import os

from PIL import Image
from numpy import *
# SKLEARN
from sklearn.utils import shuffle


# input image dimensions
img_rows, img_cols = 64, 64

# number of channels
img_channels = 3

#%%
#  data

path1 = 'D:/5_Fruit_Disease_Detection/test/1'    #path of folder of images    
path2 = 'D:/5_Fruit_Disease_Detection/Dataset/test_set/1'  #path of folder to save images    

listing = os.listdir(path1)
num_samples=size(listing)
print(num_samples)

for file in listing:
    im = Image.open(path1 + '\\' + file)  
    img = im.resize((img_rows,img_cols))
    gray = img.convert(mode='RGB')
                #need to do some more processing here          
    gray.save(path2 +'\\' +  file, "JPG")

imlist = os.listdir(path2)

im1 = array(Image.open('input_data_resized/5/' + imlist[0])) # open one image to get size
m,n = im1.shape[0:2] # get the size of the images
imnbr = len(imlist) # get the number of images

# # create matrix to store all flattened images
# immatrix = array([array(Image.open('input_data_resized/'+ im2)).flatten()
#               for im2 in imlist],'f')
               
# label=np.ones((num_samples,),dtype = int)
# label[0:245]=0
# label[245:288]=1


# size(label)

