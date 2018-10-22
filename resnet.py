from keras.applications.resnet50 import ResNet50
from keras import models,layers,optimizers
from keras.callbacks import TensorBoard
import get_DataFlow as df
import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'


conv_base = ResNet50(weights='imagenet', include_top=False, pooling='avg')
model = models.Sequential()
model.add(conv_base)
model.add(layers.Dense(256, activation='relu'))
model.add(layers.Dense(2, activation='softmax'))
conv_base.trainable=False

model.summary()

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

model.fit_generator(
      df.train_flow,
      steps_per_epoch=df.image_numbers // df.BATH_SIZE,
      epochs=df.EPOCHS,
      verbose=1,
      validation_data=df.val_flow,
      validation_steps=df.BATH_SIZE,
    callbacks=[TensorBoard(log_dir='log_dir3')])

model.save(df.output_model + '/resnet.h5')
