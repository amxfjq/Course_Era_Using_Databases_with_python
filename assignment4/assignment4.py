import json
import sqlite3

conn = sqlite3.connect('assignment4.sqlite')
cur = conn.cursor()

cur.executescript('''
                  drop table if exists user;
                  drop table if exists course;
                  drop table if exists member;

                  create table user(
                  id integer not null primary key autoincrement unique,
                  name text unique
                  );

                  create table course(
                  id integer not null primary key autoincrement unique,
                  title text unique
                  );

                  create table member(
                  role integer,
                  user_id integer,
                  course_id integer,
                  primary key (user_id, course_id)
                  );
                  
''')

uf_json = open('roster_data.json').read()
f_json = json.loads(uf_json)

for entry in f_json:
    user = entry[0]
    course = entry[1]
    role = entry[2]

    cur.execute('insert or ignore into user(name) values(?)', (user,))
    cur.execute('select id from user where name = ?', (user,))
    user_id = cur.fetchone()[0]

    cur.execute('insert or ignore into course(title) values(?)', (course,))
    cur.execute('select id from course where title = ?', (course,))
    course_id = cur.fetchone()[0]

    cur.execute('insert or replace into member(role, user_id, course_id) values(?, ?, ?)', (role, user_id, course_id))

    conn.commit()