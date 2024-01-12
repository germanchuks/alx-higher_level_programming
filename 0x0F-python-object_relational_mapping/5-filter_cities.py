#!/usr/bin/python3
""" Takes in the name of a state as an argument and lists all cities of that
state, using the database hbtn_0e_4_usa """
import MySQLdb
from sys import argv

if __name__ == '__main__':
    conn = MySQLdb.connect(host="localhost", port=3306,
                           user=argv[1], passwd=argv[2], db=argv[3])
    cur = conn.cursor()

    input_name = argv[4]

    query = '''SELECT cities.name
            FROM cities
            JOIN states ON cities.state_id = states.id
            WHERE states.name = %s
            ORDER BY cities.id ASC
            '''
    cur.execute(query, (input_name,))

    query_rows = cur.fetchall()
    cities_by_state = ', '.join(row[0] for row in query_rows)
    print(cities_by_state)

    cur.close()
    conn.close()
