import sqlite3

# Подключение к базе данных (файл будет создан, если не существует)
conn = sqlite3.connect('database.db')
cursor = conn.cursor()

# Создание таблицы "Товары"
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Товары (
        id INTEGER PRIMARY KEY,
        название TEXT,
        цена REAL,
        количество INTEGER,
        дата_добавления TEXT
    )
''')

cursor.execute("INSERT INTO Товары (название, цена, количество, дата_добавления) VALUES (?, ?, ?, ?)",
               ('Сахар', 2.10, 10, '12.10.2025'))

conn.commit()

cursor.execute("SELECT * FROM Товары")
rows = cursor.fetchall()
for row in rows:
    print(row)

conn.close()
