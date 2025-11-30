import os
import pandas as pd
import yaml
import pickle
import mlflow
import mlflow.sklearn
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

with open('params.yaml', 'r') as f:
    params = yaml.safe_load(f)

n_estimators_list = params['train']['n_estimators']
random_state = params['train']['random_state']

train_path = os.path.join('data', 'processed', 'train.csv')
test_path = os.path.join('data', 'processed', 'test.csv')

train_df = pd.read_csv(train_path)
test_df = pd.read_csv(test_path)

X_train = train_df.iloc[:, :-1]
y_train = train_df.iloc[:, -1]

X_test = test_df.iloc[:, :-1]
y_test = test_df.iloc[:, -1]

mlflow.set_tracking_uri('sqlite:///mlflow.db')

mlflow.set_experiment('Эксперимент с классификацией ирисов')

for d in ['models', 'plots']:
    os.makedirs(d, exist_ok=True)

for n in n_estimators_list:
    model = RandomForestClassifier(n_estimators=n, random_state=random_state)

    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    plot_path = os.path.join('plots', f'plot_{n}.png')

    plt.scatter(X_test.iloc[:, 0], X_test.iloc[:, 1], c=y_pred)
    plt.title('Результаты классификации Iris')
    plt.xlabel('Параметр 1')
    plt.ylabel('Параметр 2')
    plt.savefig(plot_path)

    acc = accuracy_score(y_test, y_pred)
    f1_weighted = f1_score(y_test, y_pred, average="weighted")
    precision_weighted = precision_score(y_test, y_pred, average="weighted")
    recall_weighted = recall_score(y_test, y_pred, average="weighted")

    model_path = os.path.join('models', f'model_{n}.pkl')

    with open(model_path, 'wb') as f:
        pickle.dump(model, f)

    with mlflow.start_run(run_name=f'RandomForestClassifier с n_estimators == {n}'):
        mlflow.log_param('model', 'RandomForestClassifier')
        mlflow.log_param('n_estimators', n)
        mlflow.log_metric('accuracy', acc)
        mlflow.log_metric('f1_weighted', f1_weighted)
        mlflow.log_metric('precision_weighted', precision_weighted)
        mlflow.log_metric('recall_weighted', recall_weighted)
        mlflow.log_artifact(plot_path, artifact_path='artifacts')
        mlflow.sklearn.log_model(model, artifact_path='sklearn_model')