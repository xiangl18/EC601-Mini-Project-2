from keras import models
import numpy as np
import cv2
import os
import get_DataFlow as df
import glob as gb


os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
def get_inputs(A):
    pre_x = []
    for s in A:
        input = cv2.imread(s)
        input = cv2.resize(input, (128, 128))
        input = cv2.cvtColor(input, cv2.COLOR_BGR2RGB)
        pre_x.append(input)
    pre_x = np.array(pre_x) / 255.0
    return pre_x

def put_prey(pre_y, label):
    output=[]
    for y in pre_y:
        if y[0]<0.5:
            output.append([label[0], 1-y[0]])
        else:
            output.append([label[1], y[0]])
    return output

load_path = os.path.join(df.output_model, 'simple_cnn_model.h5')

model = models.load_model(load_path)

pre_x = get_inputs(gb.glob(os.path.join(df.path, 'test/*.jpg')))

pre_y = model.predict(pre_x)

output = put_prey(pre_y,list(df.train_flow.class_indices.keys()))

print(output)
