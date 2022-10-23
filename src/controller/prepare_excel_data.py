class PrepareExcelData:
    def __init__(self, data, db):
        self.data = data
        self.db = db

    def __str__(self):
        return self.data

    def prepare(self):
        conn = self.db
        cur = conn.cursor()
        cur.execute('SELECT * FROM books')
        books = cur.fetchall()
        print('books', books)
        cur.close()
        conn.close()
        return data
