from db import connect


def create_indexes():
    with connect() as driver:
        queries = [
            "CREATE INDEX ON :Servidor(cpf)",
            "CREATE INDEX ON :Servidor(nome)",
            "CREATE INDEX ON :Contrato(orgId)",
            "CREATE INDEX ON :Servidor(cpf, nome)",
            "CREATE INDEX ON :Empresa(cnpj)",
            "CREATE INDEX ON :ItemLicitacao(numeroProcesso)",
            "CREATE INDEX ON :Orgao(id)",
            "CREATE INDEX ON :Licitacao(numeroLicitacao)",
            "CREATE INDEX ON :Licitacao(numeroProcesso)",
            "CREATE INDEX ON :Licitacao(numeroLicitacao, numeroProcesso)",
            "CREATE INDEX ON :ParticipanteLicitacao(numeroLicitacao)",
            "CREATE INDEX ON :ParticipanteLicitacao(codigoItemCompra)",
            "CREATE INDEX ON :Socio(cnpj)",
            "CREATE INDEX ON :Socio(cpfCnpj)",
        ]

        with driver.session() as session:
            tx = session.begin_transaction()
            for query in queries:
                tx.run(query)
            tx.commit()
