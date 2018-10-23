from keras.applications import MobileNet
from keras import models, layers, optimizers
from keras.callbacks import TensorBoard
import get_DataFlow as df
import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
EPOCHS = 30
conv_base = MobileNet(weights='imagenet', include_top=False, input_shape=(128, 128, 3))

model = models.Sequential()
model.add(conv_base)
model.add(layers.Flatten())
model.add(layers.Dense(256, activation='relu'))
model.add(layers.Dense(2, activation='sigmoid'))
path = df.output_model + '/mobilenet_use.h5'
model.load_weights(path)

conv_base.trainable = True
model.summary()

model.compile(optimizer=optimizers.adam(lr=1e-5), loss='binary_crossentropy', metrics=['accuracy'])


history = model.fit_generator(
    df.train_flow,
    steps_per_epoch=df.image_numbers // df.BATH_SIZE,
    epochs=EPOCHS,
    verbose=1,
    validation_data=df.val_flow,
    validation_steps=df.BATH_SIZE,
    callbacks=[TensorBoard(log_dir='log_dir4/2')])

model.save(df.output_model + '/mobilenet_fine_tune.h5')