from urllib.request import urlopen
#from urllib.parse import urlencode
import sqlite3
import xml.etree.ElementTree as ET

# conn = sqlite3.connect('trackdb.sqlite')
# cur = conn.cursor()

# cur.executescript('''
                  
# DROP TABLE IF EXISTS Artist;
# DROP TABLE IF EXISTS Album;
# DROP TABLE IF EXISTS Track;
                  
# CREATE TABLE Artist(
#                   id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
#                   name TEXT UNIQUE
# );
                  
# CREATE TABLE Album(
#                   id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
#                   artiste_id INTEGER,
#                   title TEXT UNIQUE
# );

# CREATE TABLE Track(
#                   id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
#                   title TEXT UNIQUE
#                   album_id INTEGER,
#                   artiste_id INTEGER,
#                   len INTEGER, rating INTEGER, count INTEGER
# );
                                               
# '''

# )
def lookup(d, key):
    found = False
    for child in d:
        if found:
            return child.text
        if child.tag == 'key' and child.text == key:
            found = True
    return None

f_xml = ET.parse('Library.xml')
all = f_xml.findall('dict/dict/dict')
i = 0
for entry in all:
    #if (lookup(entry, 'Track ID') is None):
    #    continue

    name = lookup (entry, 'Name')
    artist = lookup(entry, 'Artist')
    album = lookup(entry, 'Album')
    count = lookup(entry, 'Play Count')
    rating = lookup(entry, 'Rating')
    length = lookup(entry, 'Total Time')

    #if name is None or artist is None or album is None:
    #    continue

    print(name, artist, album, count, rating, length)

    i += 1
    if i > 7:
        break