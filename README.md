# EC601-Mini-Project-2
Deep Learning  

How To Use
---
For users who run this project for the first time:  
1. Please dowload all files to one folder you have created, then please put your images needed for building dataset into two different folders. In this project, the goal is to classify the cars and trucks, so you need to put all the cars images into a folder named 'car', and put all the trucks images you have gatherd into a folder named 'truck'. 
2. Please make sure that this two folder are in the same path as the codes downloaded in step 1. The path should be like the following example:  
![Image text](https://github.com/xiangl18/EC601-Mini-Project-2/raw/master/img_folder/unprocess_data.PNG)  
As it shows in unprocessed_images_example. 
3. Then please run the rename.py, and create_dataset.py, whcih will create a data set as:  
![Image text](https://github.com/xiangl18/EC601-Mini-Project-2/raw/master/img_folder/dataset_example.PNG)  
As it shows in dataset_example.  
The images are divided at the ratio of 80% trian, 10% test, 10% validation.
4. Based on the dataset you have built, you could use simple_cnn.py to train a model made by yourself with simplifed cnn layers. And you could also run the vgg16.py and mobilenet.py to train and then fine tuning the vgg16 and mobilenet which are pre-trained on imagenet dataset.  
5. The model are saved in the model_out folder, with which you could run eval.py and get the prediction result on classifying the images in test set. For example, the one of the test images is:  
![Image text](https://github.com/xiangl18/EC601-Mini-Project-2/raw/master/img_folder/car.368.jpg)  
For this iamge, when you run the eval.py with the fine-tuning resnet model, you will get the result, A label with possibility:  
```cmd  
[['cars', 0.6442234814167023]]  
```  
Result
---   
The tranning parameters are:  
```python  
BATH_SIZE = 32
EPOCHS = 100
STEPS_PER_EPOCH = image_numbers/BATH_SIZE  
```  
As it shows in get_DataFlow.py.  
I use images including 392 cars and 392 trucks to build the dataset.
1. The structure of simpel_cnn net is:  
![Image text](https://github.com/xiangl18/EC601-Mini-Project-2/raw/master/img_folder/simple_cnn.PNG)  
And the result of training for 100epoches on simple_cnn net is:  
2. The structure of mobilenet is:  
![Image text](https://github.com/xiangl18/EC601-Mini-Project-2/raw/master/img_folder/mobilenet.PNG) 
3. For the training result, the result of training on mobilenet before fine tune, I train for 100 epoches, is:  
![Image text](https://github.com/xiangl18/EC601-Mini-Project-2/raw/master/img_folder/mobilenet_val.PNG)  
The validation accuracy is 83.3%.
After we do the fine tuning, train for 30 epochs, and the result is :  
![Image text](https://github.com/xiangl18/EC601-Mini-Project-2/raw/master/img_folder/mobilenet_finetune_val.PNG)  
The validation accuracy is 83.3%.








