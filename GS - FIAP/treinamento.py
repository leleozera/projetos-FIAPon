import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

# Carregar dados
df = pd.read_csv('historico_calor.csv', sep=';')
X = df[['temperature', 'humidity']]
y = df['label']

# Treinar modelo
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
clf = RandomForestClassifier()
clf.fit(X_train, y_train)

# Salvar modelo
joblib.dump(clf, 'modelo_calor_extremo.pkl')
print('Modelo salvo com sucesso!')
print(f"Acurácia no teste: {clf.score(X_test, y_test):.2f}")
