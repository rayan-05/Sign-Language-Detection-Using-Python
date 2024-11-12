import pickle

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import numpy as np

data_dict=pickle.load(open('./data.pickle','rb'))

data = np.asarray(data_dict['data'])
labels = np.asarray(data_dict['labels'])
