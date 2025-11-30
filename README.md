# HW1. Создание воспроизводимого ML-pipeline с использованием DVC и MLflow
Автор: Можогин Сергей Сергеевич, Науки о данных, 30.11.2025

**Цели проекта:**
- Построить воспроизводимый пайплайн на основе Git, DVC и MLflow для версионирования кода и датасетов;
- Залогировать параметры, метрики, графики и модель при переборе гиперпараметров;
- Настройть хранилище DVC в Google Cloud Storage Bucket и воспроизвести пайплайн на другой локальной машине.

## Команды для воспроизведения пайплайна DVC+MLflow
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
По ссылке https://colab.research.google.com/drive/1XSXhI7wW2LteGqobKrCHso3CqrRV-A6a находится ноутбук Google Colab с публичным доступом, воспроизводящий необходимые команды на стороне клиента.