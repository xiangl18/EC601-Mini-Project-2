from keras.applications import VGG16
from keras import models,layers,optimizers
from keras.callbacks import TensorBoard
import get_DataFlow as df
import os



os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

conv_base = VGG16(weights='imagenet', include_top=False, input_shape=(128, 128, 3))
model = models.Sequential()
model.add(conv_base)
model.add(layers.Flatten())
model.add(layers.Dense(256, activation='relu'))
model.add(layers.Dense(2, activation='sigmoid'))

model.summary()

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

model.fit_generator(
      df.train_flow,
      steps_per_epoch=df.image_numbers // df.BATH_SIZE,
      epochs=df.EPOCHS,
      verbose=1,
      validation_data=df.val_flow,
      validation_steps=df.BATH_SIZE,
    callbacks=[TensorBoard(log_dir='log_dir2')])

model.save(df.output_model + '/vgg16.h5')





