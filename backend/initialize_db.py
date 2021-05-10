import sqlite3

conn = sqlite3.connect('irlrpg.db')

conn.execute('''CREATE TABLE CHARACTERS
        (ID INT PRIMARY KEY   NOT NULL,
        NAME          TEXT    NOT NULL,
        STR           INT     NOT NULL,
        END           INT     NOT NULL,
        WIS           INT     NOT NULL,
        INT           INT     NOT NULL,
        CON           INT     NOT NULL,
        CHA           INT     NOT NULL,
        SPT           INT     NOT NULL);''')

