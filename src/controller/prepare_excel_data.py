import pandas as pd


class PrepareExcelData:
    def __init__(self, data, db):
        self.data = data
        self.conn = db
        self.cursor = db.cursor()

    def __str__(self):
        return self.data

    def prepare(self):
        self.data.rename(
            columns={'Entrada/Saída': 'entrada', 'Data': 'data', 'Movimentação': 'movimentacao', 'Produto': 'produto', 'Instituição': 'instituicao', 'Quantidade': 'quantidade', 'Preço unitário': 'preco_unitario', 'Valor da Operação': 'valor_operacao'}, inplace=True)

        self.create_table_dividends()
        self.append_from_df_to_db()
        self.conn.commit()
        self.cursor.close()
        self.conn.close()

    def insert_into_table(self, entrada, data, movimentacao, produto, instituicao,
                          quantidade, preco_unitario, valor_operacao):
        insert_into_dividendos = ("""INSERT INTO dividendos (entrada, data, movimentacao, produto, instituicao,
                         quantidade, preco_unitario, valor_operacao)
                    VALUES(%s,%s,%s,%s,%s,%s,%s,%s);""")
        row_to_insert = (entrada, data, movimentacao, produto, instituicao,
                         quantidade, preco_unitario, valor_operacao)
        self.cursor.execute(insert_into_dividendos, row_to_insert)

    def append_from_df_to_db(self):
        for i, row in self.data.iterrows():
            self.insert_into_table(row['entrada'], row['data'],
                                   row['movimentacao'], row['produto'], row['instituicao'], row['quantidade'], row['preco_unitario'], row['valor_operacao'])

    def create_table_dividends(self):
        return self.cursor.execute('CREATE TABLE IF NOT EXISTS dividendos (id serial PRIMARY KEY,'
                                   'entrada varchar (50) NOT NULL,'
                                   'data date NOT NULL,'
                                   'movimentacao varchar (50) NOT NULL,'
                                   'produto text,'
                                   'instituicao varchar (150) NOT NULL,'
                                   'quantidade int NOT NULL,'
                                   'preco_unitario double precision NOT NULL,'
                                   'valor_operacao double precision NOT NULL,'
                                   'criado_em date DEFAULT CURRENT_TIMESTAMP);'
                                   )
