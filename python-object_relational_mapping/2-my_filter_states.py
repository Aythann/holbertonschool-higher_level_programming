#!/usr/bin/python3
"""Displays states where name matches the argument."""
import sys
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        port=3306,
        charset="utf8",
    )

    cur = db.cursor()

    cur.execute(
        "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC"
        .format(sys.argv[4])
    )

    for row in cur.fetchall():
        print(row)

    cur.close()
    db.close()
