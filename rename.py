import os
import shutil

base_path = os.getcwd()
classes = {'car', 'truck'}  # set two classes

for index, name in enumerate(classes):
    i = 0
    class_path = base_path + '/' + name + '/'
    for item in os.listdir(class_path):
        if item.endswith('.jpg'):
            os.rename(os.path.join(class_path, item), os.path.join(class_path, (name + '.' + str(i) + '.jpg')))
            filePath = os.path.join(class_path, (name + '.' + str(i) + '.jpg'))
            newfile = base_path + '/images/' + name + '.' + str(i) + '.jpg'
            shutil.copyfile(filePath, newfile)
            i = i + 1
        else:
            continue