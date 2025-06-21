import sqlite3
from datetime import datetime

conn = sqlite3.connect("sensores.db")
cursor = conn.cursor()

# Inserir dados fictícios
dados = [
    (datetime.now().strftime("%Y-%m-%d %H:%M:%S"), 1, 1, 6.8, 45.0, 0),
    (datetime.now().strftime("%Y-%m-%d %H:%M:%S"), 0, 1, 6.0, 30.0, 1),
    (datetime.now().strftime("%Y-%m-%d %H:%M:%S"), 1, 0, 5.4, 33.5, 1),
    (datetime.now().strftime("%Y-%m-%d %H:%M:%S"), 1, 1, 7.0, 55.0, 0),
    (datetime.now().strftime("%Y-%m-%d %H:%M:%S"), 0, 0, 7.4, 25.0, 1)
]

cursor.executemany('''
INSERT INTO leituras (timestamp, fosforo, potassio, ph, umidade, irrigacao_ativa)
VALUES (?, ?, ?, ?, ?, ?)
''', dados)

conn.commit()
conn.close()
print("Dados inseridos com sucesso.")
