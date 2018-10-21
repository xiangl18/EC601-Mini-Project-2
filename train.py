from model import cnn
from keras.callbacks import TensorBoard
from keras.preprocessing.image import ImageDataGenerator
import os



os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
base_path = os.getcwd()
output_model = os.path.join(os.getcwd(), 'model_output')
BATH_SIZE = 32
MAX_STEP = 100 # 训练的步数，应当 >= 10000
EPOCHS = 50
STEPS_PER_EPOCH = 100
LOG_DIR = os.path.join(os.getcwd(), 'tensorboard_output')

if (not os.path.exists(LOG_DIR)):
                    os.mkdir(LOG_DIR)
if (not os.path.exists(output_model)):
                    os.mkdir(output_model)


def get_flow():
    path = base_path + '/dataset'
    train_dir = path + '/train/'

    val_dir = path + '/test/'

    train_pic_gen = ImageDataGenerator(rescale=1./255, rotation_range=20, width_shift_range=0.2, height_shift_range=0.2,
                                     shear_range=0.2, zoom_range=0.5, horizontal_flip=True, fill_mode='nearest')

    test_pic_gen = ImageDataGenerator(rescale=1./255)

    train_flow = train_pic_gen.flow_from_directory(train_dir, (128, 128), batch_size = BATH_SIZE, class_mode='binary')

    val_flow = test_pic_gen.flow_from_directory(val_dir, (128,128), batch_size = BATH_SIZE, class_mode='binary')
    return train_flow, val_flow


cnn.summary()

cnn.compile(optimizer='rmsprop', loss='binary_crossentropy', metrics=['accuracy'])
train_flow, val_flow = get_flow()

cnn.fit_generator(
    train_flow, steps_per_epoch=STEPS_PER_EPOCH, epochs=EPOCHS, verbose=1, validation_data=val_flow, validation_steps=100,
    callbacks=[TensorBoard(log_dir='LOG_DIR')]

)

cnn.save(output_model + '/car_truck_model.h5')
