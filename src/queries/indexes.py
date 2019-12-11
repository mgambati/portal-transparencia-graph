import db


queries = [
    "CREATE INDEX ON :Servidor(id)",
    "CREATE INDEX ON :Servidor(nome, cpf)",
    "CREATE INDEX ON :Empresa(cnpj)",
    "CREATE INDEX ON :Orgao(id)",
    "CREATE INDEX ON :Contrato(id)",
    "CREATE INDEX ON :Contrato(cnpjContratado)",
    "CREATE INDEX ON :Contrato(orgId)",
    "CREATE INDEX ON :Licitacao(id)",
    "CREATE INDEX ON :Licitacao(orgId)",
    "CREATE INDEX ON :ItemLicitacao(licitacaoId)",
    "CREATE INDEX ON :ItemLicitacao(cnpjVencedor)",
    "CREATE INDEX ON :ParticipanteLicitacao(licitacaoId)",
    "CREATE INDEX ON :ParticipanteLicitacao(cnpj)",
    "CREATE INDEX ON :Socio(cnpj)",
    "CREATE INDEX ON :Socio(cpfCnpj)",
    "CREATE INDEX ON :Socio(servidorId)",
    "CREATE INDEX ON :TermoAditivo(contratoId)",
    "CREATE INDEX ON :TermoAditivo(numero)",
]


def create_indexes():
    print("Creating indexes...")
    with db.connect() as driver:
        with driver.session() as session:
            tx = session.begin_transaction()
            for query in queries:
                tx.run(query)
            tx.commit()
