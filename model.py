from keras.models import Sequential
from keras.layers import Convolution2D,MaxPool2D,Flatten,Dense,Dropout

cnn = Sequential([
    Convolution2D(32,3,3,input_shape=(128,128,3),activation='relu'),
    MaxPool2D(pool_size=(2,2)),
    Convolution2D(64,3,3,input_shape=(128,128,3),activation='relu'),
    MaxPool2D(pool_size=(2,2)),
    Flatten(),
    Dense(64,activation='relu'),
    Dropout(0.5),
    Dense(1,activation='sigmoid')
])


