import sqlite3

conn = sqlite3.connect('database_1.db')
conn.execute("PRAGMA foreign_keys = ON")  # поддержка внешних ключей сразу после подключения
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Сотрудники (
id INTEGER PRIMARY KEY AUTOINCREMENT,
Имя  TEXT,
Фамилия TEXT,
Возраст INTEGER,
Пол TEXT,
UNIQUE (Имя, Фамилия, Возраст)
)
''')

cursor.execute("INSERT OR IGNORE INTO Сотрудники (Имя, Фамилия, Возраст, Пол) "
               "VALUES (?, ?, ?, ?)", ("Иван", "Иванов", 22, "муж"))
cursor.execute("INSERT OR IGNORE INTO Сотрудники (Имя, Фамилия, Возраст, Пол) "
               "VALUES (?, ?, ?, ?)", ("Петр", "Петров", 24, "муж"))
cursor.execute("INSERT OR IGNORE INTO Сотрудники (Имя, Фамилия, Возраст, Пол) "
               "VALUES (?, ?, ?, ?)", ("Марья", "Марьина", 28, "жен"))
cursor.execute("INSERT OR IGNORE INTO Сотрудники (Имя, Фамилия, Возраст, Пол) "
               "VALUES (?, ?, ?, ?)", ("Виктор", "Викторов", 31, "муж"))
cursor.execute("INSERT OR IGNORE INTO Сотрудники (Имя, Фамилия, Возраст, Пол) "
               "VALUES (?, ?, ?, ?)", ("Галина", "Петрова", 32, "жен"))
cursor.execute("INSERT OR IGNORE INTO Сотрудники (Имя, Фамилия, Возраст, Пол) "
               "VALUES (?, ?, ?, ?)", ("Евгений", "Иванов", 22, "муж"))
conn.commit()

cursor.execute("SELECT * FROM Сотрудники")
rows = cursor.fetchall()
for row in rows:
    print(row)

cursor.execute('''
CREATE TABLE IF NOT EXISTS Клиенты (
id INTEGER PRIMARY KEY AUTOINCREMENT,
Имя  TEXT,
Фамилия TEXT,
Адрес TEXT,
Телефон TEXT,
UNIQUE (Имя, Фамилия, Телефон)

)
''')

cursor.execute("INSERT OR IGNORE INTO Клиенты (Имя, Фамилия, Адрес, Телефон) "
               "VALUES (?, ?, ?, ?)", ("Сидр", "Сидоров", 'Минск, пр. Победителей, 1', '8029-6555-555'))
cursor.execute("INSERT INTO Клиенты (Имя, Фамилия, Адрес, Телефон) "
               "VALUES (?, ?, ?, ?)", ("Анна", "Свиридова", 'Минск, пр. Победителей, 1', '8029-6111-111'))
cursor.execute("INSERT INTO Клиенты (Имя, Фамилия, Адрес, Телефон) "
               "VALUES (?, ?, ?, ?)", ("Семен", "Семенов", 'Минск, пр. Независимости, 11', '8029-6333-333'))
cursor.execute("INSERT INTO Клиенты (Имя, Фамилия, Адрес, Телефон) "
               "VALUES (?, ?, ?, ?)", ("Аркадий", "Баянов", 'Минск, ул. Кижеватова, 10', '8029-6222-222'))
cursor.execute("INSERT INTO Клиенты (Имя, Фамилия, Адрес, Телефон) "
               "VALUES (?, ?, ?, ?)", ("Егор", "Егоров", 'Минск, пр. Победителей, 11', '8029-6777-777'))
conn.commit()
cursor.execute("SELECT * FROM Клиенты")
rows = cursor.fetchall()
for row in rows:
    print(row)

cursor.execute('''
CREATE TABLE IF NOT EXISTS Продукты (
id INTEGER PRIMARY KEY AUTOINCREMENT,          
имя TEXT,                   
категория TEXT,                                    
стоимость DECIMAL(10, 2) NOT NULL,  
количество INTEGER NOT NULL,
UNIQUE (имя, категория, стоимость)
)
''')

cursor.execute("SELECT id FROM Продукты")
ids = cursor.fetchall()
print(ids)

cursor.execute(
    """INSERT OR IGNORE INTO Продукты(имя, категория, стоимость,
    количество) 
   VALUES (?, ?, ?, ?)""", ('сахар', '2_к', 50.5, 20))
cursor.execute(
    """INSERT INTO Продукты(имя, категория, стоимость,
    количество) 
   VALUES (?, ?, ?, ?)""", ('соль', '1_к', 10.5, 25))
cursor.execute(
    """INSERT INTO Продукты(имя, категория, стоимость,
    количество) 
   VALUES (?, ?, ?, ?)""", ('конфеты " Белочка"', 'высшая', 150.5, 15))
cursor.execute(
    """INSERT INTO Продукты(имя, категория, стоимость,
    количество) 
   VALUES (?, ?, ?, ?)""", ('конфеты "Зайчик"', 'высшая', 135.5, 20))
cursor.execute(
    """INSERT INTO Продукты(имя, категория, стоимость,
    количество) 
   VALUES (?, ?, ?, ?)""", ('Печенье', 'первая', 75.5, 50))
cursor.execute(
    """INSERT INTO Продукты(имя, категория, стоимость,
    количество) 
   VALUES (?, ?, ?, ?)""", ('напиток "Буратино"', 'средняя', 35.5, 100))
conn.commit()
cursor.execute("SELECT * FROM Продукты")
rows = cursor.fetchall()
for row in rows:
    print(row)

cursor.execute('''
CREATE TABLE IF NOT EXISTS Заказы (
id INTEGER PRIMARY KEY AUTOINCREMENT,
клиент_id INTEGER NOT NULL,
сотрудник_id INTEGER NOT NULL,
Дата TEXT NOT NULL,
Статус TEXT NOT NULL,
FOREIGN KEY (клиент_id) REFERENCES Клиенты(id),
FOREIGN KEY (сотрудник_id) REFERENCES Сотрудники(id),
UNIQUE (клиент_id, Статус)
)
''')

cursor.execute("""
    INSERT OR IGNORE INTO Заказы (клиент_id, сотрудник_id, Дата, Статус)
    VALUES (?, ?, ?, ?)
""", (1, 1, '2025-06-10', 'Новый'))

cursor.execute("""
    INSERT OR IGNORE INTO Заказы (клиент_id, сотрудник_id, Дата, Статус)
    VALUES (?, ?, ?, ?)
""", (3, 4, '2025-06-10', 'Новый'))
cursor.execute("""
    INSERT OR IGNORE INTO Заказы (клиент_id, сотрудник_id, Дата, Статус)
    VALUES (?, ?, ?, ?)
""", (4, 6, '2025-06-10', 'Просмотрен'))
conn.commit()
cursor.execute("SELECT * FROM Заказы")
rows = cursor.fetchall()
for row in rows:
    print(row)

cursor.execute('''
CREATE TABLE IF NOT EXISTS Позиции_заказа (
id INTEGER PRIMARY KEY AUTOINCREMENT,          
заказ_id INTEGER NOT NULL,                   
продукт_id INTEGER NOT NULL,                 
количество INTEGER NOT NULL,                   
стоимость DECIMAL(10, 2) NOT NULL,          
FOREIGN KEY (заказ_id) REFERENCES Заказы(id),
FOREIGN KEY (продукт_id) REFERENCES Продукты(id)
    )
''')

cursor.execute(
    """INSERT INTO Позиции_заказа(
    заказ_id, продукт_id, количество, стоимость)
    VALUES (?, ?, ?, ?)""", (1, 1, 2, 50.5))

cursor.execute(
    """INSERT INTO Позиции_заказа(
    заказ_id, продукт_id, количество, стоимость)
    VALUES (?, ?, ?, ?)""", (3, 3, 6, 150.5))
cursor.execute(
    """INSERT INTO Позиции_заказа(
    заказ_id, продукт_id, количество, стоимость)
    VALUES (?, ?, ?, ?)""", (2, 5, 20, 35.5))

conn.commit()
cursor.execute("SELECT * FROM Позиции_заказа")
rows = cursor.fetchall()
for row in rows:
    print(row)

conn.close()
