import psycopg2

connection = psycopg2.connect("host=localhost dbname=example user=postgres password=061010")

cursor = connection.cursor()

cursor.execute('DROP TABLE IF EXISTS table2;')

cursor.execute('''
    CREATE TABLE table2 (
        id INTEGER PRIMARY KEY,
        completed BOOLEAN NOT NULL DEFAULT False
    );
''')

cursor.execute('INSERT INTO table2 (id, completed) VALUES (%s, %s);', (1, True))

SQL = 'INSERT INTO table2 (id, completed) VALUES (%(id)s, %(completed)s);'

data = {'id':2, 'completed':True}

cursor.execute(SQL, data)

cursor.execute('INSERT INTO table2 (id, completed) VALUES (%s, %s);', (3, True))

cursor.execute('SELECT * FROM table2;')

result = cursor.fetchmany(2)
print('fetchmany(2)', result)

result2 = cursor.fetchone()
print('fetchone', result2)

result3 = cursor.fetchone()
print('fetchone', result3)

connection.commit()

connection.close()
cursor.close()
