import sqlite3

def create_table():
    conn = sqlite3.connect('events.db')

    conn.execute('''CREATE TABLE EVENTS
            (ID            INT    NOT NULL,
            NAME           TEXT    NOT NULL,
            OUTDOORS       BOOLEAN     NOT NULL,
            BODYPART       TEXT    NOT NULL,
            COST           REAL    NOT NULL);''')
    
    conn.commit()
    conn.close()

def input_event(event_string):
    conn = sqlite3.connect('events.db')

    conn.execute(event_string)

    conn.commit()
    conn.close()


def previous_id():
    conn = sqlite3.connect('events.db')

    db_items = conn.execute("SELECT id from EVENTS")
    id_list = []
    for db_item in db_items:
        id_list.append(db_item[0])

    conn.commit()
    conn.close()

    return id_list[-1]


def database_entry(value_list):
    return f"INSERT INTO EVENTS (ID, NAME, OUTDOORS, BODYPART, COST) \
        VALUES ({value_list[0]}, '{value_list[1]}', {value_list[2]}, '{value_list[3]}', {value_list[4]} )"

def database_extract():
    conn = sqlite3.connect(":memory:")
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    c.execute('select * from EVENTS')
    L = []
    for row in c.fetchall():
        L.append(dict(row))
    return L

'''
conn = sqlite3.connect('events.db')

conn.execute("DELETE from EVENTS where ID = 0;") 
conn.execute("INSERT INTO EVENTS (ID,NAME,OUTDOORS,BODYPART,COST) \
     VALUES (0, 'a', False, 'a', 0)");
conn.commit()
conn.close()
'''
