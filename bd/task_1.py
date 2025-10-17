import  sqlite3



conn = sqlite3.connect('example.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY,
        first_name TEXT,
        second_name TEXT,
        age INTEGER,
        groups TEXT
    )
''')
cursor.execute("INSERT INTO students (first_name, second_name, age, groups) VALUES (?, ?, ?, ?)",
               ('Иван', 'Иванов', 30, '123'))
conn.commit()

cursor.execute("SELECT * FROM students")
rows = cursor.fetchall()
for row in rows:
    print(row)

conn.close()