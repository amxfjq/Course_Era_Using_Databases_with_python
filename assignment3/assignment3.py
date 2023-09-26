import sqlite3
import xml.etree.ElementTree as ET

conn = sqlite3.connect('assignment3.sqlite')
cur = conn.cursor()
cur.executescript('''
                  drop table if exists artist;
                  drop table if exists genre;
                  drop table if exists album;
                  drop table if exists track;
                  
                  create table artist(
                  id integer not null primary key autoincrement unique,
                  name text unique
                  );
                  
                  create table genre(
                  id integer not null primary key autoincrement unique,
                  name text unique
                  );
                  
                  create table album(
                  id integer not null primary key autoincrement unique,
                  artist_id integer,
                  title text unique
                  );
                  
                  create table track(
                  id integer not null primary key autoincrement unique,
                  title text unique,
                  album_id integer,
                  genre_id integer,
                  len integer, rating integer, count integer
                  );
                  ''')

f_xml = ET.parse('Library_ass.xml')
data = f_xml.findall('dict/dict/dict')

def retrieve(x, key):
    yyy = False
    for i in x:
        if yyy:
            return i.text
        if i.tag == 'key' and i.text == key:
            yyy = True
    return '<no entry>'

for entry in data:

    name = retrieve(entry, 'Name')
    artist = retrieve(entry, 'Artist')
    genre = retrieve(entry, 'Genre')
    album = retrieve(entry, 'Album')
    len = retrieve(entry, 'Play Count')
    rating = retrieve(entry, 'Rating')
    count = retrieve(entry, 'Total Time')

    cur.execute('insert or ignore into artist(name) values(?)', (artist,))
    cur.execute('select id from artist where name = ?', (artist,))
    row = cur.fetchone()
    artist_id = row[0]

    cur.execute('insert or ignore into genre(name) values(?)', (genre,))
    cur.execute('select id from genre where name = ?', (genre,))
    row = cur.fetchone()
    genre_id = row[0]

    cur.execute('insert or ignore into album(artist_id, title) values(?,?)', (artist_id, album))
    cur.execute('select id from album where title = ?', (album,))
    row = cur.fetchone()
    album_id = row[0]

    cur.execute('insert or replace into track(title, album_id, genre_id, len, rating, count) values(?,?,?,?,?,?)', (name, album_id, genre_id, len, rating, count))
    
    conn.commit()