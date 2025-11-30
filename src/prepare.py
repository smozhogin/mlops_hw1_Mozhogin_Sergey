import os
import pandas as pd
from sklearn.model_selection import train_test_split
import yaml

with open('params.yaml', 'r') as f:
    params = yaml.safe_load(f)

test_size = params['prepare']['split_ratio']
random_state = params['prepare']['random_state']

raw_dataset_path = os.path.join('data', 'raw', 'iris.csv')
iris_df = pd.read_csv(raw_dataset_path)

X = iris_df.drop(columns=[iris_df.columns[-1]])
y = iris_df[iris_df.columns[-1]]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state, stratify=y)

train_df = pd.concat([X_train, y_train], axis=1)
test_df = pd.concat([X_test, y_test], axis=1)

train_path = os.path.join('data', 'processed', 'train.csv')
test_path = os.path.join('data', 'processed', 'test.csv')

train_df.to_csv(train_path, index=False)
test_df.to_csv(test_path, index=False)