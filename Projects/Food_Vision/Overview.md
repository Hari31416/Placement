- [1. The Data Source](#1-the-data-source)
- [2. Aim of the Project](#2-aim-of-the-project)
- [3. Preparation of Dataset](#3-preparation-of-dataset)
  - [3.1. Making Training Faster](#31-making-training-faster)
- [4. The Performance Metrics](#4-the-performance-metrics)
- [5. Base Model](#5-base-model)
- [6. The Training Process](#6-the-training-process)
- [7. Fine Tuning Process](#7-fine-tuning-process)
- [8. Model Deployment, if any](#8-model-deployment-if-any)
- [9. Result](#9-result)
- [10. Question Section](#10-question-section)
  - [10.1. If you were to do something differently, what would that be?](#101-if-you-were-to-do-something-differently-what-would-that-be)
  - [10.2. What were the most challenging aspect of the project and how you overtook it?](#102-what-were-the-most-challenging-aspect-of-the-project-and-how-you-overtook-it)
  - [10.3. What improvements can be made?](#103-what-improvements-can-be-made)
  - [10.4. Some Mistakes I've made](#104-some-mistakes-ive-made)
# 1. The Data Source
The data Food 101, available on [kaggle](https://www.kaggle.com/datasets/dansbecker/food-101) which is taken from the original [source](https://data.vision.ee.ethz.ch/cvl/datasets_extra/food-101/). However, for this project, I've used the `tensorflow_datasets` module to load the `food101` Dataset. The benefit by using this is that the dataset is already been preprocessed quite a bit and we need to do just some minor tweaking before it can be used to train DNN's. 

Food 101 contains 101 different categories of food having 1000 images each. `tensorflow_datasets` reshapes the images to 512x512x3. The images are in RGB format.

# 2. Aim of the Project
The aim of the project is to build a model that can classify the images of food into 101 different categories.

# 3. Preparation of Dataset
Not a lot is required as preprocessing because the `tensorflow_datasets` has done a lot of preprocessing already. Only things which I've done are:

1. Change the datatype of the images from `uint8` to `float32`
2. Reshape the images to 224x224x3.
3. Scale the images by dividing them by 255.0
   
Since this is a huge dataset, a number of steps are required to be taken to make the training process faster. The steps are:
## 3.1. Making Training Faster
I'm using Tensorflow for deep learning models. With GPU if we do some preprocessing to the dataset using the `tf.Data` API, the training time can be reduced significantly. Though, we have a very small dataset and we can go on without using these steps, I've done it anyway. In brief, these are the steps which are done to make the training faster:
1. Creating custom functions for train and test data to be used for preprocessing.
2. Batched the datasets with batch size of 64.
3. Used `prefetch` which prepares subsequent batches of data whilst other batches of data are being computed on.
4. Used `tf.data.AUTOTUNE` so that Tensorflow can figure out itself how many number of parallel calls it should make.

Apart from this, I've used mixed precision training, meaning that the model is trained using both the `float16` datatype and `float32` datatype. This is done to reduce the training time. Using mixed precision training can improve your performance on modern GPUs (those with a compute capability score of 7.0+) by up to 3x. For details see [TensorFlow mixed precision guide](https://www.tensorflow.org/guide/mixed_precision).
# 4. The Performance Metrics
The dataset has 101 categories and each category has 1000 samples meaning it is a balanced dataset. Thus, I've used accuracy.

# 5. Base Model
In this project, I utilized transfer learning from the very beginning. The base model is a feature extraction model which uses the [EfficientNetB0](https://www.tensorflow.org/api_docs/python/tf/keras/applications/efficientnet/EfficientNetB0) as backbone connected with `GlobalAveragePooling2D` and a dense output layer. The base model gives an accuracy of about 71.0% on test data.

# 6. The Training Process
In this project, I utilized transfer learning from the very beginning. I've experminted with the `EfficientNetB0`. The training process follows a feature extraction model which also is the base model followed by fine tuning of the base model. To check the progress of the training cycle, I've used a number of callbacks, some of them are:
1. `TensorBoard`
2. `ModelCheckpoint`
3. `EarlyStopping`
4. `ReduceLROnPlateau`

Apart from these model and callback related steps, I also tried using smaller amount of data to make the experimentations faster.

# 7. Fine Tuning Process
The base model uses the `EfficientNetB0` as backbone connected with `GlobalAveragePooling2D` and a dense output layer. The base model gives an accuracy of about 71.0% on test data. After that, fine tuning of the same is performed. For this
1. First, a small number of top layers of the model are trained.
2. Later, I've unfreezed all the layers of the model so that each layer can learn. The callback, `ReduceLROnPlateau` is used to reduce the learning rate once we don't see any change in loss.


# 8. Model Deployment, if any
The model is deployed on Streamlit as well as on heroku as a django app.
# 9. Result
The best model is fine tuned `EfficientNetB0` which gives an accuracy of 80.2% on test data. The model is deployed on Streamlit as well as on heroku as a django app.
# 10. Question Section
## 10.1. If you were to do something differently, what would that be?
The modeling experiments are done using the `EfficientNetB0` as backbone. I would like to try out other models as well. Especially, the `EfficientNetB7` which is the largest model in the EfficientNet family.

## 10.2. What were the most challenging aspect of the project and how you overtook it?
The dataset is over 5GB in size. Before this project, I'd worked with dataset which were very small compared to this. The hugeness of the dataset was creating problem with the experminenting cycle as one epoch was taking a lot of time. I overcame this by using the `tf.data` API and mixed precision training. I also tried smaller subset of the dataset, like 10% of it to make the cycle run faster.
## 10.3. What improvements can be made?
There are a number of improvements which can be made. Some are:
1. Use of other models like `EfficientNetB7` as backbone.
2. Using data augmentation to increase the size of the dataset.
3. Training for a longer time.

## 10.4. Some Mistakes I've made
1. I've used `tf.keras.applications.EfficientNetB0` as the base model. This model is trained on ImageNet dataset which has 1000 classes. Thus, I've used `include_top=False` to remove the top layer. But, I forgot to add the `GlobalAveragePooling2D` layer. This caused the model to give an accuracy of 0.0% on test data. I realized this mistake after a lot of time. I've used `EfficientNetB0` as the base model again and this time I've added the `GlobalAveragePooling2D` layer. This time the model gave an accuracy of 71.0% on test data.