
# 5 August 2018
# Amani Abdullah
# CNN-MGP: Convolutional neural networks for Metagenomic Gene Prediction, 2018

import timeit
import numpy as np
np.random.seed(123)  # for reproducibility

 	
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Flatten
from keras.utils import np_utils
from keras.models import load_model
import h5py
from keras.layers import Dense, Dropout
from keras.layers import Embedding
from keras.layers import Conv1D, GlobalAveragePooling1D, MaxPooling1D, GlobalMaxPooling1D



model1 = load_model('cnn_part1.h5')
model2 = load_model('cnn_part2.h5')
model3 = load_model('cnn_part3.h5')
model4 = load_model('cnn_part4.h5')
model5 = load_model('cnn_part5.h5')
model6 = load_model('cnn_part6.h5')
model7 = load_model('cnn_part7.h5')
model8 = load_model('cnn_part8.h5')
model9 = load_model('cnn_part9.h5')
model10 = load_model('cnn_part10.h5')

# open writing file probability of ORFs encode gene
outfile = open('test_output.txt', 'w')


# read Test_orfSeqs_2528 file
f = h5py.File('Test_orfSeqs.mat')
x = f["x"]
x2=np.array(x)
x2 = np.ascontiguousarray(x2.swapaxes(1, 2))
print x2.shape

# read gc_2528 file
f = h5py.File('gc_2528.mat')
gc = f["gc"]
gc=np.array(gc)

print gc.shape
num_row=len(gc[0])
print num_row
pre=[]


for i in range(num_row):#
    GcR=gc[0,i]
# gc Range 1
    if GcR>=0 and GcR<0.3657:
      
       newdf=x2[ i, :, :]
       pred = model1.predict(newdf.reshape((1, 705, 4)),batch_size=1)
       #print(pred[0,1])#[0][1]
       num=pred[0,1]
       num=str(num)
       outfile.write(num +'\n')


# gc Range 2
    elif GcR>=0.3657 and GcR<0.4157:
       newdf=x2[ i, :, :]
       pred = model2.predict(newdf.reshape((1, 705, 4)),batch_size=1)
       #print(pred[0,1])#[0][1]
       num=pred[0,1]
       num=str(num)
       outfile.write(num +'\n')

# gc Range 3
    elif GcR>=0.4157 and GcR<0.46:
       newdf=x2[ i, :, :]
       pred = model3.predict(newdf.reshape((1, 705, 4)),batch_size=1)
       #print(pred[0,1])#[0][1]
       num=pred[0,1]
       num=str(num)
       outfile.write(num +'\n')


# gc Range 4
    elif GcR>=0.46 and GcR<0.5014:
       newdf=x2[ i, :, :]
       pred = model4.predict(newdf.reshape((1, 705, 4)),batch_size=1)
       #print(pred[0,1])#[0][1]
       num=pred[0,1]
       num=str(num)
       outfile.write(num +'\n')


# gc Range 5
    elif GcR>=0.5014 and GcR<0.5428:
       newdf=x2[ i, :, :]
       pred = model5.predict(newdf.reshape((1, 705, 4)),batch_size=1)
       #print(pred[0,1])#[0][1]
       num=pred[0,1]
       num=str(num)
       outfile.write(num +'\n')


# gc Range 6
    elif GcR>=0.5428 and GcR<0.5814:
       newdf=x2[ i, :, :]
       pred = model6.predict(newdf.reshape((1, 705, 4)),batch_size=1)
       #print(pred[0,1])#[0][1]
       num=pred[0,1]
       num=str(num)
       outfile.write(num +'\n')



# gc Range 7
    elif GcR>=0.5814 and GcR<0.6185:
       newdf=x2[ i, :, :]
       pred = model7.predict(newdf.reshape((1, 705, 4)),batch_size=1)
       #print(pred[0,1])#[0][1]
       num=pred[0,1]
       num=str(num)
       outfile.write(num +'\n')

# gc Range 8
    elif GcR>=0.6185 and GcR<0.65:
       newdf=x2[ i, :, :]
       pred = model8.predict(newdf.reshape((1, 705, 4)),batch_size=1)
       #print(pred[0,1])#[0][1]
       num=pred[0,1]
       num=str(num)
       outfile.write(num +'\n')


# gc Range 9
    elif GcR>=0.65 and GcR<0.6828:
       newdf=x2[ i, :, :]
       pred = model9.predict(newdf.reshape((1, 705, 4)),batch_size=1)
       #print(pred[0,1])#[0][1]
       num=pred[0,1]
       num=str(num)
       outfile.write(num +'\n')


# gc Range 10
    else: 
       newdf=x2[ i, :, :]
       pred = model10.predict(newdf.reshape((1, 705, 4)),batch_size=1)
       #print(pred[0,1])#[0][1]
       num=pred[0,1]
       num=str(num)
       outfile.write(num +'\n')






