import sqlite3

conn = sqlite3.connect("database/sensores.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS leituras (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp TEXT NOT NULL,
    fosforo INTEGER NOT NULL,
    potassio INTEGER NOT NULL,
    ph REAL NOT NULL,
    umidade REAL NOT NULL,
    irrigacao_ativa INTEGER NOT NULL
)
""")

conn.commit()
conn.close()
print("Tabela 'leituras' criada com sucesso!")

