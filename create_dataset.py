import os
import shutil
import random

def train_test_split(total, trainval_percent, train_percent, set):
    num = len(total)
    list = range(num)
    tv = int(num * trainval_percent)
    tr = int(tv * train_percent)
    trainval = random.sample(list, tv)
    train = random.sample(trainval, tr)
    test_num = 0
    val_num = 0
    train_num = 0
    for i in list:
        name = total[i]
        if i in trainval:  # train and val set
            # ftrainval.write(name)
            if i in train:
                # ftrain.write(name)
                # print("train")
                # print(name)
                # print("train: "+name+" "+str(train_num))
                directory = "train"
                train_num += 1
                train_path1 = os.path.join(os.getcwd(), 'dataset/{}'.format(directory))
                train_path2 = os.path.join(train_path1, set)
                if (not os.path.exists(train_path1)):
                    os.mkdir(train_path1)
                if (not os.path.exists(train_path2)):
                    os.mkdir(train_path2)
                filePath = os.path.join(path, name)
                newfile = os.path.join(train_path2, os.path.basename(name))
                shutil.copyfile(filePath, newfile)

            else:
                # fval.write(name)
                # print("val")
                # print("val: "+name+" "+str(val_num))
                directory = "validation"
                val_num += 1
                validation_path1 = os.path.join(os.getcwd(), 'dataset/{}'.format(directory))
                validation_path2 = os.path.join(validation_path1, set)
                if (not os.path.exists(validation_path1)):
                    os.mkdir(validation_path1)
                if (not os.path.exists(validation_path2)):
                    os.mkdir(validation_path2)
                filePath = os.path.join(path, name)
                newfile = os.path.join(validation_path2, os.path.basename(name))
                shutil.copyfile(filePath, newfile)
                # print(name)
        else:  # test set
            # ftest.write(name)
            # print("test")
            # print("test: "+name+" "+str(test_num))
            directory = "test"
            test_num += 1
            test_path1 = os.path.join(os.getcwd(), 'dataset/{}'.format(directory))
            if (not os.path.exists(test_path1)):
                os.mkdir(test_path1)
            filePath = os.path.join(path, name)
            newfile = os.path.join(test_path1, os.path.basename(name))
            shutil.copyfile(filePath, newfile)
            # print(name)
    print("train total : " + str(train_num))
    print("validation total : " + str(val_num))
    print("test total : " + str(test_num))
    total_num = train_num + val_num + test_num
    print("total number : " + str(total_num))



path = os.getcwd() + "/images/"
saveBasePath = os.getcwd() + "/dataset/"
if (not os.path.exists(saveBasePath)):
    os.mkdir(saveBasePath)
trainval_percent = 0.9
train_percent = 0.89

cars = [path+i for i in os.listdir(path) if 'car' in i]
trucks = [path+i for i in os.listdir(path) if 'truck' in i]

train_test_split(cars, trainval_percent, train_percent, 'cars')
train_test_split(trucks, trainval_percent, train_percent, 'trucks')

