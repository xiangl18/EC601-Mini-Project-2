# EC601-Mini-Project-2
Deep Learning  

How To Use
---
For users who run this project for the first time:  
1. Please dowload all files to one folder you have created, then please put your images needed for building dataset into two different folders. In this project, our goal is to classify the cars and trucks, so we need to put all the cars images into a folder named 'car', and put all the trucks images we have gatherd into a folder named 'truck'. 
2. Please make sure that this two folder are in the same path as the codes downloaded in step 1. The path should be like the following example:  
![Image text](https://github.com/xiangl18/EC601-Mini-Project-2/raw/test_version2/img_folder/unprocess_data.PNG)  
As it shows in unprocessed_images_example. 
3. Then please run the rename.py, and create_dataset.py, whcih will create a data set as:  
![Image text](https://github.com/xiangl18/EC601-Mini-Project-2/raw/test_version2/img_folder/dataset_example.PNG)  
As it shows in dataset_example.  
4. Based on the dataset we have built, we could use simple_cnn.py to train a model made by myself with simplifed cnn layers. And we could also run the vgg16.py and resnet.py to fine tuning the vgg16 and resnet which are pre-trained on imagenet dataset.  
5. The model are saved in the model_out folder, with which we could run eval.py and get the prediction result on classifying the images in test set. For example, the one of the test images is:  
![Image text](https://github.com/xiangl18/EC601-Mini-Project-2/raw/test_version2/img_folder/car.368.jpg) 
For this iamge, when we run the eval.py with the fine-tuning resnet model, we will get the result:  
```cmd
[['cars', 0.6442234814167023]]  
```  
A label and possibility.

