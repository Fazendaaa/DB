"""This program implements book store functions"""
import sqlite3

#   ----------------------------   FUNCTIONS   -----------------------------   #

class Database:
    """Class that performance all the sugar behind the SQL side"""

    def __init__(self, filename):
        """Function that initialize SQL table"""
        self.conn = sqlite3.connect(filename)
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS book(id INTEGER PRIMARY \
        KEY, title text, author text, year integer, isbn integer)")
        self.conn.commit()

    def insert(self, title, author, year, isbn):
        """Function that inserts SQL values"""
        self.cur.execute("INSERT INTO book VALUES(NULL, ?, ?, ?, ?)", (title, author, year, isbn))
        self.conn.commit()

    def view(self):
        """Function that returns SQL array values"""
        self.cur.execute("SELECT * FROM book")

        return self.cur.fetchall()

    def search(self, title='', author='', year='', isbn=''):
        """Function that searches SQL by given keys"""
        self.cur.execute("SELECT * FROM book WHERE title=? OR author=? OR \
        year=? OR isbn =?", (title, author, year, isbn))

        return self.cur.fetchall()

    def delete(self, id):
        """Function that deletes from SQL defined value"""
        self.cur.execute("DELETE FROM book WHERE id=?", (id,))
        self.conn.commit()

    def update(self, id, title, author, year, isbn):
        """Function that updates from SQL defined value"""
        self.cur.execute("UPDATE book SET title=?, author=?, year=?, isbn=? \
        WHERE id=?", (title, author, year, isbn, id))
        self.conn.commit()

    def close(self):
        """Function that terminates the SQL connection"""
        self.conn.close()

#   ------------------------------   EOF   ---------------------------------   #
