import sqlite3

conn = sqlite3.connect('my_database_1.db')

conn.execute("PRAGMA foreign_keys = ON")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS сотрудники(
id INTEGER PRIMARY KEY AUTOINCREMENT,
имя TEXT,
фамилия TEXT,
возраст INTEGER,
пол TEXT,
UNIQUE (имя, фамилия, возраст)
)
""")

cursor.execute("""CREATE TABLE IF NOT EXISTS клиенты(
id INTEGER PRIMARY KEY AUTOINCREMENT,
имя TEXT,
фамилия TEXT,
адрес TEXT,
телефон TEXT,
UNIQUE (имя, фамилия, телефон)
)
""")

cursor.execute("""CREATE TABLE IF NOT EXISTS продукты(
id INTEGER PRIMARY KEY AUTOINCREMENT,
название TEXT,
категория TEXT,
стоимость DECIMAL(10, 2) NOT NULL,
количество INTEGER,
UNIQUE (название, категория, стоимость)
)
""")

cursor.execute("""CREATE TABLE IF NOT EXISTS заказы(
id INTEGER PRIMARY KEY AUTOINCREMENT,
клиент_id INTEGER,
сотрудник_id INTEGER,
дата TEXT,
статус TEXT,
FOREIGN KEY (клиент_id) REFERENCES клиенты(id),
FOREIGN KEY (сотрудник_id) REFERENCES сотрудники(id)
)
""")

cursor.execute("""CREATE TABLE IF NOT EXISTS позиция_заказов(
id INTEGER PRIMARY KEY AUTOINCREMENT,
заказ_id INTEGER,
продукт_id INTEGER,
количество INTEGER,
стоимость REAL,
FOREIGN KEY (заказ_id) REFERENCES заказы(id),
FOREIGN KEY (продукт_id) REFERENCES продукты(id),
UNIQUE (заказ_id, продукт_id )
)
""")

сотрудники = [
    ('Иван', 'Иванов', 35, 'М'),
    ('Мария', 'Петрова', 28, 'Ж'),
    ('Андрей', 'Сидоров', 45, 'М'),
    ('Елена', 'Козлова', 31, 'Ж'),
    ('Дмитрий', 'Новиков', 40, 'М'),
    ('Ольга', 'Попова', 26, 'Ж'),
    ('Сергей', 'Волков', 38, 'М'),
    ('Анна', 'Смирнова', 33, 'Ж'),
    ('Николай', 'Федоров', 29, 'М'),
    ('Ирина', 'Морозова', 41, 'Ж')
]

клиенты = [
    ('Алексей', 'Смирнов', 'ул. Ленина, 10', '5551234'),
    ('Анна', 'Кузнецова', 'пр. Мира, 15', '444555678'),
    ('Борис', 'Соловьев', 'ул. Победы, 8', '333222111'),
    ('Виктория', 'Орлова', 'ул. Мира, 20', '5559876'),
    ('Григорий', 'Васильев', 'ул. Московская, 50', '5550001'),
    ('Дарья', 'Алексева', 'ул. Чехова, 70', '222333444'),
    ('Евгений', 'Зайцев', 'ул. Пушкина, 33', '555111222'),
    ('Жанна', 'Кириллова', 'пр. Ленина, 11', '999888777'),
    ('Захар', 'Морозов', 'ул. Гагарина, 5', '444555666'),
    ('Ирина', 'Николаева', 'ул. Лесная, 1', '555444333')
]

продукты = [
    ('Кофе Арабика', 'Напитки', 5.5, 100),
    ('Яблоки', 'Фрукты', 3.0, 200),
    ('Сахар', 'Продукты', 2.0, 150),
    ('Чай Зеленый', 'Напитки', 4.0, 80),
    ('Бананы', 'Фрукты', 2.5, 120),
    ('Кофе Растворимый', 'Напитки', 6.0, 90),
    ('Апельсины', 'Фрукты', 3.2, 110),
    ('Сыр', 'Молочные продукты', 8.0, 50),
    ('Сметана', 'Молочные продукты', 6.5, 60),
    ('Творог', 'Молочные продукты', 7.0, 70)
]

заказы = [
    (1, 1, '2023-01-15', 'готово'),
    (2, 2, '2023-02-10', 'в процессе'),
    (3, 3, '2023-03-05', 'готово'),
    (1, 4, '2022-12-25', 'готово'),
    (5, 5, '2022-12-30', 'в процессе'),
    (6, 6, '2023-01-20', 'готово'),
    (7, 7, '2023-04-15', 'отменен'),
    (8, 8, '2023-05-10', 'готово'),
    (9, 9, '2023-06-01', 'в процессе'),
    (10, 10, '2023-07-22', 'готово')
]

позиция_заказов = [
    (1, 1, 2, 5.5),
    (1, 2, 5, 3.0),
    (2, 3, 10, 2.0),
    (3, 4, 3, 4.0),
    (4, 5, 7, 2.5),
    (5, 6, 4, 6.0),
    (6, 7, 8, 3.2),
    (7, 8, 1, 8.0),
    (8, 9, 2, 6.5),
    (9, 10, 5, 7.0)
]

cursor.executemany("INSERT OR IGNORE INTO сотрудники(имя, фамилия, возраст, пол) Values(?, ?, ?, ?);", сотрудники)

cursor.execute("SELECT * FROM сотрудники")
rows = cursor.fetchall()
for row in rows:
    print(row)
cursor.executemany("INSERT OR IGNORE INTO клиенты (имя, фамилия, адрес, телефон) Values(?, ?, ?, ?);", клиенты)

cursor.execute("SELECT * FROM клиенты")
rows = cursor.fetchall()
for row in rows:
    print(row)
cursor.executemany("INSERT OR IGNORE INTO продукты (название, категория, стоимость, количество) Values(?, ?, ?, ?);",
                   продукты)

cursor.execute("SELECT * FROM продукты")
rows = cursor.fetchall()
for row in rows:
    print(row)
cursor.executemany("INSERT OR IGNORE INTO заказы (клиент_id, сотрудник_id, дата, статус) Values(?, ?, ?, ?);", заказы)

cursor.execute("SELECT * FROM заказы")
rows = cursor.fetchall()
for row in rows:
    print(row)
cursor.executemany(
    "INSERT OR IGNORE INTO позиция_заказов (заказ_id, продукт_id, количество, стоимость) Values(?, ?, ?, ?);",
    позиция_заказов)

cursor.execute("SELECT * FROM позиция_заказов")
rows = cursor.fetchall()
for row in rows:
    print(row)

conn.commit()
# Найдите сумму всех заказов для каждого клиента.
query = """
SELECT 
  клиенты.имя || ' ' || клиенты.фамилия AS клиент,
  SUM(позиция_заказов.стоимость * позиция_заказов.количество) AS сумма_заказов
FROM клиенты
JOIN заказы ON клиенты.id = заказы.клиент_id
JOIN позиция_заказов ON заказы.id = позиция_заказов.заказ_id
GROUP BY клиенты.id
ORDER BY сумма_заказов DESC;
"""

cursor.execute(query)
results = cursor.fetchall()

for клиент, сумма in results:
    print(f"{клиент} — {сумма}")

# Определите средний возраст всех сотрудников в компании.
cursor.execute("SELECT AVG(возраст) FROM сотрудники")
average_age = cursor.fetchone()[0]
print(f"Средний возраст: {average_age:.2f} лет")

# Подсчитайте общую стоимость всех продуктов на складе.
cursor.execute("SELECT SUM(стоимость * количество) FROM продукты")
total_cost = cursor.fetchone()[0]
print(f"Общая стоимость всех продуктов на складе: {total_cost:.2f}")

# запрос клиента с максимальным количеством заказов
cursor.execute("""
SELECT клиент_id, COUNT(*) AS количество_заказов 
FROM заказы 
GROUP BY клиент_id 
ORDER BY количество_заказов DESC 
LIMIT 1
""")

results = cursor.fetchone()
print(f"Клиент с ID {results[0]} имеет максимальное количество заказов: {results[1]}")

conn.close()
