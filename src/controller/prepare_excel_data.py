class PrepareExcelData:
    def __init__(self, data, db):
        self.data = data
        self.conn = db
        self.cursor = db.cursor()

    def __str__(self):
        return self.data

    def prepare(self):
        self.cursor.execute('SELECT * FROM books')
        books = self.cursor.fetchall()
        print('books', books)
        self.cursor.close()
        self.conn.close()
        return books
