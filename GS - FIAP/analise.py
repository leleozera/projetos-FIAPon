import sqlite3
import joblib
import pandas as pd
import time

clf = joblib.load('modelo_calor_extremo.pkl')

while True:
    conn = sqlite3.connect('leitura.db')
    c = conn.cursor()
    c.execute('SELECT temperature, humidity, timestamp FROM leituras ORDER BY id DESC LIMIT 1')
    row = c.fetchone()
    conn.close()

    if row:
        temperature, humidity, timestamp = row
        # Aqui cria o DataFrame:
        input_data = pd.DataFrame([[temperature, humidity]], columns=['temperature', 'humidity'])
        risk = clf.predict(input_data)[0]
        if risk == 1:
            print(f"{timestamp}: ALERTA! Risco de calor extremo: {temperature:.2f}°C / {humidity:.2f}%")
        else:
            print(f"{timestamp}: Temperatura normal: {temperature:.2f}°C / {humidity:.2f}%")
    else:
        print("Nenhum dado no banco ainda.")

    time.sleep(10)
