import sqlite3
import sys

# Prints the given table
def print_table(t):
    select_all = "SELECT * FROM {}".format(t)
    res = cur.execute(select_all)

    print('--------------------')
    n = [x[0] for x in res.description]
    print(n)
    print('--------------------')
    for row in res : print(row)
    print('')

# Executes insert with given table and records
def insert_record(t, records):
    if t == "Album" or t == "album":
        print("Adding record...", end="\n\n")
        cur.execute("INSERT INTO {}(Name, id, date, type) VALUES (?, ?, ?, ?);".format(t), records)
        print("Updated {} table:".format(t))  
        print_table(t)  
    elif t == "Instrument" or t == "instrument":
        print("Adding record...", end="\n\n")
        cur.execute("INSERT INTO {}(id, type, key) VALUES (?, ?, ?);".format(t), records)
        print("Updated {} table:".format(t))
        print_table(t)
    else:
        print("Adding record...", end="\n\n")
        cur.execute("INSERT INTO {}(num, street, str_type, name, ssn) VALUES (?, ?, ?, ?, ?);".format(t), records)
        print("Updated {} table:".format(t))
        print_table(t)

# Executes delete with given table and records
def delete_record(t, key):
    if t == "Musician" or t == "musician":
        print("Deleting record...", end="\n\n")
        cur.execute("DELETE FROM {} WHERE ssn={}".format(t, key))
        print("Updated {} table:".format(t))
        print_table(t)
    else:
        print("Deleting record...", end="\n\n")
        cur.execute("DELETE FROM {} WHERE id={}".format(t, key))
        print("Updated {} table:".format(t))
        print_table(t)

# Parses the records for add/del command
# returns table and records/key
def parse_records(records, command_type):
    # Table name
    t = records[2].split(':')[0]

    # If add, parse all the given records
    if command_type == 'Add' or command_type == 'add':

        # Parse words after ':' and append to temp
        temp = []
        for x in records[2:]:
            if ':' in x:
                temp.append(x.split(':')[1])
            else:
                temp.append(x)

        r = []                  # Will hold fully parsed records
        i = 0                   # Index for ta
        size = len(temp) - 1    # Size of ta

        # Iterate through temp, append on different cases
        while i <= size:
            # Record with a space gets appended together
            if not ',' in temp[i] and i != size:
                r.append(temp[i] + " " + temp[i + 1])
                i += 1
            # Last record gets appended
            elif i == size:
                r.append(temp[i])
            # Record with comma gets appended without it
            else:
                r.append(temp[i].split(',')[0])
            i += 1
        # Return table & fully parsed records   
        return (t, r)
    # If del, parse the key in the given records
    else:
        key = records[2].split(':')[1]
        return (t, key)

# Handles command execution
def run_command(records, command_type):
    # Parse records given command type
    (t, data) = parse_records(records, command_type)

    # Table before command 
    print("{} table: ".format(t), end="\n\n")
    print_table(t)

    # Execute insert
    if command_type == 'add' or command_type == 'Add':
        insert_record(t, data)
    # Execute delete
    else:
        delete_record(t, data)


# Main
# Updates the tables: album, instrument, musician
# Must be in given order for the following tables:
# album         => name, id, date, type
# instrument    => id, type, key
# musician      => num, street, street_type, name, ssn
# Connect to databse
con = sqlite3.connect('project.db')
cur = con.cursor()

# Fetch command
records = []
for x in sys.argv:
    records.append(x)

# records[1] => command type (i.e add/del)
run_command(records, records[1])

con.commit()
con.close()
