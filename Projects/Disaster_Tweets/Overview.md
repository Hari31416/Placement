- [1. The Data Source](#1-the-data-source)
- [2. Aim of the Project](#2-aim-of-the-project)
- [3. Preparation of Dataset](#3-preparation-of-dataset)
  - [3.1. Cleaning the Text](#31-cleaning-the-text)
  - [3.2. Filling Null Values](#32-filling-null-values)
  - [3.3. Text to Vector](#33-text-to-vector)
    - [3.3.1. Tf-Idf](#331-tf-idf)
    - [3.3.2. Text Vectorization](#332-text-vectorization)
    - [3.3.3. Word Embedding](#333-word-embedding)
  - [3.4. Transfer Learning with USE](#34-transfer-learning-with-use)
  - [3.5. Making Training Faster](#35-making-training-faster)
- [4. The Performance Metrics](#4-the-performance-metrics)
- [5. Base Model](#5-base-model)
- [6. The Training Process](#6-the-training-process)
  - [6.1. Using just the `text` column](#61-using-just-the-text-column)
  - [6.2. Using the `text` and `keyword` Columns](#62-using-the-text-and-keyword-columns)
- [7. Fine Tuning Process](#7-fine-tuning-process)
- [8. Model Deployment, if any](#8-model-deployment-if-any)
- [9. Result](#9-result)
- [10. Question Section](#10-question-section)

# 1. The Data Source
The data is taken from Kaggle. It contains some tweets. Along with the tweet text, we have some more information like keyword and location. The tweets may or may not talk about a disaster happening. The various columns of the dataset are:
* id - a unique identifier for each tweet
* text - the text of the tweet
* location - the location the tweet was sent from (may be blank)
* keyword - a particular keyword from the tweet (may be blank)
* target - in train.csv only, this denotes whether a tweet is about a real disaster (1) or not (0)
* 
# 2. Aim of the Project
The goal is to predict whether a given tweet is about a real disaster or not. If so, predict a 1. If not, predict a 0. It is not always obvious, just by the words, whether the tweet is about a real disaster or not. So, training a model to do so will be a difficult task.

# 3. Preparation of Dataset
This is a dataset where the features are text. So, we have more steps than general to prepare the dataset. The preparation will be done in many steps:
## 3.1. Cleaning the Text
First step is to clean the texts. For this, many things can be done. Some steps, which I've performed are:
1. Lowercasing
2. Removing last `s` (only done in `keyword` column)
3. Removing `@user`
4. Removing the links
5. Removing non ASCII characters (like emojis)
6. Removing punctuation and special characters
7. Removing english stopwords

## 3.2. Filling Null Values
Some values are missing from the dataset, especially from the column `keyword` and `address`. The `address` column is not used in the final models as it is not very relavant and hence the column is simply dropped. The `keyword` column is more relavant and hence the missing values are filled with follwoing stretegy:
1. Make a list of all the keywords in the `keyword` column.
2. Loop thorough the `text` for which the `keyword` is null.
3. Search if there is a word in the text that is in the list of keywords.
4. If yes, fill the `keyword` column with that word else fill with some other special word.

## 3.3. Text to Vector
ML models requires numbers to work, they can not work on raw text data, even though they are cleaned and all. There are number of ways to convert a text to a vector. The methods I've used are as follow:
### 3.3.1. Tf-Idf
Tf-Idf is a method to convert text to vector. It is a combination of two methods:
1. Term Frequency (Tf)
2. Inverse Document Frequency (Idf)

This step is done for my base model, which is a Naive Bayes model trained on this Tf-Idf. However, the bulk of my modeling experiments revolve around DL models and there I've used other methods. They are given below.

### 3.3.2. Text Vectorization
I've used TensorFlow's `TextVectorization` layer to create a vector of the text. The max vocabulary size used is 10000 and the maximum length of words in a single example is 20. The `TextVectorization` layer added directly to the model.

### 3.3.3. Word Embedding
Next step is to create a word embedding using the text-vectors. I've used `Embedding` layer for this. The output dimension of the layer is 128. Same as before, the `Embedding` layer is added directly to the model.

## 3.4. Transfer Learning with USE
An alternative to creating and training our own word embedding is to use some already pretrained word embedding. This has the advantage of having more robust. I've used the Universal Sentence Encoder (USE) for this. The USE is a pretrained model that can be used to create a vector of a sentence. USE is a great word embedding in a way that it embedds two words which are Semantic similar are closer to each other in the embedding space. The model is available on tensorflow hub.

Both sentence level and character level encoding are performed using USE to train DL models.

## 3.5. Making Training Faster
I'm using Tensorflow for deep learning models. With GPU if we do some preprocessing to the dataset using the `tf.Data` API, the training time can be reduced significantly. Though, we have a very small dataset and we can go on without using these steps, I've done it anyway. In brief, these are the steps which are done to make the training faster:
1. Create Tensorflow Dataset from numpy array using `tf.data.Dataset.from_tensor_slices` and `tf.data.Dataset.zip`.
2. Batched the datasets with batch size of 64.
3. Used `prefetch` which prepares subsequent batches of data whilst other batches of data are being computed on.
4. Used `tf.data.AUTOTUNE` so that Tensorflow can figure out itself how many number of parallel calls it should make.

See the article [Better performance with the tf.data API](https://www.tensorflow.org/guide/data_performance)

# 4. The Performance Metrics
The dataset is not exactly balanced. However, it is not terribly imbalanced either. So, accuracy is a good metric to use. However, we will also use F1 score and AUC score. Kaggle uses accuracy to evaluate the submissions. So, accuracy will be our primary metric too.

# 5. Base Model
The base model is a Naive Bayes model. It is a simple model and is a good starting point. The model is trained on the Tf-Idf vector of the text. The model gives an accuracy of 0.79 and f1 score of 0.785 on the test set

# 6. The Training Process
As the base model is trained, I've moved to deep learning models. The input to models are text embeddings, first trained while training the NN network itself and then using a pretrained embedding model, the USE. I've experminented with a number of architectures involving the most successfull NN layers like Conv1D, LSTM, GRU, Bidirectional, etc. The models are trained on the GPU. The training process is as follow:
## 6.1. Using just the `text` column
This family of models were trained on just the `text` column. The `keyword` and `location` columns were not used. The models were trained on the sentence level encoding by using the USE. I used Fully connected layers, Conv1D, LSTM, GRU, as well as the bidirectional variant of the last two layers. The best model in this family gave an accuracy of 83.6% on train set. Surprsingly, this was as simple feed forward model.

## 6.2. Using the `text` and `keyword` Columns
Next set of experiments were performed using both the `text` and `keyword` columns. The `location` column was not used. For this, I created a multivariate model where there were two inputs, one for `text` and other for `keyword`. For `keyword`, character level encoding was performed.
# 7. Fine Tuning Process
How the best model and model before them were tuned for the best parameter.

# 8. Model Deployment, if any
The model is not deployed. However, the model is saved in the form of a tensorflow model. The model can be loaded and used for prediction.

# 9. Result

# 10. Question Section
Here, answer a few of the most asked questions about the project. Some questions are:

1. If you were to do something differently, what would that be?
2. If I were to change condition X in this project, how would your approach change?
3. What were the most challenging aspect of the project and how you overtook it?
4. Some mistakes you made.
5. What improvements can be made?
6. Why did this algorithm work or didn't work?
7. What were the most important features?
8. (Classification) Balanced or unbalanced classes?
9. What were the most important features?

