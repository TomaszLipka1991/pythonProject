import sqlite3
import io
conn = sqlite3.connect('example.db')

c = conn.cursor()
# c.execute('''create table stocks (date text, trans text, symbol text, qty real, price real)''')
# c.execute("insert into stocks values('2022-02-07', 'buy', 'rhat', 100, 34.23)")
# c.execute("select * from stocks")
# conn.commit()
# conn.close()

# t = ('rhat',)
# c.execute('select * from stocks where symbol = ?', t)
# # print(c.fetchone())
# purchases = [
#     ('2021-11-23', 'buy', 'ibm', 1000, 45.00),
#     ('1999-09-20', 'sell', 'msft', 1000, 72.00),
#     ('2005-01-15', 'sell', 'ibm', 500, 53.00)
# ]
# c.executemany('insert into stocks values (?,?,?,?,?)', purchases)
# conn.commit()
# for row in c.execute ('select * from stocks order by price'):
#     print(row)
# print(type(c.execute ('select * from stocks order by price')))

# dump bazy danych
# with io.open('example_dump.sql', 'w') as f:
#     for line in conn.iterdump():
#         f.write('%s\n' % line)
# print('Kopia zapasowa została wykonana pomyslnie.')
# print('Zapisano jako example_dump.sql')
# conn.close()

