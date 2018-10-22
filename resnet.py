from keras.applications.resnet50 import ResNet50
from keras import models,layers,optimizers
from keras.callbacks import TensorBoard
import get_DataFlow as df
import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'


base_model = ResNet50(weights='imagenet', include_top=False, pooling='avg')
model = models.Sequential()
model.add(base_model)
model.add(layers.Dense(2, activation='softmax'))


model.summary()

model.compile(optimizer='rmsprop', loss='categorical_crossentropy', metrics=['accuracy'])

model.fit_generator(
      df.train_flow,
      steps_per_epoch=df.image_numbers // df.BATH_SIZE,
      epochs=df.EPOCHS,
      verbose=1,
      validation_data=df.val_flow,
      validation_steps=df.BATH_SIZE,
    callbacks=[TensorBoard(log_dir='log_dir3')])

model.save(df.output_model + '/resnet.h5')
