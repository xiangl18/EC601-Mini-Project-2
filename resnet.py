from keras.models import Model
from keras.layers import Dense
from keras.applications.resnet50 import ResNet50
from keras.preprocessing.image import ImageDataGenerator
from keras.callbacks import TensorBoard
import get_DataFlow as df
import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'


base_model = ResNet50(weights='imagenet', include_top=False, pooling='avg')
predictions = Dense(2, activation='softmax')(base_model.output)
model = Model(inputs=base_model.input, outputs=predictions)

model.compile(optimizer='rmsprop', loss='categorical_crossentropy')


# model.fit_generator(train_generator,
#                     steps_per_epoch=image_numbers // batch_size,
#                     epochs=epochs,
#                     validation_data=validation_generator,
#                     validation_steps=batch_size,
#                   callbacks=[TensorBoard(log_dir='log_dir3')])

model.fit_generator(
      df.train_flow,
      steps_per_epoch=df.image_numbers // df.BATH_SIZE,
      epochs=df.EPOCHS,
      verbose=1,
      validation_data=df.val_flow,
      validation_steps=df.BATH_SIZE,
    callbacks=[TensorBoard(log_dir='log_dir3')])

model.save(df.output_model + '/resnet.h5')

