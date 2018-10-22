from keras.preprocessing.image import ImageDataGenerator
import os


BATH_SIZE = 32
EPOCHS = 40
STEPS_PER_EPOCH = 100

base_path = os.getcwd()
path = os.path.join(base_path, 'dataset/')
train_dir = os.path.join(path, 'train/')
val_dir = os.path.join(path, 'validation/')
test_dir = os.path.join(path, 'test/')
output_model = os.path.join(base_path, 'model_output')


if (not os.path.exists(output_model)):
                    os.mkdir(output_model)

train_pic_gen = ImageDataGenerator(rescale=1./255, rotation_range=20, width_shift_range=0.2, height_shift_range=0.2,
                                     shear_range=0.2, zoom_range=0.5, horizontal_flip=True, fill_mode='nearest')


test_pic_gen = ImageDataGenerator(rescale=1./255)

train_flow = train_pic_gen.flow_from_directory(train_dir, (128, 128), batch_size=BATH_SIZE)

image_numbers = train_flow.samples

val_flow = test_pic_gen.flow_from_directory(val_dir, (128,128), batch_size=BATH_SIZE)

test_flow = test_pic_gen.flow_from_directory(test_dir, (128,128), batch_size=BATH_SIZE)
