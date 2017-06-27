"""Biblitoteca pra implementar as chamadas ao SGBD"""
import psycopg2

#   ----------------------------   FUNCTIONS   -----------------------------   #

class SGBD:
    """Classe para realizar as tarefas do lado do banco de dados SQL"""
    def __init__(self, dbname=None, user=None, password=None, host=None, port=None):
        path = "dbname='%s' user='%s' password='%s' host= '%s' port='%s'" % (dbname, user, password, host, port)
        self.conn = psycopg2.connect(path)
        self.cur = self.conn.cursor()

    def inserir(self, item, quantity, price):
        """Function that insert SQL values"""
        self.cur.execute("INSERT INTO store VALUES(%s,%s,%s)", (item, quantity, price))
        self.conn.commit()

    def visualizar(self):
        """Function that returns SQL array values"""
        self.cur.execute("SELECT * FROM store")
        return self.cur.fetchall()

    def deletar(self, item):
        """Function that delete from SQL defined value"""
        self.cur.execute("DELETE FROM store WHERE item=%s", (item,))
        self.conn.commit()

    def atualizar(self, item, quantity, price):
        """Function that delete from SQL defined value"""
        self.cur.execute("UPDATE store SET quantity=%s, price=%s WHERE item=%s", (quantity, price, item))
        self.conn.commit()

    def encerrar(self):
        self.conn.close()

#   ------------------------------   EOF   ---------------------------------   #
