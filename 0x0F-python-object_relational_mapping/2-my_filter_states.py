#!/usr/bin/python3
"""
This script displays all values in the states table of hbtn_0e_0_usa
where name matches the provided state name.
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    try:
        # Connect to the MySQL server
        states_db = MySQLdb.connect(host="localhost", port=3306,
                                    user=argv[1], passwd=argv[2], db=argv[3])

        # Create a cursor
        cur = states_db.cursor()

        # Execute the query (use .format to get state passed)
        cur.execute("SELECT * FROM states WHERE name LIKE BINARY '{}' \
            ORDER BY id ASC".format(argv[4]))

        # Fetch all rows
        rows = cur.fetchall()

        # Display the results
        for row in rows:
            print(row)

    except MySQLdb.Error as e:
        print("Error:", e)

    finally:
        # Close the cursor and connection
        if 'cur' in locals():
            cur.close()
        if 'states_db' in locals():
            states_db.close()
