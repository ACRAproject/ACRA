#!/usr/bin/env python
# coding: utf-8

# # Automated Chest Radiograph Analyser (ACRA) 

# ## Part01 - Building the CNN

# In[1]:


# Importing Keras libraries and packages
from keras.models import Sequential
from keras.layers import Convolution2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense


# ### Initialising the CNN

# In[2]:


classifier = Sequential()


# ### Step01 - Convolution

# In[3]:


classifier.add(Convolution2D(32, (3, 3), input_shape=(64,64,3), activation='relu'))


# ### Step02 - Pooling

# In[4]:


classifier.add(MaxPooling2D(pool_size=(2,2)))


# ### Adding a Second Convolutional Layer

# In[5]:


classifier.add(Convolution2D(32, (3, 3), activation='relu'))
classifier.add(MaxPooling2D(pool_size=(2,2)))


# ### Step03 - Flattening

# In[6]:


classifier.add(Flatten())


# ### Step04 - Full Connection

# In[7]:


classifier.add(Dense(output_dim=128, activation='relu'))
classifier.add(Dense(output_dim=1, activation='sigmoid'))


# ### Compiling the CNN

# In[8]:


classifier.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])


# ## Part02 - Fitting the CNN to the images

# In[9]:


from keras.preprocessing.image import ImageDataGenerator

#Below pixels are rescaled to have value b/w 0 and 1 and different modifications are performed
train_datagen = ImageDataGenerator(
        rescale=1./255,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True)

#Here only rescaling is done
test_datagen = ImageDataGenerator(rescale=1./255)


# ### Loading Data

# In[10]:


train_generator = train_datagen.flow_from_directory('train',
                                                    target_size=(64, 64),
                                                    batch_size=32,
                                                    class_mode='binary')

validation_generator = test_datagen.flow_from_directory('test',
                                                        target_size=(64, 64),
                                                        batch_size=32,
                                                        class_mode='binary')


# ### Fitting the CNN to data

# In[11]:


classifier.fit_generator(train_generator,
                        samples_per_epoch=5216,
                        nb_epoch=25,
                        validation_data=validation_generator,
                        nb_val_samples=624)


# In[13]:


classifier.save('classifier3.h5')


# In[ ]:




