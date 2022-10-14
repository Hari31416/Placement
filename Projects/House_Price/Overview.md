- [1. The Data Source](#1-the-data-source)
- [2. Aim of the Project](#2-aim-of-the-project)
- [3. Preparation of Dataset](#3-preparation-of-dataset)
  - [3.1. Data Cleaning](#31-data-cleaning)
  - [3.2. Feature Engineering](#32-feature-engineering)
  - [3.3. Preprocessing](#33-preprocessing)
    - [3.3.1. Label Encoding](#331-label-encoding)
    - [3.3.2. Normalization](#332-normalization)
    - [3.3.3. Outliers](#333-outliers)
    - [3.3.4. Train-Test Split](#334-train-test-split)
- [4. The Performance Metrics](#4-the-performance-metrics)
- [5. Base Model](#5-base-model)
- [6. The Training Process](#6-the-training-process)
  - [6.1. Models](#61-models)
- [7. Fine Tuning Process](#7-fine-tuning-process)
- [8. Model Deployment, if any](#8-model-deployment-if-any)
- [9. Final Result](#9-final-result)
- [10. Question Section](#10-question-section)
  - [10.1. If you were to do something differently, what would that be?](#101-if-you-were-to-do-something-differently-what-would-that-be)
  - [10.2. What were the most challenging aspect of the project and how you overtook it?](#102-what-were-the-most-challenging-aspect-of-the-project-and-how-you-overtook-it)
  - [10.3. What were some mistakes you made? How did you rectify them?](#103-what-were-some-mistakes-you-made-how-did-you-rectify-them)
  - [10.4. What Were the Most Important Features?](#104-what-were-the-most-important-features)
  - [10.5. What improvements would you make to your model in the future?](#105-what-improvements-would-you-make-to-your-model-in-the-future)
# 1. The Data Source
The data is taken from kaggle. The data is a part of Kaggle's getting started competitions. The dataset has 79 explanatory variables describing (almost) every aspect of residential homes in Ames, Iowa. Some of the columns in the dataset are:
<li><strong>SalePrice</strong> - the property's sale price in dollars. This is the target variable that you're trying to predict.</li>
<li><strong>LotFrontage</strong>: Linear feet of street connected to property</li>
<li><strong>Foundation</strong>: Type of foundation</li>
<li><strong>BsmtQual</strong>: Height of the basement</li>
<li><strong>Bedroom</strong>: Number of bedrooms above basement level</li>
<li><strong>Kitchen</strong>: Number of kitchens</li>
etc.

# 2. Aim of the Project
The aim of the project is to predict the price of the house using the given features.

# 3. Preparation of Dataset
## 3.1. Data Cleaning
The dataset contains lot of missing values in both train and the test set. A variety of methods are used to fill the missing values. The methods used are:
1. A lot of missing values in this dataset are because the facilty or object defined by that column does not exist in the house. Default value of "None" is used for all of them.
2. Some mising values are filed by the mode.
3. Some columns are filled by grouping using other columns and then filling them by the mean of the group.

## 3.2. Feature Engineering
Not a lot of feature engineering is done since there are already 80 features to work with. However, I've created some new features using the existing features. The new features are:
1. The age of the house
   
## 3.3. Preprocessing
### 3.3.1. Label Encoding
There are about 80 columns. And a lot of them are categorical. One hot encoding them will result in a lot of columns. So, I have used ordinal encoding for the categorical columns. I've used values from 0 to 5 for the different categories. 0 for the worst and 5 for the best. This results in not creation of new columns. This works because there are a lot of columns where comparative adjectives like "excellent", "good", "bad" are used. Of course, this does not work for all the columns. Other columns are dropped.

### 3.3.2. Normalization
Numerical columns, which has larger range are normalized using `StandardScaler`.

### 3.3.3. Outliers
The dataset does have some outliers. But, I've not removed them. I've tried removing them. But, it did not improve the performance of the model. Plus, we need to predict on all the test dataset and that dataset too has outliers. So, I've not removed them.

### 3.3.4. Train-Test Split
A 80-20 split is used for the train and the test set. I've used `train_test_split` from `sklearn.model_selection` which shuffles the data before splitting. So, we don't have data leakage.

# 4. The Performance Metrics
This is a regression task. The ideal metric for this is RMSE (Root Mean Squared Error). However, Kaggle has used RMSLE (The Root Mean Squared Log Error) for this competition. So, I've used that as well.

# 5. Base Model
The base model used is a simple linear regression with the default parameters given by `sklearn`. The RMSE and the RMSLE for the base model on test dataset are:
* RMSE: 32138.47833846781
* RMSLE: 0.1541983866756769
The base model now done, we are ready to move on to the next step.

# 6. The Training Process

## 6.1. Models
A polynomial model is fitted after the linear model. Elastic net is used to fit the model. After that, I've moved to more powerful algorithms.

# 7. Fine Tuning Process
To tune the model, I've used `GridSearchCV` from `sklearn.model_selection`. I've used 3-fold cross validation.

# 8. Model Deployment, if any
The model is not deployed.

# 9. Final Result
The best model gave an RMSLE score of 0.12384 on the Kaggle test set. This was placed in the top 15% of the leaderboard.

# 10. Question Section
## 10.1. If you were to do something differently, what would that be?
There are a couple of things that I would do differently:
1. First, I'll try different ratio for train-test split. I've used 90-10 split given the fact that the dataset is small. However, this gives a small dataset for training. Using a 80-20 split might give better results.
2. Second, a lot of categorical columns have been dropped. I might try coming with some other way to encode them. Not all of them are useful, of course, but some features might be useful.
3. Feature engineering is not done a lot. I might try to do more of it. 

## 10.2. What were the most challenging aspect of the project and how you overtook it?
The most challenging aspect of the project was to decide which features to use, escpecially the categotical features. There are a huge number of categorical variables in the dataset and there are a large number of diffrent category in each these features. Just doing a one hot encoding will not work well, this will result in over 300 columns which are not good as number of samples in the dataset are under 1500.

The solution to this problem is to use ordinal encoding. There are a lot of columns where comparative adjectives like "excellent", "good", "bad" are used. All these adjectives give a send of order to these categories. So, I used number from 0 to 6 to encode this sense of order. After that, the features are used just as any numerical columns are used. Of course, this does not work for all the columns and I did drop some of the columns.

## 10.3. What were some mistakes you made? How did you rectify them?
I spent a lot of time fitting a polynomial model of degree 2 using the `ElaticNet` model. However, it was performing poorer than even the base model. It turned out that this dataset is not a good fit for polynomial models. So, I dropped the polynomial model and moved on to more powerful models.

## 10.4. What Were the Most Important Features?
Here are the five most important features as given by the `RandomForestRegressor` model:

`OverallQual`, `GrLivArea`, `GarageCars`, `ExterQual`, `TotalBsmtSF`

While the `XGBoost` model gives the following features as the most important:

`OverallQual`, `GarageCars`, `TotRmsAbvGrd`, `BsmtQual`, `GrLivArea`

## 10.5. What improvements would you make to your model in the future?
The model is not using all the features. Also, feature engineering is not done rigorously. This is something that I would like to improve in the future. I would also like to try some different models and see how they perform. Finally, it would be good idea to deploy the model, using django or Streamlit.

