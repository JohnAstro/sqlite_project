import sqlite3
import csv

# Helper fuction that gets the contents from the given csv file
def get_contents(file_name, table):
    cur.execute(table)
    fin = open(file_name, 'r')
    contents = csv.reader(fin)
    next(contents)  # Skips the first row of csv file
    return contents

# Helper function that prints the contents of a given table
def print_table(table):
    select_all = "SELECT * FROM {}".format(table)
    res = cur.execute(select_all)

    print('--------------------')
    n = [x[0] for x in res.description]
    print(n)
    print('--------------------')
    for row in res : print(row)
    print('')

# Creates the tables with constraints in the database
def create_db():
    try:
        table1 = """
        CREATE TABLE Musician(
        num INT NOT NULL,
        street TEXT NOT NULL,
        str_type TEXT NOT NULL,
        name TEXT NOT NULL,
        ssn INT CHECK(ssn<=999999999),
        PRIMARY KEY (ssn));
        """
        contents = get_contents('musician.csv', table1)
        cur.executemany("INSERT INTO musician(num, street, str_type, name, ssn) VALUES (?, ?, ?, ?, ?);", contents)

        table2 = """
        CREATE TABLE Instrument(
        id INT,
        type TEXT NOT NULL CHECK(type='guitar' OR type='synthesizer' OR type='flute'),
        key TEXT NOT NULL CHECK(key='C' OR key='B' OR key='E' OR key='C-flat' OR key='B-flat' OR key='E-flat'),
        PRIMARY KEY (id));
        """
        contents = get_contents('instrument.csv', table2)
        cur.executemany("INSERT INTO instrument(id, type, key) VALUES (?, ?, ?);", contents)

        table3 = """
        CREATE TABLE Album(
        Name TEXT NOT NULL,
        id INT,
        date TEXT NOT NULL,
        type TEXT NOT NULL CHECK(type='CD' OR type='MC'),
        PRIMARY KEY (id));
        """
        contents = get_contents('album.csv', table3)
        cur.executemany("INSERT INTO album(Name, id, date, type) VALUES (?, ?, ?, ?);", contents)

        table4 = """
        CREATE TABLE Musician_album(
        ssn INT,
        album_id INT,
        PRIMARY KEY(ssn, album_id),
        FOREIGN KEY(ssn) REFERENCES musician,
        FOREIGN KEY(album_id) REFERENCES album(id));
        """

        contents = get_contents('musician-album.csv', table4)
        cur.executemany("INSERT INTO musician_album(ssn, album_id) VALUES (?, ?);", contents)

        table5 = """
        CREATE TABLE Album_instrument(
        album_id INT,
        instrument_id INT,
        PRIMARY KEY(album_id, instrument_id),
        FOREIGN KEY(album_id) REFERENCES album(id),
        FOREIGN KEY(instrument_id) REFERENCES instrument(id));
        """
        contents = get_contents('album-instrument.csv', table5)
        cur.executemany("INSERT INTO album_instrument(album_id, instrument_id) VALUES (?, ?);", contents)
    except:
        return

# Connect to databse
con = sqlite3.connect('project.db')
cur = con.cursor()
create_db() # Creates database if not created else do nothing

# Print tables
print_table('Musician')
print_table('Instrument')
print_table('Album')
print_table('Musician_album')
print_table('Album_instrument')

con.commit()
con.close()
