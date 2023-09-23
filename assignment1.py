import sqlite3
import re

xxx = sqlite3.connect('emaildb.sqlite')
cur = xxx.cursor()
cur.execute('DROP TABLE IF EXISTS Counts')
cur.execute('CREATE TABLE Counts(org TEXT,count INTEGER)')


with open('mbox.txt', 'r') as files:
    file = files.readlines()
    for line in file:
        org = re.findall('From \S+@(\S+)', line)
        if org:
            cur.execute('SELECT count FROM Counts WHERE org = ?', (org[0],))
            row = cur.fetchone()
            if row is None:
                cur.execute('INSERT INTO Counts(org, count) VALUES (?, 1)', (org[0],))
            else:
                cur.execute('UPDATE Counts SET count = count +1 WHERE org = ?', (org[0],))
        
        xxx.commit()

        






