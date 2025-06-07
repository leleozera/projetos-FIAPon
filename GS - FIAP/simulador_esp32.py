import sqlite3
import random
import datetime
import time

def init_db():
    conn = sqlite3.connect('leitura.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS leituras (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    temperature REAL,
                    humidity REAL,
                    timestamp TEXT
                )''')
    conn.commit()
    conn.close()

def salvar_leitura(temp, hum):
    conn = sqlite3.connect('leitura.db')
    c = conn.cursor()
    timestamp = datetime.datetime.now().isoformat()
    c.execute("INSERT INTO leituras (temperature, humidity, timestamp) VALUES (?, ?, ?)",
              (temp, hum, timestamp))
    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_db()
    while True:
        temp = random.uniform(25, 45)
        hum = random.uniform(15, 60)
        print(f"Salvando leitura: Temp={temp:.2f}°C, Humidade={hum:.2f}%")
        salvar_leitura(temp, hum)
        time.sleep(10)  # Salva uma leitura a cada 10 segundos
