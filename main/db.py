import sqlite3


# conn.execute('''CREATE TABLE EVENTS
#          (ID            INT    NOT NULL,
#          NAME           TEXT    NOT NULL,
#          OUTDOORS       BOOLEAN     NOT NULL,
#          BODYPART       TEXT    NOT NULL,
#          COST           REAL    NOT NULL);''')

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

conn = sqlite3.connect('events.db')

#conn.execute("DELETE from EVENTS where ID = 0;") 
# conn.execute("INSERT INTO EVENTS (ID,NAME,OUTDOORS,BODYPART,COST) \
#     VALUES (0, 'a', False, 'a', 0)");
conn.commit()
conn.close()
