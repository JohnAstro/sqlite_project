1) Run task.py, this will create the database
2) Running summary.py will display the summary of each table as well as the total number of albums per musician
3) To run update.py, you must run it through the cmd/terminal/shell and give it the command type, table name, and records.
    a) update.py only updates tables album, instrument, and musician.

    b) Here is the format of a command:
    python update.py [del/add] [table name]:[records]

    c) Each add command must follow the corresponding table's record order as shown below:
    python update.py add album:[name, id, date, type]
    python update.py add instrument:[id, type, key]
    python update.py add musician:[num, street, str_type, name, ssn]

    d) Each del command must give the primary key of the corresponding table as shown below:
    python update.py del album:[id]
    python update.py del instrument:[id]
    python update.py del musician:[ssn]