import sqlite3

def table_summary(table, col):
    # Print count of given column
    select_all = "SELECT COUNT({}) AS Total FROM {}".format(col, table)
    res = cur.execute(select_all)

    print("Number of {}s: ".format(table), end="")
    for row in res : print(row)


    # Print table
    select_all = "SELECT * FROM {}".format(table)
    res = cur.execute(select_all)

    print("List:")
    print('--------------------')
    n = [x[0] for x in res.description]
    print(n)
    print('--------------------')
    for row in res : print(row)
    print('')
    return

def count_musician_albums():
    select_all = """
    SELECT name AS Musician, COUNT(album_id) AS Album_count
    FROM Musician_album NATURAL JOIN Musician
    GROUP BY ssn
    """
    res = cur.execute(select_all)

    print("List of Musicians and total number of albums per Musician:")
    print('--------------------')
    n = [x[0] for x in res.description]
    print(n)
    print('--------------------')
    for row in res : print(row)
    print('')
    return

    

# Connect to databse
con = sqlite3.connect('project.db')
cur = con.cursor()

# Get summary of the database
table_summary('Musician', 'ssn')
table_summary('Album', 'id')
table_summary('Instrument', 'id')
count_musician_albums()

con.commit()
con.close()
