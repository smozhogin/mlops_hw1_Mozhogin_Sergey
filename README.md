# Команды для воспроизведения пайплайна DVC+MLflow
```
virtualenv -p python3 mlops # Создаем виртуальную среду "mlops"
source mlops/bin/activate # Активируем виртуальную среду "mlops"
git clone https://github.com/smozhogin/mlops_hw1_Mozhogin_Sergey.git # Клонируем репозиторий GitHub
cd mlops_hw1_Mozhogin_Sergey # Меняем директорию
pip install -r requirements.txt # Устанавливаем зависимости
dvc pull # Выполняем pull DVC из Google Cloud Storage Bucket
dvc repro # Воспроизводим пайплайн у себя локально
mlflow ui --backend-store-uri sqlite:///mlflow.db # Открываем MLflow UI
```