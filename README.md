# Команды для воспроизведения пайплайна DVC+MLflow
```
virtualenv -p python3 mlops
source mlops/bin/activate
git clone https://github.com/smozhogin/mlops_hw1_Mozhogin_Sergey.git
cd mlops_hw1_Mozhogin_Sergey
pip install -r requirements.txt
dvc pull
dvc repro
```