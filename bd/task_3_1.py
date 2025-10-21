
import sqlite3




conn = sqlite3.connect('database_2.db')
conn.execute("PRAGMA foreign_keys = ON")
cur = conn.cursor()


cur.executescript("""CREATE TABLE Employees (
    employee_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT,
    last_name TEXT,
    age INTEGER,
    gender TEXT,
    UNIQUE (first_name, last_name, age)
);

CREATE TABLE Customers (
    customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT,
    last_name TEXT,
    address TEXT,
    phone TEXT,
    UNIQUE (first_name, last_name, phone)
);

CREATE TABLE Products (
    product_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    category TEXT,
    price REAL,
    quantity INTEGER,
    UNIQUE (name, category, price)
);

CREATE TABLE Orders (
    order_id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id INTEGER,
    employee_id INTEGER,
    date TEXT,
    status TEXT,
    FOREIGN KEY (customer_id) REFERENCES Customers(customer_id),
    FOREIGN KEY (employee_id) REFERENCES Employees(employee_id),
   
);

CREATE TABLE OrderItems (
    order_item_id INTEGER PRIMARY KEY AUTOINCREMENT,
    order_id INTEGER,
    product_id INTEGER,
    quantity INTEGER,
    price REAL,
    FOREIGN KEY (order_id) REFERENCES Orders(order_id),
    FOREIGN KEY (product_id) REFERENCES Products(product_id),
    UNIQUE (order_id, product_id)
    
);
""")

employees = [
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

customers = [
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

products = [
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

orders = [
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

order_items = [
    (1, 1, 2, 5.5),
    (1, 2,5, 3.0),
    (2, 3, 10, 2.0),
    (3, 4, 3, 4.0),
    (4, 5, 7, 2.5),
    (5, 6, 4, 6.0),
    (6, 7, 8, 3.2),
    (7, 8, 1, 8.0),
    (8, 9, 2, 6.5),
    (9, 10, 5, 7.0)
]

cur.executemany("INSERT OR IGNORE INTO Employees VALUES (?, ?, ?, ?);", employees)
cur.executemany("INSERT OR IGNORE INTO Customers VALUES (?, ?, ?, ?);", customers)
cur.executemany("INSERT OR IGNORE INTO Products VALUES (?, ?, ?, ?);", products)
cur.executemany("INSERT OR IGNORE INTO Orders VALUES (?, ?, ?, ?);", orders)
cur.executemany("INSERT OR IGNORE INTO OrderItems VALUES (?, ?, ?, ?);", order_items)

conn.commit()
conn.close()



