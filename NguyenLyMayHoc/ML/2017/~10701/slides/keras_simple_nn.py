
# coding: utf-8

# **NOTE:** This tutorial uses a Jupyter notebook environment with a Python 2 kernel. I suggest downloading and installing Anaconda distribution (https://anaconda.org/anaconda/python) of Python 2 and learning how to launch Jupyter notebooks from the documentation. It is relatively straightforward and should be easy to learn. We use Keras for implementing a basic neural network.
# 
# **NOTE:** This tutorial assumes you are familiar with basic Python usage

# ### Model
# We will train a neural network model on the gene expression data from HW5 using Keras (https://keras.io/). The data is already split into train and validation sets and stored in numpy array format on disk

# ### Loading in the data
# These are numpy arrays saved to disk using np.save()

# In[ ]:

import numpy as np


# In[ ]:

Xtrain = np.load('Xtrain.npy')
Ytrain = np.load('Ytrain.npy')
Xvalid = np.load('Xvalid.npy')
Yvalid = np.load('Yvalid.npy')


# In[ ]:

print type(Xtrain)
print type(Ytrain)


# **NOTE**: The labels are one-hot-encoded numpy arrays

# In[ ]:

print Ytrain.shape
print Yvalid.shape


# ## Model architecture

# <img src="nn.png" alt="Drawing" style="width: 300px;"/>

# # Importing the Keras functionality that we need.
# * Sequential = Feed forward neural network
# * Dense = fully connected layer.
# * Activation = setting activations of hidden layers

# In[ ]:

from keras.models import Sequential
from keras.layers import Dense, Activation


# ### Defining the network in Keras

# In[ ]:

numFeatures = Xtrain.shape[1]
numLabels = Ytrain.shape[1]

model = Sequential()
model.add(Dense(100, input_shape=(numFeatures,)))
model.add(Activation('tanh'))
model.add(Dense(numLabels))
model.add(Activation('softmax'))

model.compile(optimizer='sgd',
              loss='categorical_crossentropy',
              metrics=['accuracy'])


# **TIP**: Play around with these hyperparameters in a systematic way. Tweak learning rate, mini-batch size, activation functions etc

# In[ ]:

model.summary()


# In[ ]:

history = model.fit(x=Xtrain,
          y=Ytrain,
          batch_size=32,
          epochs=3,
          verbose=1,
          validation_data=(Xvalid,Yvalid),
          shuffle=True)


# In[ ]:

for val in history.history:
    print val, history.history[val]


# #### TIP: Look at your learning curves
# Plot training and validation loss against epoch number to see how your model is learning

# #### TIP: Always save your model parameters so that you can refer back to them later

# In[ ]:

model.save_weights('mlp_new_weights.hdf5')


# ### Loading pretrained model

# In[ ]:

model.load_weights('mlp_old_weights.hdf5')


# In[ ]:

predTrain = model.predict_classes(Xtrain)
predValid = model.predict_classes(Xvalid)


# In[ ]:

print predTrain


# In[ ]:

trainAccuracy = 1.0*np.sum(predTrain==np.argmax(Ytrain,axis=1))/predTrain.size
validAccuracy = 1.0*np.sum(predValid==np.argmax(Yvalid,axis=1))/predValid.size
print trainAccuracy
print validAccuracy


# In[ ]:

maxClassValidPercentage = np.max(np.sum(Yvalid,axis=0))/np.sum(Yvalid)
maxClassTrainPercentage = np.max(np.sum(Ytrain,axis=0))/np.sum(Ytrain)
print maxClassTrainPercentage
print maxClassValidPercentage


# ### Metrics to use:
# 
# <ul>
#   <li>0-1 Accuracy</li>
#   <li>Compare with majority Class Percentage</li>
#   <li>Plot the learning curve to see if you're overfitting</li>
#   <li>Area Under Receiver Operating Characteristic (auROC) curve</li>
#   <li>Area Under Precision Recall Curve (AUPR) - Useful when there are imbalanced classes</li>
#   <li>F1-Score = PR/(P+R)</li>
#   <li>Confusion Matrix - visualize which labels are confusing for the model</li>
# </ul>
# #### All of these can be found in scikitlearn or other toolboxes or easily implemented by self

# #### Tips
# * If you have not started, then start ASAP. There is lot of engineering effort involved even in getting the data into the right formats that can be read in by classifiers.
# * Use standard format for data (numpy array/MATLAB matrix) so that workflow is optimized
# * **Data splitting method is important**
# * Debug your models on a small subset of the data
# * You could try to pick model architecture by looking at overfitting on a small subset of the data
# * Train on the full set after that and then do hyperparameter search if needed
# * Always save your model parameters so that you can go back to them when needed
# * Learning rate is usually the first hyperparameter that you should try to tune
# * Document hyperparameter searches in a systematic way (maintain a spreadsheet/table)

# ### Other Libraries and Toolboxes (Also check Piazza)
# * Alternative neural network toolboxes with GPU support - tensorflow, theano, torch/pytorch
# * General Machine Learning toolboxes - scikitlearn (Python), shogun (Python, R, Octave) - implementations of most typical classifiers, clustering algorithms including model evaluation metrics
# * Saving objects, loading/unloading data - numpy.save, numpy.load, pickle, .mat format, pandas.read_table, readr::read_tsv, data.table::fread, saveRDS
# * Plotting - matplotlib/seaborn (Python), ggplot2 (R, Python), plotly (general)
# * Command line tools - head, tail, less -S, more, awk, cat
