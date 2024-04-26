#!/usr/bin/python3
"""This script lists all cities based on state name"""


import MySQLdb
from sys import argv

if __name__ == "__main__":
    try:
        cities_db = MySQLdb.connect(host="localhost", port=3306,
                                    user=argv[1], passwd=argv[2], db=argv[3])
        cur = cities_db.cursor()
        query = ("SELECT cities.name FROM cities "
                 "JOIN states ON cities.state_id = states.id "
                 "WHERE  states.name = %s ORDER BY cities.id ASC")

        cur.execute(query, (argv[4],))
        rows = cur.fetchall()
        # Join the city names into a single string with commas
        cities = ", ".join(row[0] for row in rows)
        print(cities)
    except MySQLdb.Error as e:
        print("Error:", e)
    finally:
        if "cur" in locals():
            cur.close()
        if "cities_db" in locals():
            cities_db.close()
