# library imports
import pandas as pd
import numpy as np
import joblib
import random
import os
from joblib import dump, load

from sklearn.preprocessing import OneHotEncoder, PowerTransformer
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.ensemble import BaggingRegressor

# Disabling warnings:
import warnings
warnings.filterwarnings('ignore') 


# Seeding:
def seed_all(seed): 
    ''' A function to seed everything for getting stable results and reproducibility'''
    random.seed(seed)
    np.random.seed(seed)
    os.environ['PYTHONHASHSEED'] = str(seed)

seed = 786    
seed_all(seed)

# Load data
data = pd.read_csv('bmw.csv')

# Transform value of categorical columns to remove any white spaces spaces
# Note that model column has leading white space
data['model'] = data['model'].apply(lambda x : x.strip().replace(' ', '_'))

# Merge Other and Electric
data['fuelType'] = data['fuelType'].replace({'Electric':'Other'})
# Construct new feature named age from year by subtracting year from 2022.
data['age'] = 2022 - data['year']
#remove the year as we have encode that value into age 
del data['year']

# get index of car to remove
idx_to_remove = data[data.price==123456].index
# drop the car
data.drop(idx_to_remove, inplace= True)
# reset index as we have removed some rows
data.reset_index(inplace=True, drop=True)

categorical_features = ['model', 'transmission', 'fuelType']
numerical_features = ['mileage', 'mpg', 'engineSize', 'age']

# Create a preprocessot that will apply One Hot Encoder for categorical variables and PowerTransformer for numerical features
preprocessor = ColumnTransformer(
    transformers=[
        ('num', PowerTransformer(method='yeo-johnson'), numerical_features),
        ('cat', OneHotEncoder(sparse_output=False,handle_unknown='ignore'), categorical_features)
    ])

# Split the data into features and target
X = data.drop('price', axis=1)
y = data['price']

# pre process the input features
X_train = preprocessor.fit_transform(X)

#save the pre processor for later use
joblib.dump(preprocessor, 'preprocessor.joblib')
print("----- Preprocessor Exported -----")

# See what the pre processed features look like
print(preprocessor.get_feature_names_out())

# Init a model using hyper parameters we select in previous notebook
model = BaggingRegressor(random_state=786, n_jobs=-1, max_features= 1.0, max_samples= 0.7, n_estimators= 50)

# fit the model on our data
model.fit(X_train, y)

# Save model
joblib.dump(model, 'model.joblib')
print("----- Model Exported -----")

#load packages
import sys #access to system parameters https://docs.python.org/3/library/sys.html
print("Python version: {}". format(sys.version))
print("pandas version: {}". format(pd.__version__))
print("NumPy version: {}". format(np.__version__))
import sklearn #collection of machine learning algorithms
print("scikit-learn version: {}". format(sklearn.__version__))
#Python version: 3.11.5 (main, Sep 11 2023, 13:54:46) [GCC 11.2.0]
#pandas version: 2.1.2
#NumPy version: 1.24.3
#scikit-learn version: 1.3.0