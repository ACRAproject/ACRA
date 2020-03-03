#!/usr/bin/env python
# coding: utf-8

# # Importing Libraries

# In[1]:


import os

import matplotlib as mpl
import matplotlib.pyplot as plt

import cv2
import pandas as pd
import numpy as np
import mahotas

from PIL import Image,ImageOps

from skimage.feature import hog
from skimage.color import rgb2grey

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.svm import SVC

from sklearn.metrics import roc_curve, auc


# # Image and Data Preprocessing and Feature Extraction

# ## Feature Extraction Functions

# In[2]:


def fd_hu_moments(image):
    feature = cv2.HuMoments(cv2.moments(image)).flatten()
    return feature

def fd_haralick(image): 
    # compute the haralick texture feature vector
    haralick = mahotas.features.haralick(image).mean(axis=0)
    return haralick

def create_features(img):
    # flatten three channel color image
    #color_features = img.flatten()
    # convert image to greyscale
    grey_image = rgb2grey(img)
    # get HOG features from greyscale image
    hog_features,hog_imgs = hog(grey_image, orientations=9, pixels_per_cell=(4, 4),cells_per_block=(2, 2),visualize=True)  #got total 324 features,after checking I wrote this.
    # combine all features into a single array
    hu_features = fd_hu_moments(img)  #Total 7 features
    haralick_features = fd_haralick(img)  #Total 13 features
    #print('no. of features => hog=',len(hog_features),', hu=',len(hu_features),', haralick=',len(haralick_features))
    flat_features = np.hstack([hog_features,hu_features,haralick_features])
    return flat_features


# In[3]:


def getImage(path):
    img = Image.open(path)
    img = ImageOps.fit(img,(64,64),Image.ANTIALIAS)
    img = np.array(img)
    return img

def getDF(path): #get DataFrame
    features_list=[]
    for file in os.listdir(path):
        path1 = os.path.join(path+file)
        img = getImage(path1)
        fr = create_features(img)
        features_list.append(fr)
    feature_matrix = np.array(features_list)
    return feature_matrix


# ### Preparing Training Set

# In[4]:


train1 = getDF('.\\train\\NORMAL\\')


# In[10]:


train1


# In[8]:


train1.shape


# In[11]:


pca = PCA(n_components=100)
train1 = pca.fit_transform(train1)


# In[12]:


train1.shape


# In[13]:


ss = StandardScaler()
train1 = ss.fit_transform(train1)


# In[14]:


label1 = np.array(['normal']*1341).reshape(-1,1) #1341 is no. of rows in train1
train1 = np.concatenate((train1,label1),axis=1)


# In[15]:


train1


# In[16]:


# Doing same operations to get train2(Pneumonia part)
train2 = getDF('.\\train\\PNEUMONIA\\')
pca = PCA(n_components=100)
train2 = pca.fit_transform(train2)
ss = StandardScaler()
train2 = ss.fit_transform(train2)


# In[17]:


train2.shape


# In[18]:


label2 = np.array(['pneumonia']*3592).reshape(-1,1) #3592 is no. of rows in train2
train2 = np.concatenate((train2,label2),axis=1)


# In[19]:


train2.shape


# In[20]:


train_set = np.concatenate((train1,train2),axis=0)


# In[21]:


train_set


# In[22]:


train_set.shape


# In[23]:


np.random.shuffle(train_set)


# In[22]:


train_set


# ## Preparing test set

# In[24]:


test1 = getDF('.\\test\\NORMAL\\')
pca = PCA(n_components=100)
test1 = pca.fit_transform(test1)
ss = StandardScaler()
test1 = ss.fit_transform(test1)


# In[25]:


test1.shape


# In[26]:


label1 = np.array(['normal']*234).reshape(-1,1) #234 is no. of rows in test1
test1 = np.concatenate((test1,label1),axis=1)


# In[27]:


test1


# In[28]:


test2 = getDF('.\\test\\PNEUMONIA\\')
pca = PCA(n_components=100)
test2 = pca.fit_transform(test2)
ss = StandardScaler()
test2 = ss.fit_transform(test2)


# In[29]:


test2.shape


# In[30]:


label2 = np.array(['pneumonia']*390).reshape(-1,1) #390 is no. of rows in test2
test2 = np.concatenate((test2,label2),axis=1)


# In[31]:


test2.shape


# In[32]:


test_set = np.concatenate((test1,test2),axis=0)


# In[33]:


test_set.shape


# In[34]:


test_set


# In[35]:


np.random.shuffle(test_set)  #so as to mix data


# In[36]:


test_set


# ### Now Our train_set and test_set is ready 

# ### Creating DataFrames from Numpy Arrays and then saving to CSV files

# In[37]:


train = pd.DataFrame(train_set)
test = pd.DataFrame(test_set)


# In[38]:


train.to_csv('train_set_new(1).csv')
test.to_csv('test_set_new(1).csv')


# In[39]:


train


# In[40]:


test


# In[41]:


X_train = train.iloc[:, :-1].values
Y_train = train.iloc[:,-1].values
X_test = test.iloc[:, :-1].values
Y_test = test.iloc[:,-1].values


# # Training a Kernel SVM model

# In[42]:


classifier = SVC(kernel = 'rbf')
classifier.fit(X_train, Y_train)


# ## Making prediction on test set

# In[46]:


Y_pred = classifier.predict(X_test)
Y_predTrain = classifier.predict(X_train)


# ## Evaluating Results

# In[47]:


from sklearn.metrics import accuracy_score
accuracy_score(Y_train, Y_predTrain)  #Training Accuaracy


# In[48]:


accuracy_score(Y_test, Y_pred)  #Testing Accuracy


# In[49]:


from sklearn.metrics import confusion_matrix
confusion_matrix(Y_test, Y_pred)


# In[50]:


confusion_matrix(Y_train, Y_predTrain)


# # Training a linear SVM model

# In[51]:


classifier = SVC(kernel = 'linear')
classifier.fit(X_train, Y_train)


# ## Making prediction on test set

# In[52]:


Y_pred = classifier.predict(X_test)
Y_predTrain = classifier.predict(X_train)


# ## Evaluating Results

# In[53]:


from sklearn.metrics import accuracy_score
accuracy_score(Y_train, Y_predTrain)  #Training Accuaracy


# In[54]:


accuracy_score(Y_test, Y_pred)  #Testing Accuracy


# In[55]:


from sklearn.metrics import confusion_matrix
confusion_matrix(Y_test, Y_pred)


# In[56]:


confusion_matrix(Y_train, Y_predTrain)


# # Training a KNN model

# In[57]:


from sklearn.neighbors import KNeighborsClassifier
classifier = KNeighborsClassifier(n_neighbors = 5, metric = 'minkowski', p = 2)
classifier.fit(X_train, Y_train)


# ## Making prediction on test set

# In[58]:


Y_pred = classifier.predict(X_test)
Y_predTrain = classifier.predict(X_train)


# ## Evaluating Results

# In[59]:


from sklearn.metrics import accuracy_score
accuracy_score(Y_train, Y_predTrain)  #Training Accuaracy


# In[60]:


accuracy_score(Y_test, Y_pred)  #Testing Accuracy


# In[61]:


from sklearn.metrics import confusion_matrix
confusion_matrix(Y_test, Y_pred)


# In[62]:


confusion_matrix(Y_train, Y_predTrain)


# In[ ]:




