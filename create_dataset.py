import os
import shutil
import random

def train_test_split(total, trainval_percent, train_percent):
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
                train_path = os.path.join(os.getcwd(), 'dataset/{}'.format(directory))
                if (not os.path.exists(train_path)):
                    os.mkdir(train_path)
                filePath = os.path.join(path, name)
                newfile = os.path.join(saveBasePath, os.path.join(directory, os.path.basename(name)))
                shutil.copyfile(filePath, newfile)

            else:
                # fval.write(name)
                # print("val")
                # print("val: "+name+" "+str(val_num))
                directory = "validation"
                validation_path = os.path.join(os.getcwd(), 'dataset/{}'.format(directory))
                if (not os.path.exists(validation_path)):
                    os.mkdir(validation_path)
                val_num += 1
                filePath = os.path.join(path, name)
                newfile = os.path.join(saveBasePath, os.path.join(directory, os.path.basename(name)))
                shutil.copyfile(filePath, newfile)
                # print(name)
        else:  # test set
            # ftest.write(name)
            # print("test")
            # print("test: "+name+" "+str(test_num))
            directory = "test"
            test_path = os.path.join(os.getcwd(), 'dataset/{}'.format(directory))
            if (not os.path.exists(test_path)):
                os.mkdir(test_path)
            test_num += 1
            filePath = os.path.join(path, name)
            newfile = os.path.join(saveBasePath, os.path.join(directory, os.path.basename(name)))
            shutil.copyfile(filePath, newfile)
            # print(name)
    print("train total : " + str(train_num))
    print("validation total : " + str(val_num))
    print("test total : " + str(test_num))
    total_num = train_num + val_num + test_num
    print("total number : " + str(total_num))



path = os.getcwd() + "/images/"
saveBasePath = os.getcwd() + "/dataset/"
trainval_percent = 0.9
train_percent = 0.89

dogs = [path+i for i in os.listdir(path) if 'dog' in i]
cats=[path+i for i in os.listdir(path) if 'cat' in i]

train_test_split(dogs, trainval_percent, train_percent)
train_test_split(cats, trainval_percent, train_percent)

