class PrepareExcelData:
    def __init__(self, data, db):
        self.data = data
        self.conn = db
        self.cursor = db.cursor()

    def __str__(self):
        return self.data

    def prepare(self):
        self.create_table_dividends()
        self.conn.commit()
        self.cursor.close()
        self.conn.close()

    def create_table_dividends(self):
        return self.cursor.execute('CREATE TABLE IF NOT EXISTS dividendos (id serial PRIMARY KEY,'
                                   'entrada varchar (50) NOT NULL,'
                                   'data date NOT NULL,'
                                   'movimentacao varchar (50) NOT NULL,'
                                   'produto text,'
                                   'instituicao varchar (150) NOT NULL,'
                                   'quantidade int NOT NULL,'
                                   'preco_unitario double precision NOT NULL,'
                                   'valor_opercao double precision NOT NULL,'
                                   'criado_em date DEFAULT CURRENT_TIMESTAMP);'
                                   )
