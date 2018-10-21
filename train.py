from model import cnn
# from vgg16 import model
from keras.callbacks import TensorBoard
import get_DataFlow as df
import os



os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

cnn.summary()

cnn.compile(optimizer='rmsprop', loss='binary_crossentropy', metrics=['accuracy'])

cnn.fit_generator(
    df.train_flow, steps_per_epoch=df.STEPS_PER_EPOCH, epochs=df.EPOCHS, verbose=1, validation_data=df.val_flow, validation_steps=100,
    callbacks=[
TensorBoard(log_dir='log_dir')]
)

cnn.save(df.output_model + '/simple_cnn_model.h5')
