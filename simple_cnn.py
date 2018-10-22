from keras.callbacks import TensorBoard
import get_DataFlow as df
import os


os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

model = Sequential([
    Convolution2D(32, 3, 3, input_shape=(128, 128, 3),activation='relu'),
    MaxPool2D(pool_size=(2, 2)),
    Convolution2D(64, 3, 3, input_shape=(128, 128, 3),activation='relu'),
    MaxPool2D(pool_size=(2, 2)),
    Flatten(),
    Dense(64, activation='relu'),
    Dropout(0.5),
    Dense(2, activation='sigmoid')
])

model.summary()

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

model.fit_generator(
      df.train_flow,
      steps_per_epoch=df.image_numbers // df.BATH_SIZE,
      epochs=df.EPOCHS,
      verbose=1,
      validation_data=df.val_flow,
      validation_steps=df.BATH_SIZE,
    callbacks=[TensorBoard(log_dir='log_dir')])

model.save(df.output_model + '/simple_cnn_model.h5')
